#1. Написать функцию получения IATA-кода города из его названия, используя API Aviasales.

import requests
import json

def iata(city):
    link1 = "https://www.travelpayouts.com/widgets_suggest_params?q=Из%20"
    link2 = "%20в%20Москва"
    link = link1+city.title()+link2
    data = json.loads(requests.get(link).text)
    if len(data) == 0:
        err = "Город введен неверно"
    else:
        err = "IATA код города {} будет {}".format(city, data['origin']['iata'])
    return err

print("Здравствуйте, Дмитрий!")
while (True):
    input_city = input("Введите название города для получения iata кода: ")
    data_iata = iata(input_city)
    otv = int(input("{}, если будете продолжать введите - 1: ".format(data_iata)))
    if otv == 1:
        continue
    else:
        break





