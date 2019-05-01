# 1. Создайте класс Word.
# 2. Добавьте свойства text и part of speech.
# 3. Добавьте возможность создавать объект слово со значениями в скобках.
# 4. Создайте класс Sentence
# 5. Добавьте свойство content, равное списку, состоящему из номеров слов, входящих в предложение.
# 6. Добавьте метод show, составляющий предложение.
# 7. Добавьте метод show_parts, отображающий, какие части речи входят в предложение.

# Яркое солнце освещает утренний город.


class Word:
    text = "not"
    part_of_speech = "null"

    def __init__(self, text, part_of_speech):
        self.text = text
        self.part_of_speech = part_of_speech


class Sentence:
    content = []

    def __init__(self, content):
        self.content = content

    def show(self, spisok):
        all = ""
        for n in self:
            all = all + f" {spisok[n - 1]}"
        all = f"{all[1].title()}{all[2:]}."
        print(all)

    def show_parts(self, spisok):
        part = set()
        for n in self:
            part.add(spisok[n - 1])
        print(part)


bright = Word("яркое", "прилагательное")
sun = Word("солнце", "существительное")
light = Word("освещает", "глагол")
morning = Word("утренний", "прилагательное")
city = Word("город", "существительное")

spisok = [bright.text,sun.text,light.text,morning.text,city.text]
spisok_part = [bright.part_of_speech,sun.part_of_speech,light.part_of_speech,morning.part_of_speech,city.part_of_speech]

content = Sentence([4,5,3,1,2])
#content = Sentence([2,3])
#content = Sentence([2,1])
#content = Sentence([2,3,5])
#content = Sentence([1,2,3,4,5])

Sentence.show(content.content, spisok)
Sentence.show_parts(content.content, spisok_part)

