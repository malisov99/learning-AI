#Примеры использования
bias = 5                #порог срабатывания
Xi = [1, 0, 0, 1]       #входной вектор
Wi = [5, 4, 1, 1]       #вектор весов

n = Neuron(Wi, bias)
S = n.weighted_sum(Xi)  #взвешенная сумма
print("S =", S)

print("Y (Хевисайда) = ", n.onestep(S))
print("Y (Сигмоида) = ", round(n.sigmoid(S), 4))
print("Y (ReLU) = ", n.relu(S))
print("Y (Гиперболический тангенс) = ", round(n.tanh(S), 4))