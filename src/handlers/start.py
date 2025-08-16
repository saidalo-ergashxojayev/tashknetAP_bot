from aiogram import Router, F
from aiogram import types
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import CommandStart, CommandObject
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.utils.deep_linking import create_start_link
from config import load_config
from loader import db
from src.keyboards.default.menuKeyboard import MenuKeyboard
from src.helper.funcs import create_start_text_text
from config.logger import logger

config = load_config()
router: Router = Router()


@router.message(CommandStart())
async def bot_start(message: types.Message, command: CommandObject, state: FSMContext):
    user_id = message.from_user.id
    user = db.get_user(user_id)
    short_link: str

    if not user:
        short_link = await create_start_link(message.bot, payload=str(user_id))
        data = await state.get_data()
        referrer_id = data.get("referrer_id", None)
        if not referrer_id:
            referrer_id = command.args
        referrer = None
        if referrer_id and referrer_id != str(user_id):
            referrer = db.get_user(referrer_id)

        try:
            db.create_user(
                user_id,
                message.from_user.full_name,
                message.from_user.username,
                referrer_id if referrer else 0,
            )
            if referrer:
                try:
                    referrals_count = db.get_users_count_by_referrer(
                        referrer_id)
                    await message.bot.send_message(
                        chat_id=referrer_id,
                        text=f"<a href='tg://user?id={user_id}'>{message.from_user.full_name}</a> sizning taklif havolangiz orqali ro'yxatdan o'tdi. \nSizda jami {
                            referrals_count} ta takliflaringiz bo'ldi.",
                        parse_mode=ParseMode.HTML
                    )
                except:
                    pass
        except Exception as e:
            await message.bot.send_message(config.tg_bot.DEVID, "Error creating user in bot: "+config.tg_bot.BOT_URL+"\n\n"+str(e))

    else:
        short_link = config.tg_bot.BOT_URL + "?start=" + str(user_id)

    msg = create_start_text_text(short_link)
    media_group_builder = MediaGroupBuilder(caption=msg.text_1)
    for photo_id in msg.photo_ids:
        media_group_builder.add_photo(photo_id)
    media_group = media_group_builder.build()
    await message.answer_media_group(media=media_group)
    await message.answer(text=msg.text_2, reply_markup=MenuKeyboard, parse_mode=ParseMode.HTML)


@router.message(F.content_type == types.ContentType.PHOTO)
async def handle_photo(message: types.Message):
    logger.log(20, f"Photo ID: {message.photo[-1].file_id}")
