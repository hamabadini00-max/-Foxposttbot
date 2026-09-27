import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler,
    MessageHandler, filters, ContextTypes
)

BOT_TOKEN = os.environ.get("8845256483:AAFupbunk0Dhgmu-jSpaVevvEMDd9rYxzqo
")

users = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username or "بی_ناڤ"
    
    if user_id not in users:
        users[user_id] = {"username": username, "registered": True}
        await update.message.reply_text(
            f"✅ بەخێربێی {username}!\n"
            f"تۆ ب سەرکەفتیانە تومار بووی."
        )
    else:
        await update.message.reply_text("تۆ بەری نوکە تومار بوویی.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"من ئەڤە وەرگرت: {text}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("بۆت دەستپێدکەت...")
    app.run_polling()

if __name__ == "__main__":
    main()
