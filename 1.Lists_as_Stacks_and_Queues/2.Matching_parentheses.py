text = input()
stack = []

for index in range(len(text)):
    char = text[index]
    if char == "(":
        stack.append(index)
    elif char == ")":
        start_bracket = stack.pop()
        parentheses = text[start_bracket:index + 1]
        print(parentheses)


"""
------------------------------------- Problem to resolve ------------------------------

You are given an algebraic expression with parentheses.
Scan through the string and extract each set of parentheses.
  * If you find an opening parenthesis, push the index into the stack.
  * If you find a closing parenthesis, pop the topmost element from the stack. This is the index
  of the last opening parenthesis.
  * Use the current index and the popped one to extract a set of parentheses.
Print the result back on the console.
-------------------------------------- Example inputs ----------------------------------
Input	                                
1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5
Output
(2 + 3)
(3 + 1)                               
(2 - (2 + 3) * 4 / (3 + 1))                                 
------------------------------------------------------------------
Input
(2 + 3) - (2 + 3)
Output
(2 + 3)
(2 + 3)

"""
