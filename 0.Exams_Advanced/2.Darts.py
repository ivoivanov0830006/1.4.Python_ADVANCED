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

    
"""
------------------------------------ Problem to resolve --------------------------------

You will be given a matrix with 7 rows and 7 columns representing the dartboard. For example:

1	2	3	4	5	6	7
24	D	D	D	D	D	8
23	D	T	T	T	D	9
22	D	T	B	T	D	10
21	D	T	T	T	D	11
20	D	D	D	D	D	12
19	18	17	16	15	14	13

Each of the two players starts with a score of 501 and they take turns to throw a dart – one throw
for each player. The score for each turn is deducted from the player’s total score. The first 
player who reduces their score to zero or less wins the game.
You are going to receive the information for every throw on a separate line. The coordinate 
information of a hit will be in the format: 
        "({row}, {column})".
    * If a player hits outside the dartboard, he does not score any points.
    * If a player hits a number, it is deducted from his total.
    * If a player hits a "D" the sum of the 4 corresponding numbers per column and row is doubled 
    and then deducted from his total.
    * If a player hits a "T" the sum of the 4 corresponding numbers per column and row is tripled 
    and then deducted from his total.
"B" is the bullseye. 
    * If a player hits it, he wins the game, and the program ends.
For example, if Peter hits position with coordinates (2, 1), he wins (23 + 2 + 9 + 18) * 2 = 104 points 
and they are deducted from his total. Your job is to find who won the game and with how many turns.
You should print only one line containing the winner and his count of throws: 
        "{name} won the game with {count_turns} throws!"
Constrains
There will always be exactly 7 lines
There will always be a winner
The points will be in range [1, 24]
The coordinates will be in range [0, 100]    
