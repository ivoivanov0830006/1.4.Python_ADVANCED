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
