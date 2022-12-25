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
