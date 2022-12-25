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

        
 # ------------------------------------- Another Solution -----------------------------
#
# from collections import deque
#
# pumps_count = int(input())
# pumps = deque()
#
# for _ in range(pumps_count):
#     pump_data = [int(x) for x in input().split()]
#     pumps.append(pump_data)
#
# for index in range(pumps_count):
#     current_petrol = 0
#     failed = False
#     for fuel, distance in pumps:
#         current_petrol += fuel
#         if distance > current_petrol:
#             failed = True
#             break
#
#         else:
#             current_petrol -= distance
#     if failed:
#         # pumps.append(pumps.popleft())
#         pumps.rotate(-1)
#     else:
#         print(index)
#         break
