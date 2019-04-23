# 1. Получить количество учеников с сайта geekbrains.ru:
# a) при помощи регулярных выражений

import re

with open('kod.html',encoding='UTF-8') as f:
    text = f.read()

usl = re.compile("<span.+([0-9]\s[0-9]{1,}\s[0-9]{1,}).*?</span>")
text1 = usl.findall(text)
print(text1[0])

usl1 = re.compile("<span class=\"total-users\">(.+[0-9]\s[0-9]{1,}\s[0-9]{1,}.*?)</span>")
text2 = usl1.findall(text)
print(text2[0])

# b) при помощи библиотеки BeautifulSoup.
# (Использовала модуль requests для информации в реальном времени)

import requests
from bs4 import BeautifulSoup as BS

response = requests.get('https://geekbrains.ru')
text = response.content
# with open('kod.html',encoding='UTF-8') as f:
#     text = f.read()

soup = BS(text, "html.parser")
print(soup.span.string)






