number_names = int(input())
unique_names = set()

for _ in range(number_names):
    name = input()
    unique_names.add(name)

print("\n".join(unique_names))


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program, which will take a list of names and print only the unique names in the list.
# The order in which we print the result does not matter.
# -------------------------------------- Example inputs ----------------------------------
# Input	            Output
# 8                 Alan
# Lee               Joey
# Joey              Lee
# Lee               Joe
# Joe               Peter
# Alan
# Alan
# Peter
# Joey
# ------------------------------------------------------
# 7                 Easton
# Lyle              Lyle
# Bruce             Alice
# Alice             Bruce
# Easton            Shawn
# Shawn
# Alice
# Shawn
# -------------------------------------------------------
# 6                 Adam
# Adam

