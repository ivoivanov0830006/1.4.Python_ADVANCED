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


"""
------------------------------------- Problem to resolve ------------------------------

Write a program that evaluates a string expression. You will be given that string expression on the 
first line in the form of args and operators separated with a single space from each other. Your job is 
to take that string expression and calculate the result after evaluating it.
To do that, you have to follow a simple rule. If, for example, we have this string "2 4 * 1 3 -", the 
first time we meet an operator (*), we should take all the args we have so far (2, 4), apply that operation 
to them, and save the result (8). The next time we meet an operator (-), we again take all the args we have 
(8, 1, 3) and apply the operator to them in that order (8 - 1 - 3 = 4). In the end, we print the result.
All the args will always be integers, and the possible operators are "*", "+", "-", "/". It is important 
to keep the order of the args (especially for "/" and "-" because the order matters). When having a 
division, you should round the result to the lower integer.
Input
Single line: a string containing integers and operators
Output
Single number: the result after the evaluation
Constrains
When reaching an operator, it is sure that you will have a minimum of one number to evaluate
The string will always end with an operator, so you get one number as a result
Operators and args will always be valid
There will be no case of division by zero
There might be negative args in the string
-------------------------------------- Example inputs ----------------------------------
Input	
6 3 - 2 1 * 5 /
Output
1
-------------------
Input
2 2 - 1 *
Output
0
-------------------
Input
10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *
Output
164

"""
