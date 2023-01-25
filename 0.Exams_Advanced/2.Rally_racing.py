size = int(input())
car_number = input()

matrix = []
tunnels = []
start_position = [0, 0]

distance = 0
disqualified = False
win = False

for i in range(size):
    row = input().split()
    matrix.append(row)
    if "T" in row:
        for t_index in range(len(row)):
            if row[t_index] == "T":
                tunnels.append([i, t_index])
    if "F" in row:
        end_position = [i, row.index("F")]

while True:
    command = input()
    if command == "End":
        matrix[start_position[0]][start_position[1]] = "C"
        disqualified = True
        break

    next_position = []
    if command == "up":
        next_position = [start_position[0] - 1, start_position[1]]
    elif command == "down":
        next_position = [start_position[0] + 1, start_position[1]]
    elif command == "left":
        next_position = [start_position[0], start_position[1] - 1]
    elif command == "right":
        next_position = [start_position[0], start_position[1] + 1]

    row, col = next_position[0], next_position[1]
    matrix[start_position[0]][start_position[1]] = "."   # matrix[row][col]

    if matrix[row][col] == ".":
        matrix[row][col] = "C"
        distance += 10

    elif matrix[row][col] == "T":
        matrix[row][col] = "."
        tunnel_exit = tunnels[1]
        next_position = [tunnel_exit[0], tunnel_exit[1]]
        distance += 30

    elif matrix[row][col] == "F":
        matrix[row][col] = "C"
        distance += 10
        win = True
        break

    start_position = next_position

if disqualified:
    print(f"Racing car {car_number} DNF.")
if win:
    print(f"Racing car {car_number} finished the stage!")
print(f"Distance covered {distance} km.")
for row in matrix:
    print("".join(row))
