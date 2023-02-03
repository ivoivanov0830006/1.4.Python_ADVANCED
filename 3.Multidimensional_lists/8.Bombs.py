size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
coordinates = ((int(x) for x in coordinate.split(",")) for coordinate in input().split())

directions = (
    (-1, 0),        # up
    (1, 0),         # down
    (0, 1),         # right
    (0, -1),        # left
    (-1, 1),        # up-right
    (-1, -1),       # up-left
    (1, -1),        # down-left
    (1, 1),         # down-right
    (0, 0)          # current
)

for row, col in coordinates:
    if matrix[row][col] <= 0:
        continue

    for x, y in directions:
        r, c = row + x, col + y
        if 0 <= r < size and 0 <= c < size:
            matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0

alive_cells_count = 0
alive_cells_sum = 0

for row in matrix:
    for element in row:
        if element > 0:
            alive_cells_count += 1
            alive_cells_sum += element

print(f"Alive cells: {alive_cells_count}")
print(f"Sum: {alive_cells_sum}")
for row in matrix:
    print(*row, sep=" ")
