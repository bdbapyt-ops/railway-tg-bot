import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = os.getenv("BOT_TOKEN")  # Railway Variables থেকে টোকেন আসবে

async def start(update, context):
    await update.message.reply_text("হাই! আমি Railway-এ ডিপ্লয় করা টেলিগ্রাম বট 🤖")

async def echo(update, context):
    await update.message.reply_text(update.message.text)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
