rows, columns = [int(x) for x in input().split()]

matrix = []
for r in range(rows):
    line = []
    for c in range(columns):
        item = chr(97 + r) + chr(97 + r + c) + chr(97 + r)
        line.append(item)
    matrix.append(line)

for row in matrix:
    print(*row)
