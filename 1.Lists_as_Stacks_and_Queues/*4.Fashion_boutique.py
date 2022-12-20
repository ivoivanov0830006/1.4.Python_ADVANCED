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


# ------------------------------------- Another Solution -----------------------------
#
# clothes = list(map(int, input().split()))
# rack_capacity = int(input())
#
# rack_count = 1
# current_rack = 0
#
# for _ in range(len(clothes)):
#     if current_rack + clothes[-1] > rack_capacity:
#         rack_count += 1
#         current_rack = clothes.pop()
#     elif current_rack + clothes[-1] == rack_capacity:
#         current_rack = 0
#         clothes.pop()
#         if clothes:
#             rack_count += 1
#
#     else:
#         current_rack += clothes.pop()
#
# print(rack_count)
