﻿"""
имеем проект развития образовательной платформы GAZ Campus - многоформатной площадки образования клиентов с лекциями, МК и встречами с экспертами

создадим чат-бот в Телеграм для отправки напоминаний клиентам и приглашений к участию

импортируем библиотеку c помощью функции import и подключаем Телеграм-бот на python 

программируем чат-бот на отправку конкретного текста (приглашения), задаем время отправки через alert

напишем обработчик входящих сообщений через команды help и schedule (1 отвечает за краткую информацию о платформе, 2 высылает расписание мероприятий)
"""

import telebot
import gzcamp_bot
from telebot import types
import datetime

# TOKEN = gzcamp_bot.1883015533:AAGn0-6zRCyq9tJV0gCJ6kyj5-0l85dyT7c
bot = telebot.TeleBot('1883015533:AAGn0-6zRCyq9tJV0gCJ6kyj5-0l85dyT7c')
@bot.message_handler(content_types=['start'])
def start(message):
	bot.send_message(message.from_user.id, 'Здравствуйте, {message.from_user.first_name}! Что Вас интересует?')
	#bot.register_next_step_handler(message, data)
def get_respond(message):
	bot.send_chat_action(message.from_user.id, 'typing')
	if message.text == "Здравствуйте":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		key1 = types.KeyboardButton('Online events')
		key2 = types.KeyboardButton('Offline events') 
		markup.add(key1, key2)

def name(m):
    if message.text == "Месяц":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = types.KeyboardButton('Июнь')
        key2 = types.KeyboardButton('Июль') 
        markup.add(key1, key2)
    elif message.text == "Формат":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key3 = types.KeyboardButton('Online')
        key4 = types.KeyboardButton('Offline') 
        markup.add(key3, key4)
    elif message.text == "Событие":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key5 = types.KeyboardButton('Как')
        key6 = types.KeyboardButton('Что') 
        markup.add(key5, key6)
   
@bot.message_handler(commands=['info'])
def send_welcome(message):
        name = bot.get_me()
        print(name)
        bot.reply_to(message, "Welcome")
        
with open('gazdata.txt','r') as f:
	lines = f.readlines()

class MyEvent(object):
    event_name = 'Как настроить логистику для вашего бизнеса'
    event_date = datetime.date(2021, 6, 5)
    
    def __init__(self, line):
        self.event_name = line.split(' ')[0]
        pass

events = []
for l in lines:
    #'Как настроить логистику для вашего бизнеса', '2021, 5, 27'
    events.append(MyEvent(l)) #['Как настроить логистику для вашего бизнеса', '27/05']
    
class MyUser(object):
    name = '@uzunishe'
    user_events = []
    
my_users = {'tg_name': MyUser}
for l in lines:
    pass

bot.polling(none_stop=True)
