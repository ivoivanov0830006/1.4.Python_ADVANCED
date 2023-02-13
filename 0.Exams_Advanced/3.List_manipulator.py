import collections
from collections import deque


def list_manipulator(input_list, *args):
    # final_list = []
    current_list = deque(input_list)
    commands = deque(args)

    action = commands.popleft()
    location = commands.popleft()
    if action == "add" and location == "beginning":
        if commands:
            current_commands_list = list(collections.deque(commands))
            current_commands_list += current_list
            current_list = current_commands_list
    elif action == "add" and location == "end":
        if commands:
            for command in commands:
                current_list.append(int(command))
    elif action == "remove" and location == "beginning":
        if commands:
            for command in commands:
                for _ in range(command):
                    current_list.popleft()
        else:
            current_list.popleft()
    elif action == "remove" and location == "end":
        if commands:
            for command in commands:
                for _ in range(command):
                    current_list.pop()
        else:
            current_list.pop()

    final_list = list(collections.deque(current_list))
    # for element in current_list:
    #     final_list.append(element)

    return final_list


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))


"""
------------------------------------ Problem to resolve --------------------------------

Write a function called list_manipulator which receives a list of numbers as first parameter and 
different amount of other parameters. The second parameter might be "add" or "remove". The third 
parameter might be "beginning" or "end". There might or might not be any other parameters (numbers):
    * In case of "add" and "beginning", add the given numbers to the beginning of the given list of 
    numbers and return the new list
    * In case of "add" and "end", add the given numbers to the end of the given list of numbers and 
    return the new list
    * In case of "remove" and "beginning"
        - If there is another parameter (number), remove that amount of numbers from the beginning of 
        the list of numbers.
        - If there are no other parameters, remove only the first element of the list.
        - Finaly, return the new list
    * In case of "remove" and "end"
        - If there is another parameter (number), remove that amount of numbers from the end of the 
        list of numbers.
        - Otherwise if there are no other parameters, remove only the last element of the list.
        - Finaly, return the new list
Input
There will be no input
Parameters will be passed to your function
Output
The function should return the new list of numbers
-------------------------------------- Example inputs ----------------------------------
Test Code	                                                            Output
print(list_manipulator([1,2,3], "remove", "end"))                       [1, 2]      
print(list_manipulator([1,2,3], "remove", "beginning"))                 [2, 3]      
print(list_manipulator([1,2,3], "add", "beginning", 20))                [20, 1, 2, 3]       
print(list_manipulator([1,2,3], "add", "end", 30))                      [1, 2, 3, 30]      
print(list_manipulator([1,2,3], "remove", "end", 2))                    [1]
print(list_manipulator([1,2,3], "remove", "beginning", 2))              [3]     
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))        [20, 30, 40, 1, 2, 3]
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))              [1, 2, 3, 30, 40, 50]  	

"""
