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


"""
------------------------------------- Another Solution -----------------------------

longest_intersection = set()

for _ in range(int(input())):
    first_data, second_data = [el.split(",") for el in input().split("-")]

    first_range = set(range(int(first_data[0]), int(first_data[1]) + 1))
    second_range = set(range(int(second_data[0]), int(second_data[1]) + 1))

    intersection = first_range.intersection(second_range)

    if len(longest_intersection) < len(intersection):
        longest_intersection = intersection

longest_range = (', '.join(str(x) for x in longest_intersection))
print(f"Longest intersection is [{longest_range}] with length {len(longest_intersection)}")

