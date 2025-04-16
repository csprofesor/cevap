from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7214368466:AAEWeHtixBlXe_5wK6I2BAX8WF1axSTmIhY"  # Bot tokenı

# Anahtar kelimeler listesi
ANAHTAR_KELIMELER = ["cs", "kekik", "depo", "repo", "yardım", "eklenti"]

# Verilecek sabit cevap
CEVAP_METNI = """kekikdevam
Latte
makoto
nikstream
nikyokki
güncel bilinen liste. başka bildiğiniz varsa içine ekleyebiliriz."""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Merhaba! Anahtar kelime yazarsan sana yardımcı olabilirim.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mesaj = update.message.text.lower()

    if any(kelime in mesaj for kelime in ANAHTAR_KELIMELER):
        await update.message.reply_text(CEVAP_METNI)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot çalışıyor...")
    app.run_polling()
