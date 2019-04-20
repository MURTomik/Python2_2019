# 1. Получите текст из файла.

import re
with open('text.txt', 'r', encoding='UTF-8') as f:
    text = f.read()
print(text)


# 2. Разбейте текст на предложения.
#разбиваем текст на предложения и записываем в файл text2.txt 

pattern2 = re.compile('(?<=\w[.!?])( |\n)')
text_list = pattern2.split(text)
for t in text_list:
    print(t)

with open('text2.txt', 'w', encoding='UTF-8') as f1:
    print(*text_list, file=f1, sep="\n")

# 3. Найдите самую используемую форму слова, состоящую из 4 букв и более, на русском языке.

pattern3 = re.compile('([а-яА-ЯёЁ]{4,})')

text_list3 = pattern3.findall(text)
result = {i: text_list3.count(i) for i in text_list3};
max_rezult = max(result.values())
print(result)
print(max_rezult)
print("3 задание  ",{word:kol for word, kol in result.items() if kol == max_rezult})

# 4. Отберите все ссылки.

pattern4 = re.compile('([\w+\.]{1,}[ru/][\w+\.]{1,}|[\w+\.]{1,}ru)')
text_list4 = pattern4.findall(text)
print("4 задание  ",text_list4)

# 5. Ссылки на страницы какого домена встречаются чаще всего?

text1 = text.lower()
text_list5 = re.findall('\w+\.ru',text1)
result5 = {i: text_list5.count(i) for i in text_list5};
max_rezult5 = max(result5.values())
print(text_list5)
print(result5)
print(max_rezult5)
print("5 задание  ",{domen:kol for domen, kol in result5.items() if kol == max_rezult5})


# 6. Замените все ссылки на текст «Ссылка отобразится после регистрации».
# Исключила Mail.ru - эксперимент

pattern6 = re.compile(' ([a-z0-9]+[\.]){1,}ru[/\w+]{0,}')
text_list6 = pattern6.sub('"Ссылка отобразится после регистрации"',text)
print("6 задание  ",text_list6)

