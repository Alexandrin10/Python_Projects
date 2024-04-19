from pyowm import OWM
from pyowm.utils.config import get_default_config
from colorama import init

init()


from colorama import Fore, Back, Style

config_dict = get_default_config()
config_dict['language'] = 'ro' 

owm = OWM('f8328971db2ccbe474c7fb2c7246465d',config_dict )
mgr = owm.weather_manager()

print( Back.BLACK )

place = input("Oras/Tara? : ")

observation = mgr.weather_at_place(place)
w = observation.weather
temp=w.temperature('celsius')['temp']

print( Back.BLACK )

print('In orasul/Tara:  ' + place + '  acum: ' + w.detailed_status)
print('Temperatura este in jur de:' + str(temp))
if temp<10:
	print('Ii frig tare , imbracate bine :D')
elif temp<20:
	print('Ii racoare imbracate')
else:
	print('Afara este cald')