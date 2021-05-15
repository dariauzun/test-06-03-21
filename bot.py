"""
имеем проект развития образовательной платформы GAZ Campus - многоформатной площадки образования клиентов с лекциями, МК и встречами с экспертами

создадим чат-бот в Телеграм для отправки напоминаний клиентам и приглашений к участию

импортируем библиотеку c помощью функции import и подключаем Телеграм-бот на python 

программируем чат-бот на отправку конкретного текста (приглашения), задаем время отправки черед alert

напишем обработчик входящих сообщений через команды help и schedule (1 отвечает за краткую информацию о платформе, 2 высылает расписание мероприятий)
"""
import telebot
bot = telebot.TeleBot('1827099486:AAFnrUzG0chBM7MCIT2cBGgDo6CtMOa7zPQ')
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Здравствуйте!")
msg.from_user.username
bot.polling()
with open file "name"
"a": F write line chat ID
bot.send_message(chatid, text)
with open 

