from collections import deque


def operator_func(operator, bee, nec):
    result = 0
    if operator == "+":
        result = bee + nec
    elif operator == "-":
        result = bee - nec
    elif operator == "/":
        result = bee / nec
    elif operator == "*":
        result = bee * nec
    return result


bees = deque([int(x) for x in input().split()])
nectar = list([int(x) for x in input().split()])
operators = deque([str(x) for x in input().split()])

total_honey = 0

while True:
    if not bees or not nectar:
        break

    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_bee < current_nectar:
        current_operator = operators.popleft()
        total_honey += abs(operator_func(current_operator, current_bee, current_nectar))
    elif current_bee > current_nectar:
        bees.appendleft(current_bee)

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
    

