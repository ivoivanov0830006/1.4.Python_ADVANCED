from collections import deque


def best_list_pureness(*args):
    all_rotations = {}
    count_rotations = args[-1]
    values = deque(args[0])
    for rotation in range(count_rotations + 1):
        total = 0
        for i in range(len(values)):
            total += values[i] * i
        all_rotations[rotation] = total
        first_value = values.pop()
        values.appendleft(first_value)

    best_rotation = 0
    best_total = 0
    for key, value in all_rotations.items():

        if value > best_total:
            best_rotation = key
            best_total = value

    return f"Best pureness {best_total} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
