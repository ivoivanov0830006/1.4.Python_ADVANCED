input_sequence = list(input().split("|"))
matrix = [([int(x) for x in sub_list.split()]) for sub_list in input_sequence]
flattened_matrix = []

for idx in range(len(matrix)):
    row = matrix[len(matrix) - 1 - idx]
    for number in row:
        flattened_matrix.append(number)
print(*flattened_matrix)
