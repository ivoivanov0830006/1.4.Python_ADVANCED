from collections import deque

numbers = deque(input().split())
numbers.reverse()

print(" ".join(numbers))


"""
------------------------------------- Another Solution -----------------------------
numbers = input().split()
stack = []

for index in range(len(numbers)):
    stack.append(numbers.pop())

print(" ".join(stack))


------------------------------------- Another Solution -----------------------------
print(*input().split()[::-1], sep=" ")


------------------------------------- Problem to resolve ------------------------------

Write a program that reads a string with N integers from the console, separated by a single space,
and reverses them using a stack. Print the reversed integers on one line, separated by a single space.
-------------------------------------- Example inputs ----------------------------------
Input	                
1 2 3 4 5	            
1
Output
5 4 3 2 1
1

"""
