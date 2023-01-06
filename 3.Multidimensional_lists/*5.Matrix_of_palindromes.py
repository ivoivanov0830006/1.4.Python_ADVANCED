rows, columns = [int(x) for x in input().split()]

matrix = []
for r in range(rows):
    line = []
    for c in range(columns):
        item = chr(97 + r) + chr(97 + r + c) + chr(97 + r)
        line.append(item)
    matrix.append(line)

for row in matrix:
    print(*row)

    
"""
------------------------------------- Another Solution ---------------------------------

rows, columns = list(map(int, input().split()))

for r in range(97, rows + 97):
    for c in range(columns):
        palindrome = f'{chr(r)}{chr(r + c)}{chr(r)}'
        print(palindrome, end=' ')
    print()
    

------------------------------------ Problem to resolve --------------------------------

Write a program to generate the following matrix of palindromes of 3 letters with r rows and c columns like
the one in the examples below.
⦁	Rows define the first and the last letter: row 0  'a', row 1  'b', row 2  'c', …
⦁	Columns + rows define the middle letter: 
⦁	column 0, row 0  'a', column 1, row 0  'b', column 2, row 0  'c', …
⦁	column 0, row 1  'b', column 1, row 1  'c', column 2, row 1  'd', …
Input
⦁	The numbers r and c stay at the first line at the input in the format "{rows} {columns}"
⦁	r and c are integers in the range [1, 26]
-------------------------------------- Example inputs ----------------------------------
Input	
4 6	
Output
aaa aba aca ada aea afa
bbb bcb bdb beb bfb bgb
ccc cdc cec cfc cgc chc
ddd ded dfd dgd dhd did
----------------------------
Input
3 2
Output
aaa aba
bbb bcb
ccc cdc

"""
