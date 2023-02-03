def is_outside(current_r, current_c, r, c):
    return current_r < 0 or current_c < 0 or current_r >= r or current_c >= c


def get_children(current_r, current_c, r, c):
    result = []
    possible_children_coordinates = [
        [current_r - 1, current_c],
        [current_r, current_c - 1],
        [current_r, current_c + 1],
        [current_r + 1, current_c]
    ]
    for current_child_row, current_child_col in possible_children_coordinates:
        if not is_outside(current_child_row, current_child_col, r, c):
            result.append([current_child_row, current_child_col])
    return result


input_rows, input_cols = [int(x) for x in input().split()]

directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1)
}

bunnies = set()
position = []
matrix = []

for i in range(input_rows):
    current_row = list(input())
    matrix.append(current_row)
    if "P" in current_row:
        position = [i, current_row.index("P")]
    if "B" in current_row:
        for bunny_index in range(len(current_row)):
            if current_row[bunny_index] == "B":
                bunnies.add(f"{i} {bunny_index}")

input_directions = input()

won = False
dead = False

for direction in input_directions:
    row, col = position[0] + directions[direction][0], position[1] + directions[direction][1]   # next pos
    matrix[position[0]][position[1]] = "."  # current pos

    new_bunnies = set()
    for bunny in bunnies:
        bunny_row, bunny_col = [int(x) for x in bunny.split()]
        children = get_children(bunny_row, bunny_col, input_rows, input_cols)
        for child_row, child_col in children:
            new_bunnies.add(f"{child_row} {child_col}")
            matrix[child_row][child_col] = "B"
            if child_row == row and child_col == col:
                dead = True
                break

    bunnies = bunnies.union(new_bunnies)

    if is_outside(row, col, input_rows, input_cols):
        position = [position[0], position[1]]
        won = True
        break
    elif matrix[row][col] == "B":
        position = [row, col]
        dead = True
        break
    else:
        matrix[row][col] = "P"
        position = [row, col]

for row in matrix:
    print("".join(row))
if won:
    print(f"won: {position[0]} {position[1]}")
if dead:
    print(f"dead: {position[0]} {position[1]}")
