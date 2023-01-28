from collections import deque

pumps_count = int(input())
pumps = deque()

for _ in range(pumps_count):
    liters, distance = input().split()
    pumps.append([int(liters), int(distance)])

for index in range(pumps_count):
    current_petrol = 0
    for pump in pumps:
        petrol = pump[0]
        distance = pump[1]
        current_petrol = current_petrol + petrol - distance
        if current_petrol < 0:
            pumps.append(pumps.popleft())
            break

    else:
        print(index)
        break

        
"""
from collections import deque

pump_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

pump_data_copy = pump_data.copy()
index = 0
gas_in_tank = 0

while pump_data_copy:
    petrol, distance = pump_data_copy.popleft()
    gas_in_tank += petrol

    if gas_in_tank < distance:
        pump_data.rotate(-1)
        pump_data_copy = pump_data.copy()
        index += 1
        gas_in_tank = 0
    else:
        gas_in_tank -= distance

print(index)
