import asyncio
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from config import load_config
from loader import ow
from src.states.states import StatesGroup as sg
from src.keyboards.default.menuKey import MenuKeyboard
from src.filters.filters import DistrictFilter
from src.helper.get_long_lat import get_long_lat
from src.helper.animate_load import animate_loading
from src.helper.parser import parse_air_pollution_data, format_air_quality_message
from src.helper.tashkent_radius_check import is_in_tashkent
config = load_config()
router: Router = Router()


@router.message(StateFilter(sg.ChL_ChD), F.text == "⬅️ Back")
async def back_handler(message: types.Message, state: FSMContext):
    await message.answer("You are back to the main menu.", reply_markup=MenuKeyboard)
    await state.set_state(sg.MM)



@router.message(StateFilter(sg.ChL_ChD), DistrictFilter())
async def district_selection_handler(message: types.Message, state: FSMContext):
    selected_district = message.text
    lon_lat_res = get_long_lat(selected_district)
    
    if lon_lat_res is None:
        await message.answer("Could not find the location for the selected district. Please try again.")
        return
    
    lat, lon = lon_lat_res
    stop_event = asyncio.Event()
    msg = await message.answer("Loading...")
    
    animation_task = asyncio.create_task(
        animate_loading(msg, "Loading", 0.1, stop_event)
    )
    
    try:
        await asyncio.sleep(1)
        result = ow.get_air_pollution(lat=lat, lon=lon)
        
        if result is None:
            stop_event.set()
            await animation_task
            await message.answer("Failed to retrieve air quality data. Please try again later.")
            return
        
        # Parse the air pollution data
        parsed_data = parse_air_pollution_data(result)
        
        if parsed_data is None:
            stop_event.set()
            await animation_task
            await message.answer("Failed to process air quality data. Please try again later.")
            return
        
        # Stop loading animation
        stop_event.set()
        await animation_task
        
        # Format and send the response
        response_message = format_air_quality_message(parsed_data)
        await message.answer(response_message, parse_mode="HTML")
        
    except Exception as e:
        stop_event.set()
        await animation_task
        print(f"Error in district_selection_handler: {e}")
        await message.answer("An error occurred while fetching air quality data. Please try again later.")

@router.message(StateFilter(sg.ChL_ChD))
async def location_handler(message: types.Message, state: FSMContext):
    if message.text:
        await message.answer("Please select from the keyboard options.")
        return

    if not message.location:
        await message.answer("Please share your location using the Telegram location feature.")
        return
    
    lon, lat = message.location.longitude, message.location.latitude
    in_radius = is_in_tashkent(lat=lat, lon=lon, geojson_file="tashkent_city.geojson")

    if not in_radius:
        await message.answer("You are outside the Tashkent city limits. Please select a district from the list.")
        return

    stop_event = asyncio.Event()
    msg = await message.answer("Loading...")
    
    animation_task = asyncio.create_task(
        animate_loading(msg, "Loading", 0.05, stop_event)
    )
    
    try:
        await asyncio.sleep(1)
        result = ow.get_air_pollution(lat=lat, lon=lon)
        
        if result is None:
            stop_event.set()
            await animation_task
            await message.answer("Failed to retrieve air quality data. Please try again later.")
            return
        
        # Parse the air pollution data
        parsed_data = parse_air_pollution_data(result)
        
        if parsed_data is None:
            stop_event.set()
            await animation_task
            await message.answer("Failed to process air quality data. Please try again later.")
            return
        
        # Stop loading animation
        stop_event.set()
        await animation_task
        
        # Format and send the response
        response_message = format_air_quality_message(parsed_data)
        await message.answer(response_message, parse_mode="HTML")
        
    except Exception as e:
        stop_event.set()
        await animation_task
        print(f"Error in district_selection_handler: {e}")
        await message.answer("An error occurred while fetching air quality data. Please try again later.")

