text = list(input())
stack = []

for i in range(len(text)):          # while text:
    stack.append(text.pop())        

print("".join(stack))


# ------------------------------------- Problem to resolve ------------------------------
#
# Write program that:
#   * Reads an input string
#   * Reverses it using a stack
# Prints the result back on the console
# -------------------------------------- Example inputs ----------------------------------
# Input	                            Output
# I Love Python	                    nohtyP evoL I
# ------------------------------------------------
# Stacks and Queues	                seueuQ dna skcatS
