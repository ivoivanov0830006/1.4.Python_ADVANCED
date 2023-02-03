matrix = [[int(x) for x in input().split()] for i in range(int(input()))]

while True:
    current_command = input()
    if current_command == "END":
        break
    command = current_command.split()
    action = command[0]
    row, col = int(command[1]), int(command[2])
    value = int(command[3])
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        current_value = matrix[row][col]
        if action == "Add":
            current_value += value
        if action == "Subtract":
            current_value -= value
        matrix[row][col] = current_value
    else:
        print("Invalid coordinates")

for r in matrix:
    print(*r)


"""
------------------------------------ Problem to resolve --------------------------------

Write a program that reads a matrix from the console and changes its values. On the first line, you will 
get the matrix's rows - N. You will get elements for each column on the following N lines, 
separated with a single space. You will be receiving commands in the following format:
⦁	"Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
⦁	"Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
If the coordinate is invalid, you should print "Invalid coordinates". A coordinate is valid if both of 
the given indexes are in range [0; len() – 1].
When you receive "END", you should print the matrix and stop the program.
-------------------------------------- Example inputs ----------------------------------
Input	
3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END	
Output
6 2 3
4 3 6
7 8 9
------------------
Input
4
1 2 3 4
5 6 7 8
8 7 6 5
4 3 2 1
Add 4 4 100
Add 3 3 100
Subtract -1 -1 42
Subtract 0 0 42
END	
Output
Invalid coordinates
Invalid coordinates
-41 2 3 4
5 6 7 8
8 7 6 5
4 3 2 101

"""
