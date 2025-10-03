import datetime
from datetime import datetime, timedelta
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from config import load_config
from loader import ow
from src.states.states import StatesGroup as sg
from src.keyboards.default.menuKey import MenuKeyboard
from src.keyboards.default.districtsKey import DistrictsKeyboard
from src.keyboards.default.periodSelectKey import PeriodSelectKeyboard
from src.filters.filters import DistrictFilter
from src.helper.get_long_lat import get_long_lat
from src.helper.animate_load import animate_loading
from src.helper.parser import parse_air_pollution_data, format_air_quality_message
from src.helper.tashkent_radius_check import is_in_tashkent
from src.helper.data_to_xsxl import save_air_pollution_history_to_buffer

config = load_config()
router: Router = Router()


@router.message(StateFilter(sg.HD_D), F.text == "⬅️ Back")
async def back_handler(message: types.Message, state: FSMContext):
    await message.answer("You are back to the main menu.", reply_markup=MenuKeyboard)
    await state.set_state(sg.MM)


@router.message(StateFilter(sg.HD_D), DistrictFilter())
async def district_selection_handler(message: types.Message, state: FSMContext):
    selected_district = message.text
    lon, lat = get_long_lat(selected_district)
    await state.update_data(lon=lon, lat=lat)
    await message.answer("Please select a the period:", reply_markup=PeriodSelectKeyboard)
    await state.set_state(sg.HD_DT)


@router.message(StateFilter(sg.HD_D))
async def location_handler(message: types.Message, state: FSMContext):
    if message.text:
        await message.answer("Please select from the keyboard options.")
        return

    if not message.location:
        await message.answer("Please share your location using the Telegram location feature.")
        return

    lon, lat = message.location.longitude, message.location.latitude
    in_radius = is_in_tashkent(
        lat=lat, lon=lon, geojson_file="tashkent_city.geojson")

    if not in_radius:
        await message.answer("You are outside the Tashkent city limits. Please select a district from the list.")
        return

    await state.update_data(lon=lon, lat=lat)
    await state.set_state(sg.HD_DT)
    await message.answer("Please select a the period:", reply_markup=PeriodSelectKeyboard)


@router.message(StateFilter(sg.HD_DT), F.text == "⬅️ Back")
async def back_handler(message: types.Message, state: FSMContext):
    await message.answer("You are back to the district selection.", reply_markup=DistrictsKeyboard)
    await state.set_state(sg.HD_D)


@router.message(StateFilter(sg.HD_DT))
async def period_selection_handler(message: types.Message, state: FSMContext):
    selected_period = message.text
    if selected_period not in ["🗓 Last 3 days", "🗓 Last 7 days", "🗓 Last 30 days"]:
        await message.answer("Invalid period selected. Please choose a valid period.")
        return

    data = await state.get_data()
    lon, lat = data.get("lon"), data.get("lat")
    if not lon or not lat:
        await message.answer("Location data is missing. Please try again.")
        await state.set_state(sg.MM)
        return

    start_time, end = None, None
    await message.answer("Loading...", reply_markup=MenuKeyboard)
    if selected_period == "🗓 Last 3 days":
        start_time = int((datetime.now() - timedelta(days=3)).timestamp())
    elif selected_period == "🗓 Last 7 days":
        start_time = int((datetime.now() - timedelta(days=7)).timestamp())
    elif selected_period == "🗓 Last 30 days":
        start_time = int((datetime.now() - timedelta(days=30)).timestamp())
    
    end = int(datetime.now().timestamp())
    res = ow.get_air_pollution_history(lat=lat, lon=lon, start=start_time, end=end)
    buf = save_air_pollution_history_to_buffer(res)
    file = types.BufferedInputFile(buf.read(), filename="air_pollution_history.xlsx")
    await message.answer_document(file, caption=f"{selected_period[2:]} data")
    await state.set_state(sg.MM)