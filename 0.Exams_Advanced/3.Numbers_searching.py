from collections import deque


def numbers_searching(*args):
    max_num = max(args)
    min_num = min(args)
    sorted_numbers = deque(sorted(args))

    missing_number = 0
    clean_list = []
    duplicated_list = []

    while sorted_numbers:
        first_num = sorted_numbers.popleft()
        if first_num not in clean_list:
            clean_list.append(first_num)
        else:
            if first_num not in duplicated_list:
                duplicated_list.append(first_num)

    for number in range(min_num, max_num + 1):
        if number not in clean_list:
            missing_number = number
            break

    return [missing_number, duplicated_list]


print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))


"""
------------------------------------- Another Solution ---------------------------------

def numbers_searching(*args):
    check_for_missing = set(sorted(args))
    first = min(check_for_missing)
    last = max(check_for_missing)
    full_list = [x for x in range(first, last + 1)]
    missing = list(set(full_list) - check_for_missing)

    duplicates = []
    find_duplicates = set(args)
    for x in find_duplicates:
        if args.count(x) > 1:
            duplicates.append(x)

    return [*missing, sorted(duplicates)]
