sequence = input()
opening_brackets = []

pairs = {"(": ")", "{": "}", "[": "]"}
balanced = True

for char in sequence:
    if char in "({[":
        opening_brackets.append(char)
    elif not opening_brackets:
        balanced = False
    else:
        last_opening_bracket = opening_brackets.pop()
        if pairs[last_opening_bracket] != char:
            balanced = False

    if not balanced:
        break

if not balanced or opening_brackets:
    print("NO")
else:
    print("YES")

    
"""
------------------------------------- Another Solution -----------------------------

from collections import deque

parentheses = deque(input())
open_parentheses = deque()

while parentheses:
    left_parenthesis = parentheses.popleft()

    if left_parenthesis in "{([":
        open_parentheses.append(left_parenthesis)
    elif not open_parentheses:
        print("NO")
        break
    else:
        if f"{open_parentheses.pop() + left_parenthesis}" not in "{}()[]":
            print("NO")
            break
else:
    print("YES")
