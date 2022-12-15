numbers = input().split()
stack = []
print(numbers)
for index in range(len(numbers)):
    stack.append(numbers.pop())

print(" ".join(stack))


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that reads a string with N integers from the console, separated by a single space,
# and reverses them using a stack. Print the reversed integers on one line, separated by a single space.
# -------------------------------------- Example inputs ----------------------------------
# Input	                Output
# 1 2 3 4 5	            5 4 3 2 1
# 1	                    1
