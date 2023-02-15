import collections
from collections import deque


def stock_availability(input_list, *args):
    inventory = deque(input_list)
    commands = deque(args)

    action = commands.popleft()
    if action == "delivery":
        for command in commands:
            inventory.append(command)
    if action == "sell":
        if commands:
            for command in commands:
                if type(command) == int:
                    for _ in range(command):
                        inventory.popleft()
                else:
                    if command in inventory:
                        while command in inventory:
                            inventory.remove(command)

        else:
            inventory.popleft()

    result = list(collections.deque(inventory))
    return result


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
