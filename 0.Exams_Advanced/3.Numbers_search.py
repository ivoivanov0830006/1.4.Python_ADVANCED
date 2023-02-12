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
    
    
------------------------------------ Problem to resolve --------------------------------

Write a function called numbers_searching which receives a different amount of parameters. All 
parameters will be integer numbers forming a sequence of consecutive numbers. Your task is to find 
an unknown amount of duplicates from the given sequence and a missing value, such that all the duplicate 
values and the missing value are between the smallest and the biggest received number. 
The function should return a list with the last missing number as a first argument and a sorted list, 
containing the duplicates found, in ascending order.
For example: 
    if we have the following numbers: 1, 2, 4, 2, 5, 4 will return 3 as missing number and 2, 4 as 
    duplicate numbers in the following format: [3, [2, 4]]
Input
⦁	There will be no input
⦁	Parameters will be passed to your function
Output
⦁	The function should return a list in the following format: 
        [missing number, [duplicate_numbers separated with comma and space]]
Constraints
⦁	The missing number will always be between the smallest and the biggest received number
-------------------------------------- Example inputs ----------------------------------
Input	
print(numbers_searching(1, 2, 4, 2, 5, 4))	
Output
[3, [2, 4]]
---------------------------------------------
Input
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))	
Output
[6, [5, 7, 9]]
---------------------------------------------
Input
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))	
Output
[46, [44, 45, 47, 48, 50]]

"""
