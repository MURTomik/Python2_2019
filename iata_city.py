# 1. Написать функцию получения IATA-кода города из его названия, используя API Aviasales.
# Сделала две функции, поиск по разным ссылкам (в первой не нужно использовать модуль re,
# но необходимо вводить город четко без ошибок, вторая позволяет ошибаться при вводе города)
# https://www.travelpayouts.com/widgets_suggest_params?q=Из%20"+city.title()+"%20в%20Москва
# http://autocomplete.travelpayouts.com/places2?term="+city.title()+"&locale=ru


import requests, json, re

def iata(city):
    link1 = "https://www.travelpayouts.com/widgets_suggest_params?q=Из%20"
    link2 = "%20в%20Москва"
    link = link1 + city.title() + link2
    data = json.loads(requests.get(link).text)
    if len(data) == 0:
        err = "Город введен неверно"
    else:
        err = "IATA код города {} будет {}".format(city, data['origin']['iata'])
    return err

def iata_other(city):
    link = "http://autocomplete.travelpayouts.com/places2?term="+city.title()+"&locale=ru"
    data = str(json.loads(requests.get(link).text))
    kod = re.compile('code\': \'(\w{3})')
    if len(data) > 2:
        err = "IATA код города {} будет {}".format(city, kod.findall(data)[0])
    else:
        err = "Город введен неверно"
    return err

print("Здравствуйте, Дмитрий!")
while (True):
    input_city = input("Введите название города для получения iata кода: ")
    data_iata = iata_other(input_city)
#    data_iata = iata(input_city)
    otv = int(input("{}, если будете продолжать введите - 1: ".format(data_iata)))
    if otv == 1:
        continue
    else:
        break
