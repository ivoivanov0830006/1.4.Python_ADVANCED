def get_magic_triangle(rows):
    magic_triangle = [[1], [1, 1]]
    for row in range(2, rows):
        new_row = []
        for num in range(len(magic_triangle[row - 1])):
            if num + 1 <= len(magic_triangle[row - 1]) - 1:
                new_row.append(magic_triangle[row - 1][num] + magic_triangle[row - 1][num + 1])
            else:
                break
        magic_triangle.append([1, *new_row, 1])

    return magic_triangle


print(get_magic_triangle(5))


"""
------------------------------------ Problem to resolve --------------------------------

Create a function called get_magic_triangle which will receive a single parameter (integer n) and it 
should create a magic triangle which follows those rules:
⦁	We start with this simple triangle [[1], [1, 1]]
⦁	We generate the next rows until we reach n amount of rows
⦁	Each number in each row is equal to the sum of the two numbers right above it in the triangle
⦁	If the current number has no neighbor to the upper left/right, we just take the existing neighbor
After you create the magic triangle, return it as a multidimensional list. Here is an example with n = 5
 
Note: Submit only the function in the judge system
Input
⦁	There will be no inputs
⦁	The function will be tested by passing different values of n
⦁	You can test your function with the test code below
Constraints
⦁	N will be in range [2, 100]
-------------------------------------- Example inputs ----------------------------------
Test Code	
get_magic_triangle(5)	
Output
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

"""
