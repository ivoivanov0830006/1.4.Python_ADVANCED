text = list(input())
stack = []

for i in range(len(text)):
    stack.append(text.pop())

print("".join(stack))

"""
------------------------------------- Another Solution -----------------------------
text = list(input())

while len(text) > 0:
    element = text.pop()
    print(element, end="")


------------------------------------- Problem to resolve ------------------------------

Write program that:
  * Reads an input string
  * Reverses it using a stack
Prints the result back on the console
-------------------------------------- Example inputs ----------------------------------
Input	                            
I Love Python
Output
nohtyP evoL I
------------------------------------------------
Input
Stacks and Queues
Output
seueuQ dna skcatS

"""
