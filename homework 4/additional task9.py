#Задача 9. Кодирование на основе длин серий

"""Напишите рекурсивную функцию, реализующую алгоритм кодирования на основе длин серий, описанный в предыдущей задачи. 
На вход функции должен поступать список или строка, а на выходе будет закодированный список. 
В основной программе запросите у пользователя строку, сожмите ее при помощи своей функции и отобразите на экране кодированный список."""

def rle_encode_recursive(sequence):
    if not sequence:
        return []

    def count_repeats(seq, char):
        if not seq or seq[0] != char:
            return 0
        return 1 + count_repeats(seq[1:], char)

    first_char = sequence[0]
    repeats = count_repeats(sequence, first_char)

    return [first_char, repeats] + rle_encode_recursive(sequence[repeats:])

if __name__ == "__main__":
    user_string = input("Введите строку для сжатия: ")

    encoded_list = rle_encode_recursive(list(user_string))
    print("Закодированный список:", encoded_list)