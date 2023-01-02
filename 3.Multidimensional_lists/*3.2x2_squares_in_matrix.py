rows, columns = [int(x) for x in input().split(' ')]
matrix = [input().split(' ') for _ in range(rows)]

count = 0
sub_matrix = []
for r in range(len(matrix) - 1):
    for c in range(len(matrix[r]) - 1):
        if matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
            sub_matrix = matrix[r][c], matrix[r][c + 1], matrix[r + 1][c], matrix[r + 1][c + 1]
            count += 1

print(count)


"""
------------------------------------ Problem to resolve --------------------------------

Find the number of all 2x2 squares containing identical chars in a matrix. On the first line, you will 
receive the matrix's dimensions in the format "{rows} {columns}". On the following rows, you will receive
characters separated by a single space. Print the number of all square matrices you have found.
-------------------------------------- Example inputs ----------------------------------
Input	
3 4
A B B D
E B B B
I J B B	
Output
2
----------------------
Input
2 2
a b
c d
Output
0
---------------------
Input
5 4
A A B D
A A B B
I J B B
C C C G
C C K P	
Output
3

"""
