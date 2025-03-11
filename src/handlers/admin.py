import time
from aiogram import Router, F
from aiogram import types
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram.filters import StateFilter
from config import load_config
from loader import db
from src.keyboards.default.menuKeyboard import AdminKeyboard, MenuKeyboard
from src.helper.funcs import create_start_text_text
from src.filters.filters import AdminFilter
from src.states.states import StatesGroup as sg


config = load_config()
router: Router = Router()


@router.message(Command("admin"), AdminFilter())
async def admin_command_handler(message: types.Message):
    await message.answer("Admin panelga xush kelibsiz!", reply_markup=AdminKeyboard)


@router.message(lambda message: message.text == "📊 Statistika", AdminFilter())
async def get_stat(message: types.Message):
    users_count = db.get_users_count()
    completed_users_count = db.get_completed_users_count()
    await message.answer(f"📊 Barcha foydalanuvchilar soni: {users_count}\n✅ Kursni tugatganlar soni: {completed_users_count}")


@router.message(lambda message: message.text == "🔙 Orqaga", AdminFilter(), StateFilter(None))
async def back_menu(message: types.Message):
    user_id = message.from_user.id

    short_link = config.tg_bot.BOT_URL + "?start=" + str(user_id)
    msg = create_start_text_text(short_link)
    await message.answer_photo(photo=msg.photo_id, caption=msg.text_1, parse_mode=ParseMode.HTML)
    await message.answer(text=msg.text_2, reply_markup=MenuKeyboard, parse_mode=ParseMode.HTML)


@router.message(lambda message: message.text == "📤 Ommaviy xabar", AdminFilter())
async def send_public_message(message: types.Message, state: FSMContext):
    await state.set_state(sg.message)
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="🔙 Orqaga")
            ]
        ],
        resize_keyboard=True
    )

    await message.answer("Foydalanuvcihilarga yubormoqchi bo'lgan xabaringizni yuboring:", reply_markup=keyboard)


@router.message(StateFilter(sg.message), lambda message: message.text == "🔙 Orqaga")
async def back_handler(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Bekor qilindi!", reply_markup=AdminKeyboard)


@router.message(StateFilter(sg.message))
async def confirm_message_handler(message: types.Message, state: FSMContext):
    await state.set_state(sg.confirmation)
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="✅ Ha"),
                types.KeyboardButton(text="❌ Yo'q")
            ]
        ],
        resize_keyboard=True
    )
    await state.update_data(message_id = message.message_id)
    await message.answer("Xabarni yuborishni tasdiqlaysizmi?", reply_markup=keyboard)

@router.message(StateFilter(sg.confirmation), lambda message: message.text == "❌ Yo'q")
async def cancel_message_handler(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Xabar yuborish bekor qilindi!", reply_markup=AdminKeyboard)


@router.message(StateFilter(sg.confirmation), lambda message: message.text == "✅ Ha")
async def send_message_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    message_id = data.get("message_id")
    await message.answer("Xabar yuborilmoqda...", reply_markup=AdminKeyboard)
    users = db.get_all_users()
    success = 0
    fail = 0
    for user in users:
        try:
            await message.bot.copy_message(
                chat_id=user.get("telegram_id"),
                from_chat_id=message.chat.id,
                message_id=message_id
            )
            success += 1
            time.sleep(0.05)
        except Exception as e:
            fail += 1
            print(f"Error sending message to user {user['user_id']}: {e}")
    await message.answer(f"Xabar {success} ta foydalanuvchiga muvaffaqiyatli yuborildi, {fail} ta foydalanuvchiga yuborishda xatolik yuz berdi.")
    await state.clear()

@router.message(Command("logs"))
async def get_logs(message: types.Message):
    if not str(message.from_user.id) in config.tg_bot.DEVID.split(","):
        return
    await message.answer("Sending logs...")
    
 # Send the log file
    log_file = types.FSInputFile("bot_logs.log")  # Pass the file path as a string
    await message.bot.send_document(message.chat.id, log_file)
    
    # Send the database file
    db_file = types.FSInputFile("users.db")  # Pass the file path as a string
    await message.bot.send_document(message.chat.id, db_file)
    await message.answer("Logs sent!")