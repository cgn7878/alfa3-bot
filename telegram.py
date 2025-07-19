from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from config import TELEGRAM_TOKEN, TELEGRAM_USER_ID
from core import handle_signal_request, handle_manual_command
from log import log_message


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if str(update.effective_user.id) != str(TELEGRAM_USER_ID):
        await update.message.reply_text("Yetkisiz erişim.")
        return

    await update.message.reply_text("🤖 Alfa 3 aktif. Komut bekleniyor...")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)

    if user_id != str(TELEGRAM_USER_ID):
        await update.message.reply_text("Bu bota erişiminiz yok.")
        return

    text = update.message.text.strip().lower()
    log_message(f"Kullanıcıdan gelen mesaj: {text}")

    if text.startswith("sinyal") or text.startswith("al") or text.startswith("sat"):
        cevap = await handle_signal_request(text)
    else:
        cevap = await handle_manual_command(text)

    await update.message.reply_text(cevap)


def run_bot():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    log_message("Telegram bot başlatılıyor...")
    app.run_polling()
