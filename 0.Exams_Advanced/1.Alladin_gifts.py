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
