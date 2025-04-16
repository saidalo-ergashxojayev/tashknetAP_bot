from config import load_config
from src.helper.models import StartTextResult

config = load_config()


def create_start_text_text(short_link: str) -> StartTextResult:

    return StartTextResult(
        photo_id=config.tg_bot.PHOTO_ID,

        text_1="Assalomu alaykum!\n\n" +
        "<b>READING 9.0 egalari tomonidan READING BOOSTER 1.0!!!</b>\n\n" +
        "⚠️ Agarda sizning ham Reading balingiz <b>5.0-6.0</b> da qotib qolgan bo'lsa, bu kurs aynan siz uchun. <b>Reading Expertlar</b> bilan balingizni <b>7.0+</b> gacha olib chiqing.\n\n" +
        "🔖 Kursning afzalliklari:\n" +
        "- <b>Savol turlari</b> uchun maxsus 11 ta dars ✅\n" +
        "- <b>Practice</b> uchun qo'shimcha 9 ta dars ✅\n" +
        "- 4 ta ustozdan <b>'pichoqqa sop bo'ladigan'</b> maslahatlar ✅\n" +
        "- Samarali texnikalar ✅\n\n" +
        "Barchasi mutlaqo <b>TEKINGA!</b>\n\n" +
        "Bu kursning boshqa kurslardan farqi sizga faqat test emas, barcha Reading 9.0 uchun ko'nikmalar ipidan ignasigacha tushuntiriladi. 🚀\n\n" +
        "Pastdagi havola orqali ro'yxatdan o'ting va marafonda bepul qatnashing 👇🏻" +
        short_link,

        text_2="👋 <b>Do'stlaringizni</b> bu <b>loyiha</b> haqida xabardor qiling!\n\n" +
        "👆👆👆 Yuqoridagi <b>xabarni do'stlaringizga</b> yuboring va ularga bepul kurs da qatnashish imkoniyatini taqdim eting.\n\n" +
        "<b>- Siz esa 7 ta do'stingizni</b> taklif qilib maxfiy kanalga kirishingiz mumkin! 🚀",
    )
