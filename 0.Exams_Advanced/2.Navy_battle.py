size = int(input())

matrix = []
cruisers = []
start_position = []

for i in range(size):
    row = list(input())
    matrix.append(row)
    if "S" in row:
        start_position = [i, row.index("S")]
    if "C" in row:
        for c_index in range(len(row)):
            if row[c_index] == "C":
                cruisers.append([i, c_index])

hits = 0
destroyed = False
win = False
row, col = "", ""

while True:
    if hits > 2:
        destroyed = True
        break
    if not cruisers:
        win = True
        break

    command = input()
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
    matrix[start_position[0]][start_position[1]] = "-"   # matrix[row][col]

    if matrix[row][col] == "*":
        matrix[row][col] = "S"
        hits += 1

    elif matrix[row][col] == "C":
        matrix[row][col] = "S"
        position = [row, col]
        cruisers.pop(cruisers.index(position))

    matrix[row][col] = "S"
    start_position = next_position

if destroyed:
    print(f'Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!')
if win:
    print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
for row in matrix:
    print("".join(row))

    
"""
------------------------------------ Problem to resolve --------------------------------

You will be given an integer n for the size of the battlefield (square shape). On the next n lines, 
you will receive the rows of the battlefield. The submarine will start at a random position, marked 
with the letter 'S'. The submarine surveys the surrounding area through its periscope, so it has to 
climb up to periscope depth, where it might run across naval mines.
When the submarine receives direction, it goes deep and moves one position toward the given direction. 
On each turn, you will be guiding the submarine and giving it the direction, in which it should move. 
The commands will be "up", "down", "left" and "right".
When a new position is reached,  the submarine climbs up to periscope depth to search for a cruiser:
    ⦁	If a position with '-' (dash) is reached, it means that the field is empty and the submarine 
    awaits its next direction.
    ⦁	If it runs across a naval mine ('*'), the submarine takes serious damage. When a mine is blown,
    the position of the mine will be marked with '-' (dash). U-9 can withstand two hits from naval mi0nes.
    The third time the submarine is hit by a mine, it disappears and the mission is failed. The battle 
    is over and the following message should be printed on the Console: 
            "Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!"
    ⦁	If a battle cruiser is reached ('C'), the submarine destroys it and the position of the destroyed 
    cruiser will be marked with '-' (dash).
    ⦁	If this is the last (third) battle cruiser on the battlefield, the battle is over and the following 
    message should be printed on the Console: "Mission accomplished, U-9 has destroyed all battle cruisers
    of the enemy!"
The program will end when the battle is over (All battle cruisers are destroyed or the submarine hits 
mines three times).
thing).
    ⦁	If all battle cruisers are destroyed, print: "Mission accomplished, U-9 has destroyed all battle 
    cruisers of the enemy!"
    ⦁	If U-9 is hit by a mine three times, print: "Mission failed, U-9 disappeared! 
    Last known coordinates [{row}, {col}]!".
    ⦁	At the end, print the final state of the matrix (battlefield) with the last known U-9’s position on it.
