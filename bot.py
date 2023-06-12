# import telebot
# from config import token  # из файла config.py забираем нашу переменную с токеном
#
#
# # Создаем экземпляр бота
# bot = telebot.TeleBot('6202036046:AAEanyj-Exob2AGLFtFdRrd78HF2mFDqYPM')
#
#
# # Функция, обрабатывающая команду /start
# @bot.message_handler(commands=["start"])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет! Напиши мне что-нибудь )')

# # Получение сообщений от юзера
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
#
# # Запускаем бота
# bot.polling(none_stop=True, interval=0)
#
# # # Функция, обрабатывающая команду /start
# # @bot.message_handler(commands=["start"])
# # def start(message):
# #     bot.send_message(message.chat.id, 'Привет! Напиши  )')
# #
# #
# # @bot.message_handler(commands=["task_1"])  # /task_1
# # def task_1(message):
# #     bot.send_message(message.chat.id, 'Задание 1, случайное число: ' + str(random.randint(1, 10)))
# #
# # # Получение сообщений от юзера
# # @bot.message_handler(content_types=["text"])
# # def handle_text(message):
# #     bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
#
# # Запускаем бота
# bot.polling(none_stop=True, interval=0)
#
#
# # Создаем экземпляр бота
# bot = telebot.TeleBot(token)


# import telebot
# import time
# # Токен, который выдает @botfather
# bot = telebot.TeleBot('6202036046:AAEanyj-Exob2AGLFtFdRrd78HF2mFDqYPM')
# # Адрес телеграм-канала, начинается с @
# CHANNEL_NAME = '@Hana_anna_bot'
# # Загружаем список шуток
# f = open('1.txt', 'r', encoding='UTF-8')
# jokes = f.read().split('\n')
# f.close()
# # Пока не закончатся шутки, посылаем их в канал
# for joke in jokes:
#     bot.send_message(CHANNEL_NAME, joke)
#     # Делаем паузу в один час
#     time.sleep(3600)
# bot.send_message(CHANNEL_NAME, "Анекдоты закончились :-(")

import telebot
from config import token  # из файла config.py забираем нашу переменную с токеном


# Создаем экземпляр бота
bot = telebot.TeleBot('6127790797:AAEryyGpirx7UysGFc-moT3yGgsbPLe_eMw')


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Напиши мне что-нибудь )')

import random
import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()




