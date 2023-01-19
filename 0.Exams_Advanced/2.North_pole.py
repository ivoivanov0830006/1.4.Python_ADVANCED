rows, cols = [int(x) for x in input().split(", ")]

matrix = []
position = []
total_items = {"D": 0, "G": 0, "C": 0}
collected_items = {"Decorations": 0, "Gifts": 0, "Cookies": 0}

for row in range(rows):
    current_row = input().split()
    matrix.append(current_row)
    if "Y" in current_row:
        position = [row, current_row.index("Y")]

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == "D":
            total_items["D"] += 1
        elif matrix[i][j] == "G":
            total_items["G"] += 1
        elif matrix[i][j] == "C":
            total_items["C"] += 1

success = False

while True:
    command = input()

    if command == "End":
        break
    current_command = command.split("-")
    direction = current_command[0]
    steps = int(current_command[1])
    for step in range(steps):

        if direction == "up":
            if position[0] == 0:
                position[0] = rows - 1
            else:
                position[0] -= 1
        elif direction == "down":
            if position[0] == rows - 1:
                position[0] = 0
            else:
                position[0] += 1
        elif direction == "left":
            if position[1] == 0:
                position[1] = cols - 1
            else:
                position[1] -= 1
        elif direction == "right":
            if position[1] == cols - 1:
                position[1] = 0
            else:
                position[1] += 1

        row, col = position[0], position[1]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "Y":
                    matrix[i][j] = "x"

        if matrix[row][col] == "D":
            total_items["D"] -= 1
            collected_items["Decorations"] += 1
        elif matrix[row][col] == "G":
            total_items["G"] -= 1
            collected_items["Gifts"] += 1
        elif matrix[row][col] == "C":
            total_items["C"] -= 1
            collected_items["Cookies"] += 1

        matrix[row][col] = "Y"

        if total_items["D"] == 0 and total_items["G"] == 0 and total_items["C"] == 0:
            success = True
            break

    if success:
        break

if success:
    print("Merry Christmas!")
print("You've collected:")
print(f"- {collected_items['Decorations']} Christmas decorations")
print(f"- {collected_items['Gifts']} Gifts")
print(f"- {collected_items['Cookies']} Cookies")

for row in matrix:
    print(*row)
