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

    
"""
------------------------------------- Another Solution -----------------------------
from collections import deque

total_food = int(input())
total_orders = deque([int(x) for x in input().split()])

print(max(total_orders))

for order in total_orders.copy():
    if total_food - order >= 0:
        total_orders.popleft()
        total_food -= order
    else:
        orders_left = (" ".join(map(str, total_orders)))
        print(f"Orders left: {orders_left}")
        break
else:
    print("Orders complete")


------------------------------------- Problem to resolve ------------------------------

First, you will be given the quantity of the food you have for the day (an integer number).
Next, you will be given a sequence of integers (separated by a single space), each representing the
quantity of food in each order. Keep the orders in a queue.
Find the biggest order and print it. Next, you will begin servicing your clients from the first one
that came. Before each order, check if you have enough food left to complete it:
  * If you have, remove the order from the queue and reduce the quantity of food in the restaurant.
  * Otherwise, stop serving.
Input
On the first line, you will be given the quantity of your food - an integer in the range [0, 1000]
On the second line, you will receive a sequence of integers, representing each order, separated by a single space
Output
On the first line, print the quantity of the biggest order
On the second line:
If you succeeded in servicing all your clients, print: "Orders complete".
Otherwise, print: "Orders left: {order1} {order2} .... {orderN}".
Constraints
The input will always be valid
-------------------------------------- Example inputs ----------------------------------
Input	                            
348                               
20 54 30 16 7 9
Output
54
Orders complete
----------------------------------------------
Input	
499                               
57 45 62 70 33 90 88 76 100 50 
Output
Orders left: 76 100 50   
100

"""
