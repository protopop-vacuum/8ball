import config
import telebot
import slovar
import random
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Не можешь сделать выбор? Я точно знаю как будет лучше!')
    bot.send_message(message.chat.id, 'Просто напиши свой вопрос. Сообщение должно заканчиваться на знак "?"')


@bot.message_handler(content_types=['text'])
def send_text(message):
    answer = ''
    if '?' in message.text:
        num = random.randrange(1, 5)
        num1 = random.randrange(0, 5)
        if num == 1:
            answer = slovar.good[num1]
        elif num == 2:
            answer = slovar.semi_good[num1]
        elif num == 3:
            answer = slovar.neutral[num1]
        elif num == 4:
            answer = slovar.bad[num1]
        bot.send_message(message.chat.id, answer)
        bot.send_message(message.chat.id, 'Следующий вопрос!')
    else:
        bot.send_message(message.chat.id, 'Вопрос должен заканчиваться на знак "?"')


@bot.message_handler(content_types=['photo', 'sticker', 'audio', 'video', 'document'])
def send_text(message):
    bot.send_message(message.chat.id, 'Я, пока что, умею работать только с текстом.')


bot.infinity_polling()
