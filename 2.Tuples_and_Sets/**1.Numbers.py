def add_func(current_sequence, first, second, nums):
    if current_sequence == "First":
        return first.union(nums)
    if current_sequence == "Second":
        return second.union(nums)


def remove_func(current_sequence, first, second, nums):
    if current_sequence == "First":
        return first.difference(nums)
    if current_sequence == "Second":
        return second.difference(nums)


def check_func(first, second):
    if first.issubset(second) or second.issubset(first):
        return True
    else:
        return False


first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])

number_lines = int(input())

for _ in range(number_lines):
    input_data = input().split()
    command = input_data[0]
    sequence = input_data[1]
    numbers = set([int(x) for x in input_data[2:]])
    if command == "Add":
        if sequence == "First":
            first_sequence = add_func(sequence, first_sequence, second_sequence, numbers)
        elif sequence == "Second":
            second_sequence = add_func(sequence, first_sequence, second_sequence, numbers)
    elif command == "Remove":
        if sequence == "First":
            first_sequence = remove_func(sequence, first_sequence, second_sequence, numbers)
        elif sequence == "Second":
            second_sequence = remove_func(sequence, first_sequence, second_sequence, numbers)
    elif command == "Check" and sequence == "Subset":
        print(check_func(first_sequence, second_sequence))

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
