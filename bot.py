# -*- coding: utf-8 -*-
import telebot
import config


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
    bot.send_message(message.chat.id, '''БЛА-бла''')

@bot.message_handler(content_types=['text'])
def go1_text(message):
    bot.send_message(message.chat.id, 'Я предпочитаю не тратить время на пустые разговоры, лучше покажи фотографию')





# фото: AgADAgADrqcxGykD8w0NTFX3_xiJz74QSw0ABNGIrvq1zRPvllUCAAEC
# пасхалки




if __name__ == '__main__':
    bot.polling(none_stop=True)