num_criteria = int(input("Введите количество критериев: "))

matrix = [[1] * n for k in range(n)]

for i in range(n):
    for j in range(i+1, n):
        value = float(input(f"Введите значение попарного сравнения между критерием {i+1} и критерием {j+1}: "))
        matrix[i][j] = value
        matrix[j][i] = 1/value

