#пример 1
x = [1, 1, 1, 1] #солнечно, выходной, компания есть, уставший

s = neuron.y(x)
decision = neuron.onestep(s)

print("Взвешенная сумма:", s)
if decision == 1:
    print("Идем гулять")
else:
    print("Остаемся дома")