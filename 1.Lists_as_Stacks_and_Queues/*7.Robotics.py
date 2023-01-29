from collections import deque


def robot_time_decrease():
    global working_robots
    global available_robots

    for robot in [r for r in working_robots.keys()]:
        working_robots[robot] -= 1
        if working_robots[robot] == 0:
            del working_robots[robot]
            available_robots.append(robot)


def to_time(secs):
    hours = secs // 3600
    minutes = (secs % 3600) // 60
    seconds = (secs % 3600) % 60

    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


robots = {}
line = input().split(';')

for robot in line:
    name, process_time = robot.split('-')
    robots[name] = int(process_time)
available_robots = [r for r in robots.keys()]

working_robots = {}

time_str = input().split(':')
time_in_seconds = int(time_str[0]) * 60 * 60 + int(time_str[1]) * 60 + int(time_str[2])
items = deque()
line = input()

while line != 'End':
    items.append(line)
    line = input()

while items:
    current_item = items.popleft()
    time_in_seconds += 1
    robot_time_decrease()

    if time_in_seconds == (24 * 60 * 60):
        time_in_seconds = 0

    for robot_name in available_robots:
        if robot_name not in working_robots:
            print(f'{robot_name} - {current_item} [{to_time(time_in_seconds)}]')
            working_robots[robot_name] = robots[robot_name]
            break
    else:
        items.append(current_item)
        
        
"""
------------------------------------- Another Solution -----------------------------

from collections import deque
from datetime import datetime, timedelta

robots = {}

for r in input().split(";"):
    name, time_needed = r.split("-")
    robots[name] = [int(time_needed), 0]

factory_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()

while True:
    product = input()
    if product == "End":
        break

    products.append(product)

while products:
    factory_time += timedelta(0, 1)
    product = products.popleft()

    free_robots = []

    for name, value in robots.items():
        if value[1] != 0:
            robots[name][1] -= 1

    for name, value in robots.items():
        if value[1] == 0:
            free_robots.append([name, value])

    if not free_robots:
        products.append(product)
        continue

    robot_name, data = free_robots[0]
    robots[robot_name][1] = data[0]

    print(f"{free_robots[0][0]} - {product} [{factory_time.strftime('%H:%M:%S')}]")
    
