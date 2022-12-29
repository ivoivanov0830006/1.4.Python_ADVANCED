rows, columns = (int(x) for x in input().split(", "))
total_sum = 0

matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)
    total_sum += sum(row)

print(total_sum)
print(matrix)
