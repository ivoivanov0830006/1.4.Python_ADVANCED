from collections import deque


def best_list_pureness(*args):
    all_rotations = {}
    count_rotations = args[-1]
    values = deque(args[0])
    for rotation in range(count_rotations + 1):
        total = 0
        for i in range(len(values)):
            total += values[i] * i
        all_rotations[rotation] = total
        first_value = values.pop()
        values.appendleft(first_value)

    best_rotation = 0
    best_total = 0
    for key, value in all_rotations.items():

        if value > best_total:
            best_rotation = key
            best_total = value

    return f"Best pureness {best_total} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)


"""
------------------------------------ Problem to resolve --------------------------------

Write function called best_list_pureness which will receive a list of numbers and a number K. 
You have to rotate the list K times (last becomes first) to find the variation of the list with 
the best pureness (pureness is calculated by summing all the elements in the list multiplied by 
their indices). For example, in the list [4, 3, 2, 6] with the best pureness is :
    (3 * 0) + (2 * 1) + (6 * 2) + (4 * 3) = 26. 
At the end the function should return a string containing the highest pureness and the amount 
of rotations that were made to find this pureness in the following format: 
        "Best pureness {pureness_value} after {count_rotations} rotations". 
If there is more than one highest pureness, take the first one.
Note: Submit only the function in the judge system
Input
⦁	There will be no input, just parameters passed to your function
Output
⦁	There is no expected output
⦁	The function should return a string in the following format: 
        "Best pureness {pureness_value} after {count_rotations} rotations"
-------------------------------------- Example inputs ----------------------------------
Test Code
test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)	
Output
Best pureness 26 after 3 rotations
Comment
Rotation 0 -> Pureness 25
Rotation 1 -> Pureness 16
Rotation 2 -> Pureness 23
Rotation 3 -> Pureness 26
Rotation 4 -> Pureness 25
-----------------------------------------
Test Code
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)	
Output
Best pureness 78 after 2 rotations
------------------------------------------
Test Code
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)	
Output
Best pureness 40 after 0 rotations	

"""
