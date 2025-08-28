import telebot
from telebot import types
import os

# Bot Token (Render-এর Environment Variables থেকে নেওয়া হবে)
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# Start Command
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📊 Balance")
    btn2 = types.KeyboardButton("👥 Refer")
    btn3 = types.KeyboardButton("📝 Task Submit")
    btn4 = types.KeyboardButton("💸 Withdraw")
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    
    bot.send_message(
        message.chat.id,
        "👋 Welcome!\n\nChoose an option below:",
        reply_markup=markup
    )

# Handle Menu Buttons
@bot.message_handler(func=lambda message: True)
def handle_menu(message):
    if message.text == "📊 Balance":
        bot.send_message(message.chat.id, "💰 Your current balance is: 0$")
    elif message.text == "👥 Refer":
        bot.send_message(message.chat.id, "🔗 Your referral link: https://t.me/YourBotUsername?start=ref123")
    elif message.text == "📝 Task Submit":
        bot.send_message(message.chat.id, "✅ Please submit your task details here...")
    elif message.text == "💸 Withdraw":
        bot.send_message(message.chat.id, "🏦 Enter the amount you want to withdraw...")
    else:
        bot.send_message(message.chat.id, "❌ Invalid option. Please use the menu buttons.")

print("Bot is running...")
bot.infinity_polling()
