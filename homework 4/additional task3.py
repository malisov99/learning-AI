#Задача 3. Фонетический алфавит

"""Фонетический алфавит представляет собой таблицу обозначений букв, каждой из которых соответствует то или иное слово. 
Широкое распространение такие алфавиты приобретают в условиях повышенной зашумленности каналов передачи информации, 
когда собеседник может просто не расслышать конкретную букву. В таких случаях вместо букв используются целые слова. 
Один из наиболее распространенных фонетических алфавитов был разработан в военном блоке НАТО. 

Соответствие букв и слов в нем:

A - Alpha   | J - Juliet   | S - Sierra
B - Bravo   | K - Kilo     | T - Tango
C - Charlie | L - Lima     | U - Uniform
D - Delta   | M - Mike     | V - Victor
E - Echo    | N - November | W - Whiskey
F - Foxtrot | O - Oscar    | X - Xray
G - Golf    | P - Papa     | Y - Yankee
H - Hotel   | Q - Quebec   | Z - Zulu
I - India   | R - Romeo

Напишите программу, которая будет запрашивать слово у пользователя и отображать его на экране в виде шифра 
из соответствующих слов, обозначающих буквы исходного текста. Например, если пользователь введет слово Hello, 
на экране должна быть отображена следующая последовательность слов: Hotel Echo Lima Lima Oscar. 
Для решения этой задачи вам предстоит использовать рекурсивную функцию, а не циклы. 
При этом все небуквенные символы, введенные пользователем, можно игнорировать."""

nato_dict = {'A': 'Alpha', 'J': 'Juliet', 'S': 'Sierra',
'B': 'Bravo', 'K': 'Kilo', 'T': 'Tango',
'C': 'Charlie', 'L': 'Lima', 'U': 'Uniform',
'D': 'Delta', 'M': 'Mike', 'V': 'Victor',
'E': 'Echo', 'N': 'November', 'W': 'Whiskey',
'F': 'Foxtrot', 'O': 'Oscar', 'X': 'Xray',
'G': 'Golf', 'P': 'Papa', 'Y': 'Yankee',
'H': 'Hotel', 'Q': 'Quebec', 'Z': 'Zulu',
'I': 'India', 'R': 'Romeo'}

def encode_text(word):
    if word == "":
        return ""

    char = word[0].upper()
    remaining_text = word[1:]

    if char.isalpha():
        word_code = nato_dict[char]
        return (word_code + " " + encode_text(remaining_text)).strip()
    else:
        return encode_text(remaining_text)

user_word = input("Введите слово: ")
result = encode_text(user_word)
print(result)