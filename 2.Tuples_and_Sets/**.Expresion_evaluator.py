from collections import deque


def operator_func(current_operator, current_total, current_digits):
    while current_digits:
        current_number = digits.popleft()
        if current_operator == "+":
            current_total += current_number
        elif current_operator == "-":
            current_total -= current_number
        elif current_operator == "/":
            current_total //= current_number
        elif current_operator == "*":
            current_total *= current_number
    return current_total


expression = input().split()

digits = deque()
total = 0
count = 0

for symbol in expression:
    if symbol in "+-/*":
        operation = symbol
        total = operator_func(operation, total, digits)
    else:
        digits.append(int(symbol))
        if count == 0:
            number = digits.popleft()
            total += number

    count += 1

print(total)
