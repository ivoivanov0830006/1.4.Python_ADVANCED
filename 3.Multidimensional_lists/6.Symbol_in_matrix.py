n = int(input())

matrix = [list(input()) for _ in range(n)]

found = False

symbol = input()
for i in range(n):
    for j in range(n):
        if matrix[i][j] == symbol:
            found = True
            print(f"({i}, {j})")
            break
    if found:
        break
if not found:
    print(f"{symbol} does not occur in the matrix")
