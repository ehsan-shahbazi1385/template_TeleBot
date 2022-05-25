import telebot
#include liberary

api_token = ""
bot = telebot.TeleBot(api_token)
#bot

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "text")
#Command

@bot.message_handler(commands=['send'])
def send(message):
    bot.send_message(chat_id, 'text')
#send message function

@bot.message_handler(func=lambda m: True)
def echo_bot(message):
	bot.reply_to(message, message.text)
#echo bot

@bot.message_handler(func=lambda message: True)
def font(message):
    texts = message.text.split()
    if texts[0] == "/reply":
        text = texts[1]
        bot.reply_to(message, text)
#To receive from the user

bot.infinity_polling()
