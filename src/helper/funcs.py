from config import load_config
from src.helper.models import StartTextResult

config = load_config()


def create_start_text_text(short_link: str) -> StartTextResult:

    return StartTextResult(
        photo_id=config.tg_bot.PHOTO_ID,
        text_1="""
<b>🚀8 kunlik INTENSIVE SPEAKING MARAFON da qatnashing va gapirish qolbiliyatingizni oshiring</b>

<b>IELTS</b> hamda <b>MULTILEVEL</b> ustozlaridan darslar!

⚡️ Bu 8 kun davomida siz

— IELTS Speaking barcha partlari 
— Pronunciation 
— Fluency
— Vocabulary
— Grammar
— Public speechinggiz

<b>ni keyingi levelga olib chiqa olasiz</b>

<b>🧑‍🏫👩🏻‍🏫 Instructorlar:</b>

— Jumaboyev Begzod (S 9.0)
— Urolova Ruxshona ( S 9.0)
— Kasimova Asal (S 8.5)
— Olimov Saydullo (S 8.0)

<b>🆓 Bularning barchasi — BEPUL!</b>

Ro’yxatdan o’ting va yopiq kanal linkiga ega bo’ling:
""" +
        short_link,

        text_2="""
<b>🤝Doʻstlaringizni marafonga taklif qiling!</b>

👆 Yuqoridagi xabarni doʻstlaringizga ulashing va ularga ham <b>bepul speaking marafonda</b> qatnashish <b>imkoniyatini</b> bering.

👥 Siz esa <b>atiga 1 ta</b> ingliz tili o'qiydigan <b>doʻstingizni taklif</b> qiling va yopiq maxfiy kanalga qoʻshiling!
"""
    )
