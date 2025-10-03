from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


DistrictsKeyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="📍 Share my location", request_location=True), 
    ],
    [
        KeyboardButton(text="Bektemir"),
        KeyboardButton(text="Mirzo Ulug'bek"),
    ],
    [
        KeyboardButton(text="Mirobod"),
        KeyboardButton(text="Olmazor"),
    ],
    [
        KeyboardButton(text="Sirg'ali"),
        KeyboardButton(text="Uchtepa"),
    ],
    [
        KeyboardButton(text="Chilonzor"),
        KeyboardButton(text="Shayxontohur"),
    ],
    [
        KeyboardButton(text="Yunusobod"),
        KeyboardButton(text="Yakkasaroy"),
    ],
    [
        KeyboardButton(text="Yashnobod"),
    ],
    [
        KeyboardButton(text="⬅️ Back"),
    ]
], resize_keyboard=True)
