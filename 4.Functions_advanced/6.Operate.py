def operate(operation, *args):

    def add(*numbers):
        result = 0
        for i in numbers:
            result += i
        return result

    def subtract(x, *numbers):
        result = x
        for i in numbers:
            result -= i
        return result   # return  x + sum(-y for y in args)

    def multiply(*numbers):
        result = 1
        for i in numbers:
            result *= i
        return result

    def divide(x, *numbers):
        result = x
        for i in numbers:
            result /= i
        return result

    if operation == "+":
        return add(*args)
    elif operation == "-":
        return subtract(*args)
    elif operation == "*":
        return multiply(*args)
    elif operation == "/":
        return divide(*args)
    else:
        return None


print(operate("+", 1, 2, 3))
print(operate("-", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 8, 4, 2))
