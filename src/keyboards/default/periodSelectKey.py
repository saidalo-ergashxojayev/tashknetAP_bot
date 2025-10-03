from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


PeriodSelectKeyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="🗓 Last 3 days")
    ],
    [
        KeyboardButton(text="🗓 Last 7 days")
    ],
    [
        KeyboardButton(text="🗓 Last 30 days"),
    ],
    [
        KeyboardButton(text="⬅️ Back")
    ]
], resize_keyboard=True)
