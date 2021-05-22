"""
имеем проект развития образовательной платформы GAZ Campus - многоформатной площадки образования клиентов с лекциями, МК и встречами с экспертами

создадим чат-бот в Телеграм для отправки напоминаний клиентам и приглашений к участию

импортируем библиотеку c помощью функции import и подключаем Телеграм-бот на python 

программируем чат-бот на отправку конкретного текста (приглашения), задаем время отправки через alert

напишем обработчик входящих сообщений через команды help и schedule (1 отвечает за краткую информацию о платформе, 2 высылает расписание мероприятий)
"""

import telebot

bot = telebot.TeleBot('1827099486:AAFnrUzG0chBM7MCIT2cBGgDo6CtMOa7zPQ')
@bot.message_handler(content_types=['text'])

def start(message):
	bot.send_message(message.from_user.id, 'Здравствуйте!')
	#bot.register_next_step_handler(message, data)

with open('gazdata.txt','r') as f:
	lines = f.readlines()
bot.polling()
