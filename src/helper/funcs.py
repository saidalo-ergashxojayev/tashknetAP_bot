from config import load_config
from src.helper.models import StartTextResult

config = load_config()


def create_start_text_text(short_link: str) -> StartTextResult:

    return StartTextResult(
        photo_id=config.tg_bot.PHOTO_ID,
        text_1="<b>🧨 10 kunlik writing marafonda ishtirok eting va listening balingizni 8.0+ ga oshiring!</b>\n\n" +
        "Listening eng qiyin savol turlari (multiple choice, matching features, map)\n" +
        "— Testlarni to'g'ri tahlil qilish\n" +
        "— Har kunlik jonli darslar + amaliy mashqlar;\n" +
        "— 10 kun ichida listeningdan eng kerakli bilimlarga ega boʻlasiz.\n\n" +
        
        "<b>👨‍🏫 Ustozlar:</b>\n" +
        "— G'anisher Otaboyev (Overall 8, Listening 8.5)\n" +
        "— G'ulomjon Yuldoshev (Overall 8.5, Listening 9.0)\n" +
        "— Fazliddin G’iyosov (Overall 9, Listening 9.0)\n" +
        "— Saidakhror Abdukodirov (Overall 8.5, Listening 9.0)\n\n" +
        
        "<b>🆓 Bularning barchasi — BEPUL!</b>\n" + 
        "Faqat doʻstlaringizni taklif qilsangiz kifoya!\n\n" +
        "👇 Hozir ro‘yxatdan o‘ting va marafon kanaliga qo‘shiling!\n" +
        short_link,

        text_2="<b>🤝Doʻstlaringizni marafonga taklif qiling!</b>\n\n" +
        "👆 Yuqoridagi xabarni doʻstlaringizga ulashing va ularga ham <b>bepul listening marafonda</b> qatnashish <b>imkoniyatini</b> bering.\n\n" +
        "👥 Siz esa <b>atiga 1 ta</b> ingliz tili o'qiydigan <b>doʻstingizni taklif</b> qiling va yopiq maxfiy kanalga qoʻshiling!"
    )
