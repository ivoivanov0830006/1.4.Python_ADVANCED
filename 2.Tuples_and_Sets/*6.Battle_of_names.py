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
