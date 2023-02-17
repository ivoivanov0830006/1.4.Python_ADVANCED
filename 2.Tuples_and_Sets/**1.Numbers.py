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


"""
------------------------------------- Problem to resolve ------------------------------

First, you will be given two sequences of integers values on different lines. The values of the 
sequences are separated by a single space between them.
Keep in mind that each sequence should contain only unique values.
Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:
    "Add First {args, separated by a space}" - add the given args at the end of the first sequence of args.
    "Add Second {args, separated by a space}" - add the given args at the end of the second sequence of args.
    "Remove First {args, separated by a space}" - remove only the args contained in the first sequence.
    "Remove Second {args, separated by a space}" - remove only the args contained in the second sequence.
    "Check Subset" - check if any of the given sequences are a subset of the other. If it is, print "True". 
Otherwise, print "False".
In the end, print the final sequences, separated by a comma and a space ", ". The values in each sequence 
should be sorted in ascending order.
-------------------------------------- Example inputs ----------------------------------
Input	
1 2 3 4 5
1 2 3
3
Add First 5 6
Remove Second 8 9 11
Check Subset	
Output
True
1, 2, 3, 4, 5, 6
1, 2, 3
--------------------------
Input	
5 4 2 9 9 5 4
1 1 1 5 6 5
4
Add First 5 6 9 3
Add Second 1 2 3 3 3
Check Subset
Remove Second 1 2 3 4 5	
Output
False
2, 3, 4, 5, 6, 9
6

"""
