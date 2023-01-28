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


------------------------------------- Another Solution -----------------------------

from collections import deque

pumps_count = int(input())
pumps = deque()


for _ in range(pumps_count): 
    pump_data = [int(x) for x in input().split()]
    pumps.append(pump_data)

for index in range(pumps_count):
    current_petrol = 0
    failed = False
    for fuel, distance in pumps:
        current_petrol += fuel
        if distance > current_petrol:
            failed = True
            break

        else:
            current_petrol -= distance
    if failed:
        # pumps.append(pumps.popleft())
        pumps.rotate(-1)
    else:
        print(index)
        break
        
        
------------------------------------- Problem to resolve ------------------------------

There is a circle road with N petrol pumps. The petrol pumps are numbered 0 to (N−1) (both inclusive).
For each petrol pump, you will receive two pieces of information (separated by a single space):
  * The amount of petrol the petrol pump will give you
  * The distance from that petrol pump to the next petrol pump (kilometers)
You are a truck driver, and you want to go all around the circle. You know that the truck consumes 1
liter of petrol per 1 kilometer, and its tank has infinite petrol capacity.
In the beginning, the tank is empty, but you start your journey at a petrol pump so you can fill it
with the given amount of petrol.
Your task is to calculate the first petrol pump from where the truck will be able to complete the circle.
You never miss filling its tank at a petrol pump.
Input
On the first line, you will receive the number of petrol pumps - N
On the next N lines, you will receive the amount of petrol that each petrol pump will give and the
distance between that petrol pump and the next petrol pump, separated by a single space
Output
An integer which will be the smallest index of a petrol pump from which you can start the tour
Constraints
1 ≤ N ≤ 1000001
1 ≤ amount of petrol, distance ≤ 1000000000
You will always have at least one point from where the truck will be able to complete the circle
-------------------------------------- Example inputs ----------------------------------
Input	        
3
1 5
10 3
3 4
Output
1
--------------------------
Input	
5
22 5
14 10
52 7
21 12
36 9
Output
0

"""
