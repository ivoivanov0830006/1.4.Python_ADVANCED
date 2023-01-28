clothes = list(map(int, input().split()))
rack_capacity = int(input())

rack_count = 1
current_rack = 0

for _ in range(len(clothes)):
    if current_rack + clothes[-1] > rack_capacity:
        rack_count += 1
        current_rack = clothes.pop()
    elif current_rack + clothes[-1] == rack_capacity:
        current_rack = 0
        clothes.pop()
        if clothes:
            rack_count += 1

    else:
        current_rack += clothes.pop()

print(rack_count)



"""
------------------------------------- Another Solution -----------------------------

clothes = list(map(int, input().split()))
rack_capacity = int(input())

rack_count = 1
current_rack = rack_capacity

while clothes:
    cloth = clothes.pop()

    if current_rack - cloth >= 0:
        current_rack -= cloth
    else:
        rack_count += 1
        current_rack = rack_capacity - cloth

print(rack_count)

------------------------------------- Problem to resolve ------------------------------

You own a fashion boutique and receive a delivery of a huge box of clothes, represented as a sequence
of integers. On the following line, you will be given an integer representing the capacity for one rack
in your store.
You must arrange the clothes in the store and use the racks to hang up every piece of clothing. You start
from the last piece of clothing on the top of the pile to the first one at the bottom. Use a stack for
this purpose. Each piece of clothing has its value (an integer). You must sum their values while you
take them out of the box:
  * If the sum becomes equal to the capacity of the current rack, you must take a new one for the next
  clothes (if there are any left in the box).
  * If the sum becomes greater than the capacity, do not hang the piece of clothing on the current rack.
  Take a new rack and then hang it up.
In the end, print how many racks you have used to hang up the clothes.
Constraints
The values of the clothes will be integers in the range [0,20]
There will never be more than 50 clothes in a box
The capacity will be an integer in the range [0,20]
None of the integers from the box will be greater than the value of the capacity
-------------------------------------- Example inputs ----------------------------------
Input    
5 4 8 6 3 8 7 7 9        	                
16
Output
5
----------------------------------------
1 7 8 2 5 4 7 8 9 6 3 2 5 4 6     
20
Output
5
"""
