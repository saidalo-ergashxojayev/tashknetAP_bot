from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


MenuKeyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="🔍 Check air quality (live)")
    ],
    [
        KeyboardButton(text="📈 Compare air quality in districts")
    ],
    [
        KeyboardButton(text="📂 Get historical data"),
    ],
], resize_keyboard=True)
