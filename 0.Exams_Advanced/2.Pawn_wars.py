matrix_size = 8

chess_board = []

for r in range(matrix_size, 0, -1):
    line = []
    for c in range(matrix_size):
        item = chr(97 + c) + str(r)
        line.append(item)
    chess_board.append(line)

white_position = []
black_position = []
matrix = []

for r in range(matrix_size):
    current_row = list(input().split())
    matrix.append(current_row)
    if "w" in current_row:
        c = current_row.index("w")
        white_position = [r, c]
    if "b" in current_row:
        c = current_row.index("b")
        black_position = [r, c]

while True:
    row_w, col_w = white_position[0], white_position[1]
    if row_w - 1 >= 0 and col_w - 1 >= 0:
        if matrix[row_w - 1][col_w - 1] == "b":
            row_w, col_w = white_position[0] - 1, white_position[1] - 1
            print(f"Game over! White win, capture on {chess_board[row_w][col_w]}.")
            break
    if row_w - 1 >= 0 and col_w - 1 < 8:
        if matrix[row_w - 1][col_w + 1] == "b":
            row_w, col_w = white_position[0] - 1, white_position[1] + 1
            print(f"Game over! White win, capture on {chess_board[row_w][col_w]}.")
            break
    white_position[0] -= 1
    if white_position[0] == 0:
        row_w, col_w = white_position[0], white_position[1]
        print(f"Game over! White pawn is promoted to a queen at {chess_board[row_w][col_w]}.")
        break

    row_b, col_b = black_position[0], black_position[1]
    if row_b + 1 < 8 and col_b - 1 >= 0:
        if matrix[row_b + 1][col_b - 1] == "w":
            row_b, col_b = black_position[0] + 1, black_position[1] - 1
            print(f"Game over! Black win, capture on {chess_board[row_b][col_b]}.")
            break
    if row_b + 1 < 8 and col_b + 1 < 8:
        if matrix[row_b + 1][col_b + 1] == "w":
            row_b, col_b = black_position[0] + 1, black_position[1] + 1
            print(f"Game over! Black win, capture on {chess_board[row_b][col_b]}.")
            break
    black_position[0] += 1
    if black_position[0] == matrix_size - 1:
        row_b, col_b = black_position[0], black_position[1]
        print(f"Game over! Black pawn is promoted to a queen at {chess_board[row_b][col_b]}.")
        break
