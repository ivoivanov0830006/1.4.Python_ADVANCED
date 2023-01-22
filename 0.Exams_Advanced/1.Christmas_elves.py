from collections import deque

elves_energy = deque([int(x) for x in input().split()])
materials = list([int(x) for x in input().split()])

total_energy = 0
total_toys = 0
count = 0

while True:
    if not elves_energy or not materials:
        break
    current_elf_energy = elves_energy.popleft()
    if current_elf_energy < 5:
        continue
    current_material = materials.pop()
    count += 1
    # CREATIVE AND MAY BE CLUMSY---------------------
    if count % 3 == 0:
        if current_elf_energy >= current_material * 2:
            current_elf_energy -= (current_material * 2)
            if count % 5 == 0:
                elves_energy.append(current_elf_energy)
                total_energy += current_material * 2
            else:
                elves_energy.append(current_elf_energy + 1)
                total_toys += 2
                total_energy += current_material * 2
        else:
            materials.append(current_material)
            elves_energy.append(current_elf_energy * 2)
    # CLUMSY ----------------------------------------
    elif count % 5 == 0:
        if current_elf_energy >= current_material:
            current_elf_energy -= current_material
            elves_energy.append(current_elf_energy)
            total_energy += current_material
        else:
            materials.append(current_material)
            elves_energy.append(current_elf_energy * 2)
    # REGULAR ----------------------------------------
    else:
        if current_elf_energy >= current_material:
            current_elf_energy -= current_material
            elves_energy.append(current_elf_energy + 1)
            total_toys += 1
            total_energy += current_material
        else:
            materials.append(current_material)
            elves_energy.append(current_elf_energy * 2)

print(f"Toys: {total_toys}")
print(f"Energy: {total_energy}")
if elves_energy:
    print(f"Elves left: {', '.join(map(str, elves_energy))}")
if materials:
    print(f"Boxes left: {', '.join(map(str, materials))}")
