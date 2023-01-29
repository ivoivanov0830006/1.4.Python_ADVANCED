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


------------------------------------- Problem to resolve ------------------------------

There is a robotics factory. The current project is assembly-line robots.
Each robot has a processing time – it is the time in seconds the robot needs to process a product.
When a robot is free, it should take a product for processing and log its name, product, and processing
start time.
Each robot processes a product coming from the assembly line. A product is coming from the line each
second (so the first product should appear at [start time + 1 second]). If a product passes the line
and there is not a free robot to take it, it should be queued at the end of the line again.
The robots are standing in the line in the order of their appearance.
Input
On the first line, you will receive the robots' names and their processing times in the format:
  * "robotName-processTime;robotName-processTime;robotName-processTime..."
On the second line, you will get the starting time in the format "hh:mm:ss"
Next, until the "End" command, you will get a product on each line.
Output
Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"
-------------------------------------- Example inputs ----------------------------------
Input	                        
ROB-15;SS2-10;NX8000-3        
8:00:00                       
detail                        
glass                         
wood
apple
End
Output
ROB - detail [08:00:01]
SS2 - glass [08:00:02]
NX8000 - wood [08:00:03]
NX8000 - apple [08:00:06]
-------------------------------------------------------
Input
ROB-8                         
7:59:59                       
detail                        
glass                         
wood
sock
End
Output
ROB - detail [08:00:00]
ROB - wood [08:00:08]
ROB - glass [08:00:16]
ROB - sock [08:00:24]
"""


    
