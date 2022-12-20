sequence = input().split()
clothes = []

rack_capacity = int(input())

for i in range(len(sequence)):
    clothes.append(sequence[i])

rack_count = 1
current_rack = 0

while len(clothes) > 0:
    current_clothes = int(clothes.pop())
    current_rack += current_clothes
    if current_rack == rack_capacity:
        current_rack = 0
        rack_count += 1
    elif current_rack > rack_capacity:
        clothes.append(current_clothes)
        current_rack = 0
        rack_count += 1
        current_rack += current_clothes
        clothes.pop()

print(rack_count)
