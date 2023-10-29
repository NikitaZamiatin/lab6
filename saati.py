num_criteria = int(input("Введите количество критериев: "))

if num_criteria == int:
    matrix = [[1] * num_criteria for k in range(num_criteria)]
    for i in range(num_criteria):
        for j in range(i+1, num_criteria):
            pair_weight = float(input(f"Введите значение попарного сравнения между критерием {i+1} и критерием {j+1}: "))
            matrix[i][j] = pair_weight
            matrix[j][i] = 1/pair_weight

for i in range(num_criteria):
        column_sum = sum(matrix[j][i] for j in range(num_criteria))
        for j in range(num_criteria):
            matrix[j][i] /= column_sum        

weights = [sum(line)/num_criteria for line in matrix]

rounded_weights = [round(weight, 2) for weight in weights]

for i in range(len(weights)):
    print("Весовой коэффициент критерия ", (i+1), ": ", rounded_weights[i], sep="") 