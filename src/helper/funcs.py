from config import load_config
from src.helper.models import StartTextResult

config = load_config()


def create_start_text_text(short_link: str) -> StartTextResult:
    photos = config.tg_bot.PHOTO_ID.split(",")

    return StartTextResult(
        photo_ids=photos,
        text_1="""
🚀 Maxsus <b>INSPERA 1.0</b>  kursimizda o'qib <b>READING&LISTENING</b> va qismidan <b>7.0-8.0+</b> olish imkoniyatiga ega bo'ling!

<b>10-kun davomida sizga nimalar taqdim etamiz?!</b>

— Naq 10 ta <b>JONLI DARSLAR</b>
— <b>10+10</b> IMTIXONDA tushgan materiallar
— Maxsus saralangan <b>Article(Maqolalar) va Podcastlar</b>
— Eng <b>ACTIVE</b> studenlarga maxsus <b>BEPUL SPEAKING</b> va <b>WRITING  MOCK</b>

👨‍🏫 <b>INSTRUCTORS</b>: 
<a href="https://t.me/teachernazim">TEACHER NAZIM (Mr.Nozimjon)</a>: <b>READING 9.0 x 2</b> 
<a href="https://t.me/diyorbek_8_5">Mr.Diyorbek</a>: LISTENING 9.0

🆓 Bularni hammasi <b>MUTLAQO BEPUL</b>

🔗 Joyingizni hoziroq band qilish uchun link:
""" +
        short_link,

        text_2="""
<b>🤝Doʻstlaringizni marafonga taklif qiling!</b>

👆 Yuqoridagi xabarni doʻstlaringizga ulashing va ularga ham <b>marafonimizda</b> qatnashish <b>imkoniyatini</b> bering.

👥 Siz esa <b>atiga 4 ta</b> ingliz tili o'qiydigan <b>do'stingizni taklif</b> qiling va yopiq maxfiy kanalga qoʻshiling!
"""
    )
