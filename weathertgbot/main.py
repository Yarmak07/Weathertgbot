import telebot
import requests
import json

bot = telebot.TeleBot('')
API = '76900910b7b785612863b2f862f7392a'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')





@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp}°')
    else:
        bot.reply_to(message, 'Город указан неверно!')

    
    #image = 'sun.png' if temp > 5.0 else 'unsun.png'
    #file = open('D:/Vs code/tg_bot/weathertgbot/' + image, 'rb')
    #bot.send_photo(message.chat.id, file)


bot.polling(none_stop = True)
