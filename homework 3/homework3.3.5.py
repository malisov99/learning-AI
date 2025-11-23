#Задача 5. Ниже и выше среднего.

"""Напишите программу, которая будет запрашивать у пользователя числа, пока не будет введена пустая строка. 
Сначала на экран должно быть выведено среднее значение введенного ряда чисел, 
после этого друг за другом необходимо вывести список чисел ниже среднего, равных ему (если такие найдутся) и выше среднего. 
Каждый список должен предваряться соответствующим заголовком."""

#Создаем пустой список
nums = []
#Запрашиваем ввод от пользователя
user_input = input("Введите чила (пустая строка для окончания ввода): ")
#Создаем цикл для добавления чисел в список
while user_input != "":
  num = int(user_input)
  nums.append(num)
  user_input = input("Введите числа (пустая строка для окончания ввода): ")
#Условие для среднего значения
if nums:
  average = sum(nums) / len(nums)
  print("Среднее значение введенных чисел: %d" % average)
#Создаем списки с другими значениями
below_average = []
for num in nums:
    if num < average:
        below_average.append(num)

equal_average = []
for num in nums:
    if num == average:
        equal_average.append(num)

above_average = []
for num in nums:
    if num > average:
        above_average.append(num)
#Выводим
print("Числа ниже среднего: ")
print(below_average)

print("Числа равные среднему значению: ")
print(equal_average)

print("Числа выше среднего: ")
print(above_average)