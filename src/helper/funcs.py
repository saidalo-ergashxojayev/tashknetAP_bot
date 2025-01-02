from config import load_config
from src.helper.models import StartTextResult

config = load_config()


def create_start_text_text(short_link: str) -> StartTextResult:

    return StartTextResult(
        photo_id="AgACAgIAAxkBAAMEZ3aSHeq5uxw_50q2oVab1u7CbeQAAl7nMRvMHLFLnDZ68cwn7D4BAAMCAAN5AAM2BA",

        text_1="Assalomu alaykum!\n\n" +
        "<b>LISTENING 8.5 EGASI TOMONIDAN TEKIN KURS</b>\n\n" +
        "⚠️ Aynan bugun siz mana shu <b>asl narxi 200,000 so'm</b>lik <b>LISTENING MARATHON 1.0</b> ni <b>TEKINGA</b> olishingiz mumkin.\n\n" +
        "🎧 Sizga taqdim etiladigan materiallar:\n" +
        "1. 15 full tests = 600 questions ✅\n" +
        "<b>2. 15 VIDEO EXPLANATIONS ✅</b>\n" +
        "3. 30 podcasts  ✅\n\n" +
        "Bu kursning boshqa kurslardan farqi sizga har <b>bir savolni javobi ipidan ignasigacha videoda tushuntiriladi.</b>\n\n" +
        "Listening Marathon sizgha natijangizni <b>1 balldan 3 ballgacha</b> ko'tarish imkoniyatini beradi. 🚀\n\n" +
        "Pastdagi havola orqali ro'yxatdan o'ting va marafonda bepul qatnashing 👇🏻" +
        short_link,

        text_2="👋 <b>Do'stlaringizni</b> bu <b>loyiha</b> haqida xabardor qiling!\n\n" +
        "👆👆👆 Yuqoridagi <b>xabarni do'stlaringizga</b> yuboring va ularga bepul kurs da qatnashish imkoniyatini taqdim eting.\n\n" +
        "<b>- Siz esa 5 ta do'stingizni</b> taklif qilib maxfiy kanalga kirishingiz mumkin! 🚀",
    )
