number_lines = int(input())

odd_set = set()
even_set = set()
row = 0

for _ in range(number_lines):
    row += 1
    current_name = input()
    total_sum = 0
    for char in current_name:
        total_sum += ord(char)

    total_sum = int(total_sum / row)

    if total_sum % 2 == 0:
        even_set.add(total_sum)
    else:
        odd_set.add(total_sum)

sum_odd_set = sum(odd_set)
sum_even_set = sum(even_set)

if sum_odd_set < sum_even_set:
    result = odd_set.symmetric_difference(even_set)
elif sum_odd_set > sum_even_set:
    result = odd_set.difference(even_set)
else:
    result = odd_set.union(even_set)

result = (', '.join(str(x) for x in result))
print(result)


# ------------------------------------- Problem to resolve ------------------------------
#
# You will receive a number N. On the following N lines, you will be receiving names. You should sum the ASCII
# values of each letter in the name and integer divide it by the number of the current row (starting from 1).
# Save the result to a set of either odd or even numbers, depending on if the resulting number is odd or even.
# After that, sum the values of each set.
#   * If the sums of the two sets are equal, print the union of the values, separated by ", ".
#   * If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values,
#   separated by ", ".
#   * If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric-different
#   values, separated by ", ".
# NOTE: On every operation, the starting set should be the odd set
# -------------------------------------- Example inputs ----------------------------------
# Input	            Output
# 4                 304, 128, 206, 511
# Pesho
# Stefan
# Stamat
# Gosho
# ---------------------------------------
# 6                 733, 101
# Preslav
# Gosho
# Ivan
# Stamat
# Pesho
# Stefan
