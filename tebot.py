import telebot
{}

from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ro' 

owm = OWM('f8328971db2ccbe474c7fb2c7246465d',config_dict )
mgr = owm.weather_manager()
bot = telebot.TeleBot("1722438173:AAGzJu59cV8h5gos3Vs3YsbOJTmvq1g5iPs")

@bot.message_handler(content_types=['text'])
def echo_all(message):
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	temp=w.temperature('celsius')['temp']

	answer = 'In  :  ' + message.text + '  acum: ' + w.detailed_status + '\n'
	answer += 'Temperatura este in jur de : ' + str(temp) + '\n\n'
	if temp<10:
		answer += 'Ii frig tare  imbracate bine :D'
	elif temp<20:
		answer += 'Ii reacoare imbracate'
	else:
		answer += 'Afara e cald'

	bot.send_message(message.chat.id, answer )
bot.polling(none_stop = True)
