# -*- coding: utf-8 -*-
import telebot
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, Юрий Сергеевич')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Как Ваши дела?')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Удачного Вам дня')
    #else bot.send_message(message.chat.id, 'Я Вас не понимаю')


bot.polling(none_stop=True, interval=0)
