import os
import telebot
import asyncio

TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

print(bot)

# # Handle /hi and /greet
# @bot.message_handlers(commands=['hi', 'greet'])
# def send_welcome(msg):
#     bot.reply_to(message=msg, text="Namastey!")
#
# bot.infinity_polling()

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am Leetbot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    print(message)
    bot.reply_to(message, message.text)


asyncio.run(bot.polling())
