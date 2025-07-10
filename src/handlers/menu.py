from aiogram import Router, types
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.context import FSMContext
from config import load_config
from src.keyboards.default.menuKeyboard import MenuKeyboard
from src.helper.funcs import create_start_text_text
from aiogram.utils.deep_linking import create_start_link
from loader import db


config = load_config()
router: Router = Router()

REQUIRED_CHANNELS = config.tg_bot.REQUIRED_CHANNELS.split(",")


@router.message(lambda message: message.text == "🔗 Taklif havolasi")
async def starty_link_handler(message: types.Message):
    user_id = message.from_user.id
    short_link = config.tg_bot.BOT_URL + "?start=" + str(user_id)

    msg = create_start_text_text(short_link)
    await message.answer_photo(photo=msg.photo_id, caption=msg.text_1, parse_mode=ParseMode.HTML)
    await message.answer(text=msg.text_2, reply_markup=MenuKeyboard, parse_mode=ParseMode.HTML)


@router.message(lambda message: message.text == "🚀 Maxsus linkni olish")
async def get_link_handler(message: types.Message):
    user_id = message.from_user.id
    user = db.get_user(user_id)
    referrals_count = db.get_users_count_by_referrer(user_id)
    referrer_id: int = user.get("referrer_id")
    referrer_text: str = ""
    username_text: str = ""

    if referrer_id == 0:
        referrer_text = "👑 Do'stingiz: Hech kim ⭕️\n"
    else:
        referrer = await message.bot.get_chat(referrer_id)
        referrer_text = f"👑 Do'stingiz: <a href='tg://user?id={
            str(referrer_id)}'>{referrer.full_name}</a>\n"

    if message.from_user.username:
        username_text = "🔗 Foydalanuvchi nomi: @" + \
            str(message.from_user.username) + "\n"

    button_text = "🔒 Shaxsiy kanal linkini olish" if referrals_count < config.tg_bot.REQUIRED_REFERRAL_COUNT else "🔐 Shaxsiy kanal linkini olish"
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text=button_text,
                    callback_data="$link-request"
                )
            ]
        ])

    await message.answer(
        "🆔 ID raqam: " + str(user_id) + "\n" +
        "👤 Foydalanuvchi: <a href='tg://user?id=" + str(user_id) + "'>" + message.from_user.full_name + "</a>\n" +
        username_text +
        referrer_text +
        "👥 Takliflaringiz soni: " + str(referrals_count) + " ta",
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard
    )


@router.callback_query(lambda query: query.data == "$link-request")
async def get_private_link(query: types.CallbackQuery):
    channel_link = config.tg_bot.SPECIAL_CHANNEL_URL
    user_id = query.from_user.id
    user = db.get_user(user_id)
    is_completed = user.get("is_completed")
    referrals_count = db.get_users_count_by_referrer(user_id)
    if referrals_count < config.tg_bot.REQUIRED_REFERRAL_COUNT:
        await query.answer(f"Linkni olish uchun siz yana {config.tg_bot.REQUIRED_REFERRAL_COUNT-referrals_count} ta odam taklif qilishingiz kerak!", show_alert=True)
        return

    db.update_user_completed(user_id)

    await query.message.answer(f"🎁 Kanal linki: {channel_link}\n\n😊 Darslar manfaatli bo'lsin!", disable_web_page_preview=True)
    if is_completed:
        return

    referrer_id: int = user.get("referrer_id")
    username_text: str = ""
    referrer_text: str = ""

    if referrer_id == 0:
        referrer_text = "👑 Do'sti: Hech kim ⭕️\n"
    else:
        referrer = await query.bot.get_chat(referrer_id)
        referrer_text = f"👑 Do'sti: <a href='tg://user?id={
            str(referrer_id)}'>{referrer.full_name}</a>\n"

    if query.from_user.username:
        username_text = "🔗 Foydalanuvchi nomi: @" + \
            str(query.from_user.username) + "\n"

    admins = config.tg_bot.ADMINS.split(",")

    for admin in admins:
        await query.bot.send_message(
            chat_id=admin,
            text="🎉 Foydalanuvchi shartlarni muvaffaqiyatli bajardi! 🎉\n\n" +
            "🆔 ID raqam: " + str(user_id) + "\n" +
            "👤 Foydalanuvchi: <a href='tg://user?id=" + str(user_id) + "'>" + query.from_user.full_name + "</a>\n" +
            username_text +
            referrer_text +
            "👥 Takliflar soni: " + str(referrals_count) + " ta",
        )


@router.callback_query(lambda query: query.data == "verify_subscription")
async def verify_subscription(query: types.CallbackQuery, state: FSMContext):
    user_id = query.from_user.id
    bot = query.bot
    unsubscribed_channels = []

    # Recheck subscriptions for each channel
    for channel in REQUIRED_CHANNELS:
        try:
            chat_member = await bot.get_chat_member(chat_id=f"{channel}", user_id=user_id)
            if chat_member.status not in ("member", "administrator", "creator"):
                unsubscribed_channels.append(channel)
        except TelegramBadRequest:
            # Ignore inaccessible channels
            continue

    # If the user is still not subscribed to all channels, update the keyboard
    if unsubscribed_channels:
        updated_keyboard = InlineKeyboardMarkup(inline_keyboard=[])
        i = 1
        for channel in unsubscribed_channels:
            chat = await query.bot.get_chat(chat_id=f"{channel}")
            link = chat.invite_link
            updated_keyboard.inline_keyboard.append(
                [
                    InlineKeyboardButton(
                        text=f"📢 {i}-kanalga obuna bo'lish",
                        url=link
                    )
                ]
            )
            i += 1

        updated_keyboard.inline_keyboard.append(
            [
                InlineKeyboardButton(
                    text="✅ Obunani Tasdiqlash",
                    callback_data="verify_subscription"
                )
            ]
        )
        await query.message.delete()
        await query.message.answer(
            text="Botdan foydalanish uchun quyidagi kanallarga obuna bo'lishingiz kerak. 👇",
            reply_markup=updated_keyboard,
            parse_mode="HTML"
        )
        return

    data = await state.get_data()
    referrer_id = data.get("referrer_id")
    user = db.get_user(user_id)
    if not user:
        referrer = None
        if referrer_id and referrer_id != str(user_id):
            referrer = db.get_user(referrer_id)
        try:
            db.create_user(
                user_id,
                query.from_user.full_name,
                query.from_user.username,
                referrer_id if referrer else 0,
            )
            if referrer:
                try:
                    referrals_count = db.get_users_count_by_referrer(
                        referrer_id)
                    await query.bot.send_message(
                        chat_id=referrer_id,
                        text=f"<a href='tg://user?id={user_id}'>{query.from_user.full_name}</a> sizning taklif havolangiz orqali ro'yxatdan o'tdi. \nSizda jami {
                            referrals_count} ta takliflaringiz bo'ldi.",
                        parse_mode=ParseMode.HTML
                    )
                except:
                    pass
        except Exception as e:
            await query.bot.send_message(config.tg_bot.DEVID, "Error creating user in bot: "+config.tg_bot.BOT_URL+"\n\n"+str(e))

    try:
        await query.message.delete()
    except:
        pass
    await state.clear()
    await query.message.answer(
        text="✅ Obunangiz tasdiqlandi! Endi botdan foydalanishingiz mumkin.",
        reply_markup=MenuKeyboard,
        parse_mode="HTML",
    )
