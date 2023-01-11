def fill_the_box(height, length, width, *args):
    volume = height * length * width
    left_cubes = 0
    for element in args:
        if element == "Finish":
            break

        if volume >= element:
            volume -= element
        else:
            element -= volume
            left_cubes += element
            volume = 0

    if volume:
        return f"There is free space in the box. You could put {volume} more cubes."
    else:
        return f"No more free space! You have {left_cubes} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))



"""
------------------------------------ Problem to resolve --------------------------------

Write a function called fill_the_box that receives a different number of arguments representing:
    * the height of a box
    * the length of a box
    * the width of a box
    * n-times a different number of cubes with exact size 1 x 1 x 1
    * a string "Finish"
Your task is to fill the box with the given cubes until the current argument equals "Finish".
The function should return a string in the following format:
If, at the end, there is free space left in the box, print:
"There is free space in the box. You could put {free space in cubes} more cubes."
If there is no free space in the box, print:
"No more free space! You have {cubes left} more cubes."
-------------------------------------- Example inputs ----------------------------------
Test Code	
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))	
Output
There is free space in the box. You could put 13 more cube.
-------------------------------------------------------------
Test Code	
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))	
Output
No more free space! You have 17 more cubes.
--------------------------------------------------------------
Test Code	
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))	
Output
There is free space in the box. You could put 960 more cubes.	

"""
