# -*- coding: utf-8 -*-
import telebot
import config

bot = telebot.TeleBot(config.token)


Слышь

if __name__ == '__main__':
    bot.polling(none_stop=True)

