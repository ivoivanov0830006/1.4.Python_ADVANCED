p1, p2 = input().split(", ")

matrix = []
for i in range(6):
    matrix.append(input().split())

win = False
winner = ""
trap = False
loser = ""

p1_rest = False
p2_rest = False

while True:
    command_p1 = list(map(int, input().strip("(").strip(")").split(", ")))
    if not p1_rest:
        row, col = command_p1[0], command_p1[1]
        if matrix[row][col] == "E":
            win = True
            winner = p1
            break
        elif matrix[row][col] == "T":
            trap = True
            loser = p1
            winner = p2
            break
        elif matrix[row][col] == "W":
            p1_rest = True
            print(f"{p1} hits a wall and needs to rest.")
    else:
        p1_rest = False

    command_p2 = list(map(int, input().strip("(").strip(")").split(", ")))
    if not p2_rest:
        
 
"""
------------------------------------ Problem to resolve --------------------------------

First, you will be given the names "Tom" and "Jerry", separated by a comma and a space ", ". The order in 
which they are received determines the order in which they will take turns. The first player starts first.
Next, you will be given a matrix with 6 rows and 6 columns representing the maze board. It consists of:
    ⦁	Only one Exit - marked with the "E" letter
    ⦁	Trap (one, many, or none) - marked with the "T" letter
    ⦁	Wall (one, many, or none) - marked with the "W" letter
    ⦁	Empty positions will be marked with "."
In the beginning, Tom and Jerry are outside the board. On each line, after the matrix is given, you will be 
receiving coordinates for each of the players. They will be taking turns and stepping on different positions 
on the board until one of them find the Exit or falls into a Trap. Here are the rules:
    ⦁	If a player hits the letter "E", he escapes the maze and wins the game.
    ⦁	Print "{player} found the Exit and wins the game!" and end the program.
    ⦁	If the letter "T" is hit, the player falls into a Trap, the game ends, and his opponent wins automatically.
    ⦁	Print "{player} is out of the game! The winner is {winner}." and end the program.
    ⦁	If the letter "W" is hit, the player hits a wall, and he needs to rest. The player's next move is ignored.
    ⦁	Print "{player} hits a wall and needs to rest."
    ⦁	If a player steps on an empty position ".", nothing happens. 
    ⦁	Both players can step in the same position at the same time.
You should print the output as described above and the input coordinates will always be valid.
        row, col = command_p2[0], command_p2[1]
        if matrix[row][col] == "E":
            win = True
            winner = p2
            break
        elif matrix[row][col] == "T":
            trap = True
            loser = p2
            winner = p1
            break
        elif matrix[row][col] == "W":
            p2_rest = True
            print(f"{p2} hits a wall and needs to rest.")
    else:
        p2_rest = False

if win:
    print(f"{winner} found the Exit and wins the game!")
if trap:
    print(f"{loser} is out of the game! The winner is {winner}.")
