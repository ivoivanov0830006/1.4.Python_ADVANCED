rows = int(input())

flattened_matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    for number in row:
        flattened_matrix.append(number)
print(flattened_matrix)
