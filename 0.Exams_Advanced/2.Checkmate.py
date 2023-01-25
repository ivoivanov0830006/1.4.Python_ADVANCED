matrix_size = 8
matrix = []
queens_positions = []
king_position = []

for r in range(matrix_size):
    current_row = list(input().split())
    matrix.append(current_row)
    if "K" in current_row:
        c = current_row.index("K")
        king_position = [r, c]
    if "Q" in current_row:
        for c_index in range(len(current_row)):
            if current_row[c_index] == "Q":
                queens_positions.append([r, c_index])

directions = ((0, 1),       # RIGHT
              (0, -1),      # LEFT
              (-1, 0),      # UP
              (1, 0),       # DOWN
              (1, 1),       # UP RIGHT
              (1, -1),      # UP LEFT
              (-1, -1),     # DOWN LEFT
              (-1, 1))      # DOWN RIGHT

deadly_queens = []
the_king_is_safe = True

start_row = king_position[0]
start_col = king_position[1]

for direction in directions:
    king_position = [start_row, start_col]
    while True:
        c_row, c_col = int(king_position[0]), int(king_position[1])
        row, col = direction[0] + c_row, direction[1] + c_col

        if row not in range(len(matrix)) or col not in range(len(matrix)):
            break

        if matrix[row][col] == "Q":
            deadly_queens.append([row, col])
            the_king_is_safe = False
            break

        king_position = [row, col]

if the_king_is_safe:
    print("The king is safe!")
else:
    for queen in deadly_queens:
        print(queen)
