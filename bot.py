# -*- coding: utf-8 -*-
import telebot
import config
import os
import SQL_bd

#   подключаем библиотеки
bot = telebot.TeleBot(config.token)



#   добавим пользовательскую клавиатуру
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('Мне грустно')

#   передаем клавиатуру пользователю
    bot.send_message(message.from_user.id, 'Доброго времени суток.', \
                     reply_markup=user_markup)





@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardMarkup()
    bot.send_message(message.from_user.id, 'Приходи еще', reply_markup=hide_markup)

@bot.message_handler(content_types=['photo'])
def handle_text(message):
    bot.send_message(message.chat.id, SQL_bd)





# пасхалки

@bot.message_handler(content_types=['text'])
def bla_pashal(message):
    if message.text == 'Мне грустно':
        directory = 'C:/Users/mssap/PycharmProjects/Kritik_bot/photo'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            img = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, img)
            img.close()
    else:
        bot.send_message(message.chat.id, SQL_bd)









if __name__ == '__main__':
    bot.polling(none_stop=True)