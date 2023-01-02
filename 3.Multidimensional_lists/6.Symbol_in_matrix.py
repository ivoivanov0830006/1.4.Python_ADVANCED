n = int(input())

matrix = [list(input()) for _ in range(n)]

found = False

symbol = input()
for i in range(n):
    for j in range(n):
        if matrix[i][j] == symbol:
            found = True
            print(f"({i}, {j})")
            break
    if found:
        break
if not found:
    print(f"{symbol} does not occur in the matrix")

    
"""
------------------------------------- Another Solution ---------------------------------

def find_symbol(current_matrix, current_symbol):
    for i in range(n):
        for j in range(n):
            if current_matrix[i][j] == current_symbol:
                return i, j


n = int(input())

matrix = [list(input()) for _ in range(n)]
symbol = input()

result = find_symbol(matrix, symbol)

if result:
    row_index, column_index = result
    print(f"({row_index}, {column_index})")
else:
    print(f"{symbol} does not occur in the matrix")
    
------------------------------------ Problem to resolve --------------------------------

Write a program that reads a number - N, representing the rows and columns of a square matrix. On the 
next N lines, you will receive rows of the matrix. Each row consists of ASCII characters. After that, 
you will receive a symbol. Find the first occurrence of that symbol in the matrix and print its position
in the format: "({row}, {col})". You should start searching from the top left. If there is no such 
symbol, print the message "{symbol} does not occur in the matrix".
-------------------------------------- Example inputs ----------------------------------
Input	
3
ABC
DEF
X!@
!	
Output
(2, 1)
-----------------
Input
4
asdd
xczc
qwee
qefw
4
Output	
4 does not occur in the matrix

"""
