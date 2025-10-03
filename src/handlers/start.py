from aiogram import Router, F
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import CommandStart, CommandObject
from config import load_config
from src.keyboards.default.menuKey import MenuKeyboard
from src.states.states import StatesGroup as sg


config = load_config()
router: Router = Router()


@router.message(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Welcome to Air Polluton bot to check air quality in Tashkent city. \nUse the buttons below to navigate through the bot.", reply_markup=MenuKeyboard)
    await state.set_state(sg.MM)