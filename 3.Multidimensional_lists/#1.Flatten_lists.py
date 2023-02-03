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


------------------------------------ Problem to resolve --------------------------------

Write a program to flatten several lists of numbers received in the following format:
⦁	String with numbers or empty strings separated by "|"
⦁	Values are separated by spaces (" ", one or several)
⦁	Order the output list from the last to the first matrix sub-lists and their values from left to 
right as shown below
Examples
Input	Output
1 2 3 |4 5 6 |  7  88	7 88 4 5 6 1 2 3
7 | 4  5|1 0| 2 5 |3	3 2 5 1 0 4 5 7
1| 4 5 6 7  |  8 9	8 9 4 5 6 7 1

"""
