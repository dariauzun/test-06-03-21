"""
имеем проект развития образовательной платформы GAZ Campus - многоформатной площадки образования клиентов с лекциями, МК и встречами с экспертами

создадим чат-бот в Телеграм для отправки напоминаний клиентам и приглашений к участию

импортируем библиотеку c помощью функции import и подключаем Телеграм-бот на python 

программируем чат-бот на отправку конкретного текста (приглашения), задаем время отправки через alert

напишем обработчик входящих сообщений через команды help и schedule (1 отвечает за краткую информацию о платформе, 2 высылает расписание мероприятий)
"""

import telebot
import gzcamp_bot
import datetime

# TOKEN = gzcamp_bot.1883015533:AAGn0-6zRCyq9tJV0gCJ6kyj5-0l85dyT7c
bot = telebot.TeleBot('1883015533:AAGn0-6zRCyq9tJV0gCJ6kyj5-0l85dyT7c')
@bot.message_handler(content_types=['text'])

def start(message):
	bot.send_message(message.from_user.id, 'Здравствуйте!')
	#bot.register_next_step_handler(message, data)

with open('gazdata.txt','r') as f:
	lines = f.readlines()
    
class Event(object):
    event_name = 'Как настроить логистику для вашего бизнеса'
    event_date = datetime.date(2021, 5, 27)
    
    def  _init_(self, line):
        self.event_name - line.split('')[0]
        pass
        
events = []
for l in lines:
    #'Как настроить логистику для вашего бизнеса', '2021, 5, 27'
    events.append(Event()) #['Как настроить логистику для вашего бизнеса', '27/05']
    
class MyUser(object):
    name = ''
    user_events = []
    
my_users = {'uzunishe': MyUser}
for l in lines:
    pass
bot.polling()
