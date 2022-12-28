number_elements = int(input())
unique_elements = set()

for _ in range(number_elements):
    compound = set(input().split())
    unique_elements = unique_elements.union(compound)

print("\n".join(unique_elements))


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that keeps all the unique chemical elements. On the first line, you will be given a
# number n - the count of input lines that you will receive. On the following n lines, you will be
# receiving chemical compounds separated by a single space. Your task is to print all the unique ones on
# separate lines (the order does not matter):
# -------------------------------------- Example inputs ----------------------------------
# Input	                Output
# 4                     Ce
# Ce O                  Ee
# Mo O Ce               Mo
# Ee                    O
# Mo
# ---------------------------------
# 3
# Ge Ch O Ne
# Nb Mo Tc
# O Ne	Ch
# Ge
# Mo
# Nb
# Ne
# O
# Tc
