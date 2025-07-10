from config import load_config
from src.helper.models import StartTextResult

config = load_config()


def create_start_text_text(short_link: str) -> StartTextResult:

    return StartTextResult(
        photo_id=config.tg_bot.PHOTO_ID,

        text_1="<b>🧨 8 kunlik writing marafonda ishtirok eting va writing balingizni 7+ ga oshiring!</b>\n\n" +
        "4 nafar IELTS eksperti bilan intensiv BEPUL marafonda ishtirok eting!\n\n" +
        "🗓 Marafonda nimalar oʻrgatiladi?\n" +
        "— Task 1 ning barcha grafik turlari (maps, pie, table, process, periodicals);\n" +
        "— Task 2 essay yozish boʻyicha strukturalar\n" +
        "— Har kunlik jonli darslar + amaliy mashqlar;\n" +
        "— 8 kun ichida writingdan eng kerakli bilimlarga ega boʻlasiz.\n\n" +
        "<b>👨‍🏫 Ustozlar:</b>\n" +
        "— Laziz Atabayev (Writing 9.0)\n" +
        "— Fazliddin G‘iyosov (W 8.5)\n" +
        "— Nurulloh Kamalkhujaev (W 8.0)\n" +
        "— Saidakhror Abdukodirov (W 7.5)\n\n" +
        "<b>🆓 Bularning barchasi — BEPUL!</b>\n" + 
        "Faqat doʻstlaringizni taklif qilsangiz kifoya!\n\n" +
        "👇 Hozir ro‘yxatdan o‘ting va marafon kanaliga qo‘shiling!\n" +
        short_link,

        text_2="<b>🤝Doʻstlaringizni marafonga taklif qiling!</b>\n\n" +
        "👆 Yuqoridagi xabarni doʻstlaringizga ulashing va ularga ham <b>bepul writing marafonda</b> qatnashish <b>imkoniyatini</b> bering." +
        "👥 Siz esa <b>atiga 1 ta</b> ingliz tili o'qiydigan <b>doʻstingizni taklif</b> qiling va yopiq maxfiy kanalga qoʻshiling!"
    )
