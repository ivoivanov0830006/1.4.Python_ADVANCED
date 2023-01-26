from collections import deque


def add_func(total_sum):
    if 100 <= total_sum <= 199:
        gifts["Gemstone"] += 1
    if 200 <= total_sum <= 299:
        gifts["Porcelain Sculpture"] += 1
    if 300 <= total_sum <= 399:
        gifts["Gold"] += 1
    if 400 <= total_sum <= 499:
        gifts["Diamond Jewellery"] += 1


materials = list([int(x) for x in input().split()])
magic_levels = deque([int(x) for x in input().split()])
total = 0
succeeded = False

gifts = {"Gemstone": 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}

while True:
    if not materials or not magic_levels:
        break

    first_magic = magic_levels.popleft()
    last_material = materials.pop()
    total = first_magic + last_material

    if total < 100:
        if total % 2 != 0:
            total = 2 * total
            if total >= 100:
                add_func(total)
        else:
            total = last_material * 2 + first_magic * 3
            if total >= 100:
                add_func(total)
    elif total > 499:
        total /= 2
        if total <= 499:
            add_func(total)

    else:
        add_func(total)

if gifts["Gemstone"] > 0 and gifts["Porcelain Sculpture"] > 0 or gifts["Gold"] > 0 and gifts["Diamond Jewellery"] > 0:
    succeeded = True

if succeeded:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic_levels:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")
for key, value in sorted(gifts.items()):
    if value > 0:
        print(f"{key}: {value}")


"""
------------------------------------ Problem to resolve --------------------------------

First, you will receive a sequence of integers representing the materials for every wedding present. 
After that, you will be given another sequence of integers – Genie magic level for every aim to make a gift.
Your task is to mix materials with magic levels so you can make presents, listed in the table below.
                    Gift	Magic needed
                Gemstone	100 to 199
     Porcelain Sculpture    200 to 299
                    Gold	300 to 399
       Diamond Jewellery	400 to 499
To make a present, you should take the last integer of materials and sum it with the first magic level value. 
If the result is between or equal to the numbers described in the table above, you make the corresponding gift 
and remove both materials and magic value. Otherwise:
    * If the product of the operation is under 100:
        And if it is an even number, double the materials, and triple the magic, then sum it again. 
        And if it is an odd number, double the sum of the materials and the magic level. 
        Then, check again if it is between or equal to any of the numbers in the table above.
    * If the product of the operation is more than 499, divide the sum of the material and the magic level by 2. 
        Then, check again if it is between or equal to any of the numbers in the table above.
    * If, however, the result is not between or equal to any of the numbers in the table above after performing 
    the calculation, remove both the materials and the magic level.
Stop crafting gifts when you are out of materials or magic level.
You have succeeded in crafting the presents when you've crafted either one of the pairs - a gemstone and a 
sculpture or gold and jewellery.
Input
The first line of input will represent the values of materials - integers, separated by a single space
On the second line, you will be given the magic levels - integers, separated by a single space
Output
On the first line - print whether you have succeeded in crafting the presents:
    "The wedding presents are made!"
    "Aladdin does not have enough wedding presents."
On the next two lines print the materials and magic that are left, if there are any, otherwise skip the line:
    "Materials left: {material1}, {material2}, …"
    "Magic left: {magicValue1}, {magicValue2}, …
On the next lines, print the gifts alphabetically that the Genie has crafted at least once:
    "{present1}: {amount}
     {present2}: {amount}
      …
     {presentN}: {amount}"
Constraints
All the materials values will be integers in the range [1, 1000]
Magic level values will be integers in the range [1, 1000]
-------------------------------------- Example inputs ----------------------------------
Input	
105 20 30 25
120 60 11 400 10 1	
Output
The wedding presents are made!
Magic left: 10, 1
Gemstone: 1
-----------------
Input	
30 5 21 6 0 91
15 9 5 15 8	
Output
Aladdin does not have enough wedding presents.
Materials left: 30
Gemstone: 1	
200
5 15 32 20 10 5	Aladdin does not have enough wedding presents.
Magic left: 15, 32, 20, 10, 5
Porcelain Sculpture: 1

"""
