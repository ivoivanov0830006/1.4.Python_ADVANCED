from collections import deque
import sys

max_number = -sys.maxsize
total_food = int(input())
total_orders = deque(map(int, input().split()))

for number in total_orders:  # print(max(total_orders))
    if number > max_number:  #
        max_number = number  #
print(max_number)            #

while len(total_orders):
    current_order = total_orders[0]
    if total_food < current_order:
        break
    current_order = total_orders.popleft()
    total_food -= current_order

if len(total_orders) == 0:
    print("Orders complete")
else:
    orders_left = (" ".join(map(str, total_orders)))
    print(f"Orders left: {orders_left}")
