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
    

------------------------------------- Problem to resolve ------------------------------

You will be given a sequence consisting of parentheses. Your job is to determine whether the expression
is balanced. A sequence of parentheses is balanced if every opening parenthesis has a corresponding
closing parenthesis that occurs after the former. There will be no interval symbols between the
parentheses. You will be given three types of parentheses: (), {}, and [].
  {[()]} - Parentheses are balanced.
  (){}[] - Parentheses are balanced.
  {[(])} - Parentheses are NOT balanced.
-------------------------------------- Example inputs ----------------------------------
Input	                    
{[()]}
Output
YES
----------------------
Input
{[(])}
Output	              
NO
----------------------
Input
{{[[(())]]}}	      
Output
YES

"""
