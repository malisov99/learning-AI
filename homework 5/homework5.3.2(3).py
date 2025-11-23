#пример 2
x = [0, 1, 0, 1] #плохая погода, есть время, компании нет, уставший

s = neuron.y(x)
decision = neuron.onestep(s)

print("Взвешенная сумма:", s)
if decision == 1:
    print("Идем гулять")
else:
    print("Остаемся дома")