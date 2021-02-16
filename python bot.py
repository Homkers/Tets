import telebot
bot = telebot.TeleBot('1658937169:AAFTk2lFb8emYoRvqTcpAmCUePMg22S_bzo')
@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)
bot.polling(none_stop=True, interval=0)