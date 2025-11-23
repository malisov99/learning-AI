#Задача 1. Класс Neuron

"""Используя примеры из теоретической части 5.1 и 5.2, составьте класс Neuron модели нейрона, 
принимающего на вход от одного до 10 входных параметров. Запрещается пользоваться библиотекой numpy. 
На вход подается список. Матричное умножение реализуется с помощью циклов самостоятельно. 
Класс содержит методы для вычисления взвешенной суммы, а также содержит функции активации из урока."""

import math

class Neuron:
    def __init__(self, w, bias=0):
        if not (1 <= len(w) <= 10):
            raise ValueError("Количество весов должно быть от 1 до 10")
        self.w = w
        self.bias = bias

    def weighted_sum(self, x):
        if len(x) != len(self.w):
            raise ValueError("Количество входов не совпадает с количеством весов")
        s = 0
        for i in range(len(x)):
            s += self.w[i] * x[i]
        s -= self.bias
        return s
#Функции активации
    def onestep(self, x):
        return 1 if x >= 0 else 0

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def relu(self, x):
        return x if x > 0 else 0

    def tanh(self, x):
        return math.tanh(x)