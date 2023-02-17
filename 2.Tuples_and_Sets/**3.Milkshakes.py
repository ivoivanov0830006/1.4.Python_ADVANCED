from collections import deque

chocolate = list([int(x) for x in input().split(", ")])
milk = deque([int(x) for x in input().split(", ")])

milkshakes = 0
succeeded = False

while True:
    if not chocolate or not milk:
        break
    current_chocolate = chocolate.pop()
    current_milk = milk.popleft()
    if current_chocolate <= 0 and current_milk <= 0:
        continue
    elif current_chocolate <= 0:
        milk.appendleft(current_milk)
        continue
    if current_milk <= 0:
        chocolate.append(current_chocolate)
        continue
    if current_milk == current_chocolate:
        milkshakes += 1
        if milkshakes == 5:
            succeeded = True
            break
    else:
        milk.append(current_milk)
        current_chocolate -= 5
        chocolate.append(current_chocolate)

if succeeded:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate:
    print(f"Chocolate: {', '.join(map(str, chocolate))}")
else:
    print("Chocolate: empty")
if milk:
    print(f"Milk: {', '.join(map(str, milk))}")
else:
    print("Milk: empty")
