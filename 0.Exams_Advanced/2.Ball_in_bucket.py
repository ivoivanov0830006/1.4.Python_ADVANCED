matrix_size = 6
matrix = []
for i in range(matrix_size):
    current_row = input().split()
    matrix.append(current_row)

gifts = {"Football": 0,
         "Teddy Bear": 0,
         "Lego Construction Set": 0
         }

throws = 0
points = 0

while True:
    if throws == 3:
        break
    command = list(map(int, input().strip("(").strip(")").split(", ")))
    row, col = command[0], command[1]
    throws += 1
    if row in range(len(matrix)) and col in range(len(matrix)):
        current_shot = matrix[row][col]
        column_sum = 0
        if current_shot == "B":
            matrix[row][col] = "0"
            for r in range(matrix_size):
                column_sum += int(matrix[r][col])
            points += column_sum

if 100 <= points <= 199:
    gifts["Football"] += 1
elif 200 <= points <= 299:
    gifts["Teddy Bear"] += 1
elif 300 <= points:
    gifts["Lego Construction Set"] += 1

if points >= 100:
    for prize, quantity in gifts.items():
        if quantity > 0:
            print(f"Good job! You scored {points} points, and you've won {prize}.")
            break
else:
    needed_points = 100 - points
    print(f"Sorry! You need {needed_points} points more to win a prize.")
