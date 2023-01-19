p1, p2 = input().split(", ")

matrix_rows, matrix_cols = 7, 7

matrix = [input().split() for _ in range(matrix_rows)]

p1_wins = False
p2_wins = False
total_points = {p1: 501, p2: 501}
total_throws = {p1: 0, p2: 0}
throw = 0

while True:
    command = list(map(int, input().strip("(").strip(")").split(", ")))
    row, col = command[0], command[1]
    points = 0

    throw += 1
    if row in range(len(matrix)) and col in range(len(matrix)):
        if throw % 2 != 0:
            total_throws[p1] += 1
            if matrix[row][col] == "D":
                points = (int(matrix[0][col]) + int(matrix[matrix_rows - 1][col]) +
                          int(matrix[row][0]) + int(matrix[row][matrix_cols - 1])) * 2
            elif matrix[row][col] == "T":
                points = (int(matrix[0][col]) + int(matrix[matrix_rows - 1][col]) +
                          int(matrix[row][0]) + int(matrix[row][matrix_cols - 1])) * 3
            elif matrix[row][col] == "B":
                p1_wins = True
                break
            else:
                points = int(matrix[row][col])
            total_points[p1] -= int(points)
            if total_points[p1] <= 0:
                p1_wins = True
                break
        else:
            total_throws[p2] += 1
            if matrix[row][col] == "D":
                points = (int(matrix[0][col]) + int(matrix[matrix_rows - 1][col]) +
                          int(matrix[row][0]) + int(matrix[row][matrix_cols - 1])) * 2
            elif matrix[row][col] == "T":
                points = (int(matrix[0][col]) + int(matrix[matrix_rows - 1][col]) +
                          int(matrix[row][0]) + int(matrix[row][matrix_cols - 1])) * 3
            elif matrix[row][col] == "B":
                p2_wins = True
                break
            else:
                points = int(matrix[row][col])
            total_points[p2] -= int(points)
            if total_points[p2] <= 0:
                p2_wins = True
                break
    else:
        if throw % 2 != 0:
            total_throws[p1] += 1
        else:
            total_throws[p2] += 1

if p1_wins:
    print(f"{p1} won the game with {total_throws[p1]} throws!")
if p2_wins:
    print(f"{p2} won the game with {total_throws[p2]} throws!")
