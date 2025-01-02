from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


MenuKeyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="🔗 Taklif havolasi")
    ],
    [
        KeyboardButton(text="🚀 Maxsus linkni olish"),
    ],
], resize_keyboard=True)

AdminKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📊 Statistika"),
            KeyboardButton(text="📤 Ommaviy xabar"),
        ],
        [
            KeyboardButton(text="🔙 Orqaga"),
        ]
    ], resize_keyboard=True

)