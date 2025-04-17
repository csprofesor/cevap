from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7214368466:AAEWeHtixBlXe_5wK6I2BAX8WF1axSTmIhY"

# Anahtar kelimeler
ANAHTAR_KELIMELER = ["cs", "kekik", "depo", "repo", "yardım", "eklenti"]

# Cevap metni
CEVAP_METNI = """kekikdevam
Latte
makoto
nikstream
nikyokki
güncel bilinen liste. başka bildiğiniz varsa içine ekleyebiliriz."""

# /start komutu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Merhaba Dünyalı Cs Gruba Hoşgeldin.")

# Mesaj işleme
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mesaj = update.message.text.lower()
    print("Mesaj geldi:", mesaj)

    if any(kelime in mesaj for kelime in ANAHTAR_KELIMELER):
        await update.message.reply_text(CEVAP_METNI)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))  # Hem özel hem grup mesajlarını dinler

    print("Bot çalışıyor...")
    app.run_polling()
