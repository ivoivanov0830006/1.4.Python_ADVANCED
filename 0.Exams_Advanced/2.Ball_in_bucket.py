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

    
"""
------------------------------------ Problem to resolve --------------------------------

You will be given a matrix with 6 rows and 6 columns representing the board. On the board, there 
will be points (integers) and buckets marked with the letter "B". Rules of the game:
    * You can throw a ball only 3 times.
    * When you hit a bucket (position 'B'), you score the sum of the points in the same column.
    * You can hit a bucket only once. If you hit the same bucket again, you do not score any points. 
    * If you hit outside a bucket (hit a number on the board) or outside the board - no points. 
After the board state, you are going to receive the information for every throw on a separate 
line. The coordinates’ information of a hit will be in the format: 
    "({row}, {column})".
Depending on how many points you have collected, you win one of the following:
                  Football	100 to 199 points
                Teddy Bear	200 to 299 points
     Lego Construction Set	300 and more points
Your job is to keep track of the scored points and to check if you won a prize. 
On the first line:
    * If you won a prize, print: 
            "Good job! You scored {points} points, and you've won {prize}."
    * If you did not win any prize, print the points you need to get at least the first prize: 
            "Sorry! You need {points} points more to win a prize."
Constraints
All of the given points will be integers in the range [1, 30]
All the given indexes will be integers in the range [0, 30]
There always will be exactly 6 buckets - 1 on each column
-------------------------------------- Example inputs ----------------------------------
Input	
10 30 B 4 20 24
7 8 27 23 11 19
13 3 14 B 17 В
12 5 21 22 9 6
B 26 1 28 29 2
25 B 16 15 B 18
(1, 1)
(20, 15)
(4, 0)	
Output
Sorry! You need 33 points more to win a prize.
-------------------------------------------------
Input	
B 30 14 23 20 24
29 8 27 18 11 19
13 3 B B 17 6
28 5 21 22 9 B
10 B 26 12 B 2
25 1 16 15 7 4
(0, 0)
(2, 2)
(2, 3)	
Output
Good job! You scored 299 points, and you've won Teddy Bear.

"""
