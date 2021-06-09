"""
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
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.from_user.id, 'Здравствуйте! Напишите Кампус')
	#bot.register_next_step_handler(message, data)
   
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Кампус":
        main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton('Формат')
        but2 = types.KeyboardButton('Месяц')
        but3 = types.KeyboardButton('Конкретное событие')
        but4 = types.KeyboardButton('Тип мероприятия')
        main_markup.add(but1, but2, but3, but4)
        bot.send_message(message.chat.id, "Что Вас интересует?", reply_markup = main_markup)
        bot.register_next_step_handler(message, name)
    else: 
        bot.send_message(message.chat.id, "Я Вас не понимаю. Напишите /start.")

def name(message):
    if message.text == 'Формат':
        main_markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        form1 = types.KeyboardButton('Online')
        form2 = types.KeyboardButton('Offline') 
        main_markup1.add(form1, form2)
        bot.send_message(message.chat.id, "Выберите подходящий формат", reply_markup = main_markup1)
        bot.register_next_step_handler(message, form)
    elif message.text == 'Месяц':
        main_markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        month1 = types.KeyboardButton('Май')
        month2 = types.KeyboardButton('Июнь')
        month3 = types.KeyboardButton('Июль')
        main_markup2.add(month1, month2, month3)
        bot.send_message(message.chat.id, "Какой месяц Вас интересует?", reply_markup = main_markup2)
        bot.register_next_step_handler(message, month)
    elif message.text == 'Конкретное событие':
        main_markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        ev1 = types.KeyboardButton('Пять обязательных шагов для логистики при развитии e-commerce')
        ev2 = types.KeyboardButton('Системный подход к управлению опытом кандидата и сотрудника')
        ev3 = types.KeyboardButton('Как организовать бизнес в сфере ритейла')
        ev4 = types.KeyboardButton('Новейшие инструменты продвижения в соцсетях')
        main_markup3.add(ev1, ev2, ev3, ev4)
        bot.send_message(message.chat.id, "Какое событие Вас интересует?", reply_markup = main_markup3)
        bot.register_next_step_handler(message, ev)
    
    elif message.text == 'Тип мероприятия':
        main_markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        typ1 = types.KeyboardButton('Мастермайнд')
        typ2 = types.KeyboardButton('Разговор с экспертом')
        
        main_markup4.add(typ1, typ2)
        bot.send_message(message.chat.id, "Какой формат Вам интересен?", reply_markup = main_markup4)
        bot.register_next_step_handler(message, typ)
    else: 
        bot.send_message(message.chat.id, "Я Вас не понимаю. Напишите /start.")
        
def form(message):
    if message.text == 'Online':
        main_markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        fo1 = types.KeyboardButton('05/06')
        fo2 = types.KeyboardButton('09/06') 
        main_markup5.add(fo1, fo2)
        bot.send_message(message.chat.id, "Выберите событие", reply_markup = main_markup5)
        bot.register_next_step_handler(message, fo)

    elif message.text == 'Offline':
        main_markup6 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        orm1 = types.KeyboardButton('Мастермайнд')
        orm2 = types.KeyboardButton('Разговор с экспертом') 
        main_markup6.add(orm1, orm2)
        bot.send_message(message.chat.id, "Выберите событие", reply_markup = main_markup6)
        bot.register_next_step_handler(message, orm)
    else: 
        bot.send_message(message.chat.id, "Я Вас не понимаю. Напишите /start.")
        
def month(message):
    if message.text == 'Июнь':
        main_markup7 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mo1 = types.KeyboardButton('05/06')
        mo2 = types.KeyboardButton('09/06') 
        main_markup7.add(mo1, mo2)
        bot.send_message(message.chat.id, "Выберите число", reply_markup = main_markup7)
    elif message.text == 'Июль':
        main_markup8 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        nth1 = types.KeyboardButton('01/07')
        nth2 = types.KeyboardButton('05/07') 
        main_markup8.add(orm1, orm2)
        bot.send_message(message.chat.id, "Выберите число", reply_markup = main_markup8)
    else: 
        bot.send_message(message.chat.id, "Я Вас не понимаю. Напишите /start.")
        

  
def fo(message):
    if message.text == '05/06':
        bot.send_message(message.chat.id, "Пять обязательных шагов для логистики при развитии e-commerce, 05/06/2021, 16:00, платформа Webinar")
    elif message.text == '09/06':
        bot.send_message(message.chat.id, "Системный подход к управлению опытом кандидата и сотрудника, 09/06/2021, 16:00, платформа Webinar")

def orm(message):
    if message.text == 'Мастермайнд':
        bot.send_message(message.chat.id, "10/06/2021, 16:00, шоу-рум ГАЗ на Белорусской")
    elif message.text == 'Разговор с экспертом':
        bot.send_message(message.chat.id, "11/06/2021б 16:00б шоу-рум ГАЗ на Белорусской")
        
def ev(message):
    if message.text == 'Пять обязательных шагов для логистики при развитии e-commerce':
        bot.send_message(message.chat.id, "05/06/2021, 16:00, платформа Webinar")
    elif message.text == 'Июль':
        bot.send_message(message.chat.id, "09/06/2021, 16:00, платформа Webinar")
        
def typ(message):
    if message.text == 'Мастермайнд':
        bot.send_message(message.chat.id, "10/06/2021, 16:00, шоу-рум ГАЗ на Белорусской")
    elif message.text == 'Разговор с экспертом':
        bot.send_message(message.chat.id, "11/06/2021б 16:00б шоу-рум ГАЗ на Белорусской")
bot.polling(none_stop=True)
#bot.polling(none_stop=True)
#@bot.message_handler(commands=['info'])