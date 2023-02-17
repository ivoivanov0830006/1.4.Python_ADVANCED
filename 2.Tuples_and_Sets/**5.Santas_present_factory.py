from collections import deque

presents = {
        "Doll": 0,
        "Wooden train": 0,
        "Teddy bear": 0,
        "Bicycle": 0
}
boxes = deque([int(x) for x in input().split()])
magic = deque([int(x) for x in input().split()])

succeeded = False

while True:
    if len(boxes) == 0 or len(magic) == 0:
        break
    current_box = boxes.pop()
    current_magic = magic.popleft()

    if current_box == 0 and current_magic == 0:
        continue
    if current_box == 0:
        magic.appendleft(current_magic)
        continue
    elif current_magic == 0:
        boxes.append(current_box)
        continue

    result = current_box * current_magic

    if result < 0:
        total_sum = current_magic + current_box
        boxes.append(total_sum)
    elif result == 400:         # BIKE
        presents["Bicycle"] += 1
    elif result == 300:   # BEAR
        presents["Teddy bear"] += 1
    elif result == 250:   # TRAIN
        presents["Wooden train"] += 1
    elif result == 150:   # DOLL
        presents["Doll"] += 1
    else:                      # NO TOY
        current_box += 15
        boxes.append(current_box)

if presents["Doll"] >= 1 and presents["Wooden train"] >= 1 or presents["Teddy bear"] >= 1 and presents["Bicycle"] >= 1:
    succeeded = True

if succeeded:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if boxes:
    print(f"Materials left: {', '.join(map(str, reversed(boxes)))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

for key, value in sorted(presents.items()):
    if value > 0:
        print(f"{key}: {value}")


"""
------------------------------------- Problem to resolve ------------------------------

First, you will receive a sequence of integers representing the number of materials for crafting 
toys in one box. After that, you will be given another sequence of integers – their magic level.
Your task is to mix materials with magic so you can craft presents, listed in the table below with 
the exact magic level:
             Present	Magic needed
                Doll	150
        Wooden train	250
          Teddy bear	300
            Bicycle 	400
You should take the last box with materials and the first magic level value to craft a toy. Their 
multiplication calculates the total magic level. If the result equals one of the levels described 
in the table above, you craft the present and remove both materials and magic value. Otherwise:
    * If the product of the operation is a negative number, you should sum the values together, remove 
    them both from their positions, and add the result to the materials.
    * If the product doesn't equal one of the magic levels in the table and is a positive number, remove only the magic value and increase the material value by 15.
    * If the magic or material (or both) equals 0, remove it (or both) and continue crafting the presents.
Stop crafting presents when you run out of boxes of materials or magic level values.
Your task is considered done if you manage to craft either one of the pairs:
            a doll and a train
            a teddy bear and a bicycle
Input
The first line of input will represent the values of boxes with materials - integers, separated by a single space
On the second line, you will be given the magic values - integers again, separated by a single space
Output
On the first line - print whether you've succeeded in crafting the presents:
"The presents are crafted! Merry Christmas!"
"No presents this Christmas!"
On the next two lines print the materials and magic that are left, if there are any (otherwise skip the line)
"Materials left: {material_N}, {material_N-1}, … {material_1}"
"Magic left: {magicValue_1}, {magicValue_2}, … {magicValue_N}"
On the next lines print the presents you have crafted, ordered alphabetically in the format:
"{toy_name1}: {amount}
{toy_name2}: {amount}
...
{toy_nameN}: {amount}"
Constraints
All the materials' values will be integers in the range [1, 100]
Magic level values will be integers in the range [-10, 100]
In all cases, at least one present will be crafted
-------------------------------------- Example inputs ----------------------------------
Input
10 -5 20 15 -30 10
40 60 10 4 10 0	
Output
The presents are crafted! Merry Christmas!
Materials left: 20, -5, 10
Bicycle: 1
Teddy bear: 2	
-----------------------------------------------
Input
30 5 15 60 0 30
-15 10 5 -15 25	
Output
No presents this Christmas!
Materials left: 20, 30
Doll: 1
Teddy bear: 1
-----------------------------------------------
Input
30 10
15 10 5 0 10	
Output
No presents this Christmas!
Magic left: 5, 0, 10
Doll: 1
Teddy bear: 1	

"""
