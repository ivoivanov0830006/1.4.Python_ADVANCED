text = input()
stack = []

for index in range(len(text)):
    char = text[index]
    if char == "(":
        stack.append(index)
    elif char == ")":
        last_opening_bracket = stack.pop()
        parentheses = text[last_opening_bracket:index + 1]
        print(parentheses)
