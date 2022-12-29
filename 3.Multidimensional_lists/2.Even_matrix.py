rows = int(input())

matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    new_row = []
    for number in row:
        if number % 2 == 0:
            new_row.append(number)
    matrix.append(new_row)
print(matrix)
