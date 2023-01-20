matrix = []
matrix_size = 6
position = []

for i in range(matrix_size):
    row = input().split()
    matrix.append(row)
    if "E" in row:
        position = [i, row.index("E")]

water_deposit = 0
metal_deposit = 0
concrete_deposit = 0

directions = input().split(", ")
for direction in directions:
    if direction == "up":
        if position[0] == 0:
            position[0] = matrix_size - 1
        else:
            position[0] -= 1
    elif direction == "down":
        if position[0] == matrix_size - 1:
            position[0] = 0
        else:
            position[0] += 1
    elif direction == "left":
        if position[1] == 0:
            position[1] = matrix_size - 1
        else:
            position[1] -= 1
    elif direction == "right":
        if position[1] == matrix_size - 1:
            position[1] = 0
        else:
            position[1] += 1

    row, col = position[0], position[1]

    if matrix[row][col] == "W":
        print(f"Water deposit found at ({row}, {col})")
        water_deposit += 1
    elif matrix[row][col] == "M":
        print(f"Metal deposit found at ({row}, {col})")
        metal_deposit += 1
    elif matrix[row][col] == "C":
        print(f"Concrete deposit found at ({row}, {col})")
        concrete_deposit += 1
    elif matrix[row][col] == "R":
        print(f"Rover got broken at ({row}, {col})")
        break

if water_deposit > 0 and metal_deposit > 0 and concrete_deposit > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

    
"""
------------------------------------ Problem to resolve --------------------------------

You will receive a 6x6 field on separate lines with:
    * One rover - marked with the letter "E"
    * Water deposit (one or many) - marked with the letter "W"
    * Metal deposit (one or many) - marked with the letter "M"
    * Concrete deposit (one or many) - marked with the letter "C"
    * Rock (one or many) - marked with the letter "R"
    * Empty positions will be marked with "-"
After that, you will be given the commands for the rover's movement on one line separated by a comma 
and a space (", "). Commands can be: "up", "down", "left", or "right".
For each command, the rover moves in the given directions with one step, and it can land on one of 
the given types of deposit or a rock:
    * When it lands on a deposit, you must print the coordinates of that deposit in the format shown 
    below and increase its value by 1.
    * If the rover lands on a rock, it gets broken. Print the coordinates where it got broken in the 
    format shown below, and the program ends.
    * If the rover goes out of the field, it should continue from the opposite side in the same direction. 
Example: If the rover is at position (3, 0) and it needs to move left (outside the matrix), it should 
be placed at position (3, 5).
The rover needs to find at least one of each deposit to consider the area suitable to start our colony. 
Stop the program if you run out of commands or the rover gets broken.
For each deposit found while you go through the commands, print out on the console: 
        "{Water, Metal or Concrete} deposit found at ({row}, {col})"
If the rover hits a rock, print the coordinates where it got broken in the format: 
        "Rover got broken at ({row}, {col})"
After you go through all the commands or the rover gets broken, print out on the console:
    * If the rover has found at least one of each deposit, print on the console: 
            "Area suitable to start the colony."
    * Otherwise, print on the console: 
            "Area not suitable to start the colony."
