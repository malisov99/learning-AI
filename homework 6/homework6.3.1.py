#Задача 1. Книги без буквы E.

"""В истории литературы известен случай написания романа объемом около 50 тыс. слов, 
в котором ни разу не была употреблена самая популярная в английском алфавите буква E. 
Название его – «Gadsby». Напишите программу, которая будет считывать список слов из файла и собирать статистику о том, 
в каком проценте слов используется каждая буква алфавита. 
Выведите результат для всех 26 букв английского алфавита и отдельно отметьте букву, которая встречалась в словах наиболее редко. 
В вашей программе должны игнорироваться знаки препинания и регистр символов.

Подсказки.

Переведите все слова в верхний регистр:
word = word.upper().rstrip() # upper - переводит строку в верхний регистр

Создайте словарь со счетчиком слов, содержащий каждую букву
# Для каждой буквы инициализируем счетчик нулем
counts = {}
for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
       counts[ch] = 0

Наиболее редко используемые буквы можно найти следующим образом:
smallest_count = min(counts.values()) # min - возвращает наименьшее число в списке"""

#file = open("book.txt", "r")
#text = file.read()
#file.close()

text = "It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him."

text = text.upper().rstrip()

for ch in ",.!?;:-()\"'":
    text = text.replace(ch, "")

words = text.split()

counts = {}
for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
       counts[ch] = 0

for word in words:
    letters_in_word = set(word)

    for letter in letters_in_word:
        if letter in counts:
            counts[letter] += 1

smallest_count = min(counts.values())

print("Статистика использования букв: ")
total_words = len(words)

for letter in counts:
    percent = counts[letter] / total_words * 100
    print(letter, "-", round(percent, 2), "%")

print("\nСамая редко встречающаяся буква: ")
for letter in counts:
    if counts[letter] == smallest_count:
        print(letter, "(встречается в", smallest_count, "словах)")