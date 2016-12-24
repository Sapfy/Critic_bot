# -*- coding: utf-8 -*-
import telebot
import config
import os
import sqlite3 as lite
import time

#   подключаем библиотеки
bot = telebot.TeleBot(config.token)

#   добавим пользовательскую клавиатуру
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Мне грустно')

#   передаем клавиатуру пользователю
    bot.send_message(message.from_user.id, 'Доброго времени суток.', \
                     reply_markup=user_markup)

@bot.message_handler(commands=['help'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardMarkup()
    bot.send_message(message.from_user.id, 'Я профессиональный критик. Если ты хочешь, чтобы тебе честно дали оценку '
                                           'фотографии или аудиозаписи - присылай, я все скажу.')

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    #   вставляем задержку для аудио
    time.sleep(3)
    conn = lite.connect('BD.db')

    c = conn.cursor()

    c.execute('''SELECT bla2 FROM tell
                  ORDER BY RANDOM()
                  LIMIT 1''')

    data = c.fetchone()
    bot.send_message(message.chat.id, "%s" % data)

    #   Закрываем текущее соединение с БД
    conn.close()

@bot.message_handler(content_types=['audio'])
def handle_photo(message):
    #   вставляем задержку для аудио
    time.sleep(3)
    conn = lite.connect('BD.db')

    c = conn.cursor()

    c.execute('''SELECT bla1 FROM tell
                  ORDER BY RANDOM()
                  LIMIT 1''')

    data = c.fetchone()
    bot.send_message(message.chat.id, "%s" % data)

    #   Закрываем текущее соединение с БД
    conn.close()



# пасхалки

@bot.message_handler(content_types=['text'])
def bla_pashal(message):
    if message.text == 'Мне грустно':
        directory = 'C:/Users/mssap/PycharmProjects/Kritik_bot/photo' # os.path.dirname()
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            img = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, img)
            img.close()
    else:
        conn = lite.connect('BD.db')

        c = conn.cursor()

        c.execute('''SELECT bla3 FROM tell
                         ORDER BY RANDOM()
                         LIMIT 1''')

        data = c.fetchone()
        bot.send_message(message.chat.id, "%s" % data)

        #   Закрываем текущее соединение с БД
        conn.close()


if __name__ == '__main__':
    bot.polling(none_stop=True)