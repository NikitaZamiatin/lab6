num_criteria = int(input("Введите количество критериев: "))

matrix = [[1] * n for k in range(n)]

for i in range(n):
    for j in range(i+1, n):
        pair_weight = float(input(f"Введите значение попарного сравнения между критерием {i+1} и критерием {j+1}: "))
        matrix[i][j] = pair_weight
        matrix[j][i] = 1/pair_weight

weights = [sum(line)/n for line in matrix]

rounded_weights = [round(weight, 2) for weight in weights]

for i in range(len(weights)):
    print("Весовой коэффициент критерия "+(i+1)+": "+weights[i])