input_sequence = list(input().split("|"))
matrix = [([int(x) for x in sub_list.split()]) for sub_list in input_sequence]
flattened_matrix = []

for idx in range(len(matrix)):
    row = matrix[len(matrix) - 1 - idx]
    for number in row:
        flattened_matrix.append(number)
print(*flattened_matrix)


"""
------------------------------------- Another Solution ---------------------------------

input_sequence = list(input().split("|"))
sub_lists = []

for sub_string in input_sequence[::-1]:
    sub_lists.extend(sub_string.split())

print(*sub_lists)

