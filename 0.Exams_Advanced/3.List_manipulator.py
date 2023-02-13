import collections
from collections import deque


def list_manipulator(input_list, *args):
    # final_list = []
    current_list = deque(input_list)
    commands = deque(args)

    action = commands.popleft()
    location = commands.popleft()
    if action == "add" and location == "beginning":
        if commands:
            current_commands_list = list(collections.deque(commands))
            current_commands_list += current_list
            current_list = current_commands_list
    elif action == "add" and location == "end":
        if commands:
            for command in commands:
                current_list.append(int(command))
    elif action == "remove" and location == "beginning":
        if commands:
            for command in commands:
                for _ in range(command):
                    current_list.popleft()
        else:
            current_list.popleft()
    elif action == "remove" and location == "end":
        if commands:
            for command in commands:
                for _ in range(command):
                    current_list.pop()
        else:
            current_list.pop()

    final_list = list(collections.deque(current_list))
    # for element in current_list:
    #     final_list.append(element)

    return final_list


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
