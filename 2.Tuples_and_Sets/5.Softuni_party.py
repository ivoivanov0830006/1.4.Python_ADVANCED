number_guests = int(input())

vip = set()
regular = set()

for _ in range(number_guests):
    guest = input()
    guest_type = guest[0]
    if guest_type.isdigit():
        vip.add(guest)
    else:
        regular.add(guest)

while True:
    command = input()
    if command == "END":
        break
    guest_type = command[0]
    if guest_type.isdigit():
        vip.discard(command)
    else:
        regular.discard(command)

print(len(vip.union(regular)))
print("\n".join(sorted(vip)))
print("\n".join(sorted(regular)))
