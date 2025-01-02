from config import load_config
from src.helper.models import StartTextResult

config = load_config()


def create_start_text_text(short_link: str) -> StartTextResult:

    return StartTextResult(
        photo_id="AgACAgIAAxkBAAMEZ3FcD5SwfoevjKP5oEhtqfSGC04AAsPoMRtFzIlL6_DNcKK98i0BAAMCAAN5AAM2BA",

        text_1="Bugundan yangi telegram kanalimda <u><b>self-study qilamiz!</b></u> \n\n" +
        "✅ Va'da beraman siz bu challenge da qatnashib <b>LISTENING band scoreingizni kamida 1.0 ball ga oshirasiz.</b>\n\n" +
        "‼️ <b>Shu bepul challengimni ichidagi materiallarni ishlash <u>listening dan 8.0 olishimga sababchi bo'lgan </u> desamham bo'ladi… </b>" +
        "<b>🚀 LISTENING-im 5.5 da </b> qotib qoldi deyavermasdan, hozirdan practice qilishni boshlang va <b> 30 kundan keyin natijangiz gapirsin!</b>\n\n" +
        "Pastdagi havola orqali ro'yxatdan o'ting va challengeda bepul qatnashing 👇🏻\n\n" +
        short_link,

        text_2="👋 <b>Do'stlaringizni</b> bu <b>loyiha</b> haqida xabardor qiling!\n\n" +
        "👆👆👆 Yuqoridagi <b>xabarni do'stlaringizga</b> yuboring va ularga bepul kurs da qatnashish imkoniyatini taqdim eting.\n\n" +
        "<b>- Siz esa 5 ta do'stingizni</b> taklif qilib maxfiy kanalga kirishingiz mumkin! 🚀",
    )