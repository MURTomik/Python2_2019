# Шаг первый
# 1. Создайте класс Word.
# 2. Добавьте свойства text и part of speech.
# 3. Добавьте возможность создавать объект слово со значениями в скобках.
# 4. Создайте класс Sentence
# 5. Добавьте свойство content, равное списку, состоящему из номеров слов, входящих в предложение.
# 6. Добавьте метод show, составляющий предложение.
# 7. Добавьте метод show_parts, отображающий, какие части речи входят в предложение.

# Шаг второй
# 1. Создайте классы Noun и Verb.
# 2. Настройте наследование от Word.
# 3. Добавьте защищенное свойство «Грамматические характеристики».
# 4. Перестройте работу метода show класса Sentence.
# 5. Перестройте работу метода show_part класса Sentence, чтобы он показывал грамматические характеристики.

class Word:

    def __init__(self, text = "not", part_of_speech = "null"):
        self.text = text
        self.part_of_speech = part_of_speech
        # защищенное свойство, как я поняла, защита состоит в том что его явно нигде не видно, если не знаешь о нем.
        self.__grammatic = "0"


class Sentence:
    def __init__(self, content = []):
        self.content = content

    def show(self, spisok):
        all = ""
        for n in self.content:
            all = all + f" {spisok[n - 1]}"
        print(f"{all[1].title()}{all[2:]}.")

    def show_parts(self, spisok,spisok_gr):
        part = dict()
        for n in self.content:
            part[spisok[n - 1]] = spisok_gr[n - 1]
        print(part)

class Noun(Word):
    # Корректно ли использовать pass? 
    pass
    # def __init__(self, text, part_of_speech):
    #     super().__init__(text, part_of_speech)


class Verb(Word):

    def __init__(self, text, part_of_speech):
        super().__init__(text, part_of_speech)

bright = Word("яркое", "прилагательное")
bright._Word__grammatic = "3"
print(f"Защищенное свойство - {bright._Word__grammatic}")

sun = Noun("солнце", "существительное")
sun._Noun__grammatic = "1"
print(f"Защищенное свойство - {sun._Noun__grammatic}")

light = Verb("освещает", "глагол")
light._Verb__grammatic = "2"
print(f"Защищенное свойство - {light._Verb__grammatic}")

morning = Word("утренний", "прилагательное")
morning._Word__grammatic = "3"
city = Noun("город", "существительное")
city._Noun__grammatic = "1"
run = Verb("бежит", "глагол")
run._Verb__grammatic = "2"
sky = Noun("небо", "существительное")
sky._Noun__grammatic = "1"



spisok1 = [bright.text,sun.text,light.text,morning.text,city.text,run.text,sky.text]
spisok_part1 = [bright.part_of_speech,sun.part_of_speech,light.part_of_speech,morning.part_of_speech,city.part_of_speech,run.part_of_speech,sky.part_of_speech]
spisok_gr = [bright._Word__grammatic,sun._Noun__grammatic,light._Verb__grammatic,morning._Word__grammatic,city._Noun__grammatic,run._Verb__grammatic,sky._Noun__grammatic]

content1 = Sentence([1,2,3,7])
#content1 = Sentence([4,5,3,1,2])
#content1 = Sentence([2,3])
#content1 = Sentence([2,1])
#content1 = Sentence([2,3,5])
#content1 = Sentence([1,2,3,4,5])

content1.show(spisok1)
content1.show_parts(spisok_part1,spisok_gr)

