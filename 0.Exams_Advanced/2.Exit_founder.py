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
