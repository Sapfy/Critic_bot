# -*- coding: utf-8 -*-
import telebot
import config
import random

bot = telebot.TeleBot(config.token)

#   сообщаем библиотеке, что при приеме данного сообщения,
#   должны выполняться определенные действия (декоратор)
@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, '''Для тех, кто желает начать,
    но нет подходящей музыки...''')

#   добавим пользовательскую клавиатуру
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('Прокрастинировать','Сидеть у окна','Бренно страдать ')
    user_markup.row('Гулять по кладбищу','Мыть посуду','Переходить на темную сторону')
#   передаем клавиатуру пользователю
    bot.send_message(message.from_user.id, 'Добро пожаловать туда, где знают, под какую музыку стоит начать...', \
                     reply_markup=user_markup)

@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardMarkup()
    bot.send_message(message.from_user.id, '..', reply_markup=hide_markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Прокрастинировать':
        audio = open("C:/Users/mssap/PycharmProjects/Guess_the_melody/music/Dark_Moor_-_Just_Rock.mp3", 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()

if __name__ == '__main__':
    bot.polling(none_stop=True)