number_lines = int(input())

longest_length = 0
longest_range = ()

for _ in range(number_lines):
    first_set = set()
    second_set = set()
    command = input().split("-")
    first_range = command[0].split(",")
    first_start = int(first_range[0])
    first_end = int(first_range[1])
    for num in range(first_start, first_end + 1):
        first_set.add(num)
    second_range = command[1].split(",")
    second_start = int(second_range[0])
    second_end = int(second_range[1])
    for num in range(second_start, second_end + 1):
        second_set.add(num)
    current_longest_range = first_set.intersection(second_set)
    current_longest_length = len(current_longest_range)
    if longest_length < current_longest_length:
        longest_length = current_longest_length
        longest_range = current_longest_range

longest_range = (', '.join(str(x) for x in longest_range))

print(f"Longest intersection is [{longest_range}] with length {longest_length}")


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that finds the longest intersection. You will be given a number N. On each of the next
# N lines you will be given two ranges in the format:
#       "{first_start},{first_end}-{second_start},{second_end}".
# You should find the intersection of these two ranges. The start and end numbers in the ranges are inclusive.
# Finally, you should find the longest intersection of all N intersections, print the numbers that are included
# and its length in the format:
#       "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"
# Note: in each range, there will always be an intersection. If there are two equal intersections, print the first one.
# -------------------------------------- Example inputs ----------------------------------
# Input	                    Output
# 3                         Longest intersection is [6, 7, 8, 9, 10] with length 5
# 0,3-1,2
# 2,10-3,5
# 6,15-3,10
# -----------------------------------------------------------------------------------------
# 5                         Longest intersection is [2, 3, 4, 5, 6, 7, 8, 9, 10] with length 9
# 0,10-2,5
# 3,8-1,7
# 1,8-2,4
# 4,7-2,5
# 1,10-2,11
