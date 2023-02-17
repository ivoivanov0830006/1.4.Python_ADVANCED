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
