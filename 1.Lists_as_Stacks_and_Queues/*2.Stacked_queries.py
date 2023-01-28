import sys

max_number = -sys.maxsize
min_number = sys.maxsize

count = int(input())
stack = []

for _ in range(count):
    current_command = input().split()
    query = current_command[0]
    if query == "1":
        number = int(current_command[1])
        stack.append(number)
    elif query == "2":
        if stack:
            stack.pop()
    elif query == "3":
        for number in stack:
            if number > max_number:
                max_number = number
        print(max_number)
    elif query == "4":
        for number in stack:
            if number < min_number:
                min_number = number
        print(min_number)

final_stack = []

for i in range(len(stack)):
    final_stack.append(stack.pop())

print(" ".join(list(map(str, final_stack))))


# ------------------------------------- Another Solution -----------------------------
# from collections import deque
#
# numbers = deque()
# map_functions = {
#     1: lambda x: numbers.append(x[1]),
#     2: lambda x: numbers.pop() if numbers else None,
#     3: lambda x: print(max(numbers)),
#     4: lambda x: print(min(numbers)),
# }
#
# for _ in range(int(input())):
#     number_data = [int(x) for x in input().split()]
#     map_functions[number_data[0]](number_data)
#
# numbers.reverse()
#
# print(*numbers, sep=", ")
#
# ------------------------------------- Problem to resolve ------------------------------
#
# You have an empty stack. You will receive an integer – N. On the next - N lines, you will receive
# queries. Each query is one of these four types:
# '1 {number}' – push the number (integer) into the stack
# '2' – delete the number at the top of the stack
# '3' – print the maximum number in the stack
# '4' – print the minimum number in the stack
# It is guaranteed that each query is valid.
# After you go through all the queries, print the stack from top to bottom in the following format:
# "{n}, {n1}, {n2}, ... {nn}"
# -------------------------------------- Example inputs ----------------------------------
# Input	                Output
# 9                     26
# 1 97                  20
# 2                     91, 20, 26
# 1 20
# 2
# 1 26
# 1 20
# 3
# 1 91
# 4
# -------------------------------------
# 10                    32
# 2                     66
# 1 47                  8
# 1 66                  8, 16, 25, 32, 66, 47
# 1 32
# 4
# 3
# 1 25
# 1 16
# 1 8
# 4
