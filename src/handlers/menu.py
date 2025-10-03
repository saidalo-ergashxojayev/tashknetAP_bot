import asyncio
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from config import load_config
from loader import ow
from config.consts import DISTRICTS, DISTRICTS_LONG_LAT
from src.states.states import StatesGroup as sg
from src.keyboards.default.districtsKey import DistrictsKeyboard
from src.helper.animate_load import animate_loading
from src.helper.parser import parse_air_pollution_data, format_air_quality_message
from src.helper.plotter import create_air_quality_graph

config = load_config()
router: Router = Router()


@router.message(F.text == "🔍 Check air quality (live)")
async def check_AQ_handler(message: types.Message, state: FSMContext):
    await message.answer("Please select your district:", reply_markup=DistrictsKeyboard)
    await state.set_state(sg.ChL_ChD)

@router.message(F.text == "📂 Get historical data")
async def get_historical_data_handler(message: types.Message, state: FSMContext):
    await message.answer("Please select your district:", reply_markup=DistrictsKeyboard)
    await state.set_state(sg.HD_D)


@router.message(F.text == "📈 Compare air quality in districts")
async def compare_AQ_handler(message: types.Message, state: FSMContext):
    msg = await message.answer("Preparing comparison data, please wait...")
    stop_event = asyncio.Event()
    
    animation_task = asyncio.create_task(
        animate_loading(msg, "Preparing comparison data, please wait", 1, stop_event)
    )

    try:
        districts_data = []
        for district_id, (lat, lon) in DISTRICTS_LONG_LAT.items():  # FIX unpacking
            district_name = DISTRICTS[district_id]
            try:
                result = ow.get_air_pollution(lat=lat, lon=lon)
                parsed_data = parse_air_pollution_data(result)
                districts_data.append((district_name, parsed_data))
                await asyncio.sleep(0.2)
            except Exception as e:
                print(f"Error fetching data for {district_name}: {e}")
                districts_data.append((district_name, None))

        stop_event.set()
        await animation_task

        valid_data_count = sum(1 for _, data in districts_data if data is not None)
        if valid_data_count == 0:
            await message.answer("❌ Failed to retrieve air quality data.")
            return

        # 🔥 Create graph
        img_buf = create_air_quality_graph(districts_data)
        img = types.BufferedInputFile(img_buf.getvalue(), filename="air_quality_comparison.png")
        # Send image as photo
        await message.answer_photo(photo=img, caption="📊 Air Quality Index comparison across districts")

    except Exception as e:
        stop_event.set()
        await animation_task
        print(f"Error in compare_AQ_handler: {e}")
        await message.answer("An error occurred while fetching air quality data. Please try again later.")


