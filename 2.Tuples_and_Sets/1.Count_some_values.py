sequence = input().split()
all_elements = []

for element in sequence:
    count = sequence.count(element)
    number = float(element)
    if element not in all_elements:
        all_elements.append(element)
        print(f"{number:.1f} - {count} times")
        

# ------------------------------------- Another Solution -----------------------------
#
# sequence = list(map(float, input().split()))
# all_elements = {}
#
# for element in sequence:
#     if element not in all_elements:
#         all_elements[element] = 0
#     all_elements[element] += 1
#
# for number, count in all_elements.items():     # all_elements.items returns tuples
#     print(f"{number:.1f} - {count} times")


# ------------------------------------- Problem to resolve ------------------------------
#
# You will be given numbers separated by a space. Write a program that prints the number of occurrences
# of each number in the format "{number} - {count} times". The number must be formatted to the first
# decimal point.
# -------------------------------------- Example inputs ----------------------------------
# Input	                                        Output
# -2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3               -2.5 - 3 times
# 	                                            4.0 - 2 times
#                                               3.0 - 4 times
#                                               -5.5 - 1 times
# ------------------------------------------------------
# 2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3       2.0 - 3 times
# 	                                            4.0 - 6 times
#                                               5.0 - 4 times
#                                               3.0 - 7 times

