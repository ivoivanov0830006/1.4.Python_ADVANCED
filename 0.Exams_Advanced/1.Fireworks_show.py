from collections import deque

effects = deque([int(x) for x in input().split(", ")])
power = deque([int(x) for x in input().split(", ")])

fireworks = {"Palm Fireworks": 0,
             "Willow Fireworks": 0,
             "Crossette Fireworks": 0
}
succeeded = False

while True:
    if fireworks["Palm Fireworks"] >= 3 and \
            fireworks["Willow Fireworks"] >= 3 and \
            fireworks["Crossette Fireworks"] >= 3:
        succeeded = True
        break
    if not effects or not power:
        break
    first_effect = effects.popleft()
    if first_effect <= 0:
        continue
    last_power = power.pop()
    if last_power <= 0:
        effects.appendleft(first_effect)
        continue
    total_sum = first_effect + last_power
    if total_sum % 3 == 0 and total_sum % 5 == 0:
        fireworks["Crossette Fireworks"] += 1
    elif total_sum % 3 == 0:
        fireworks["Palm Fireworks"] += 1
    elif total_sum % 5 == 0:
        fireworks["Willow Fireworks"] += 1
    else:
        first_effect -= 1
        effects.append(first_effect)
        power.append(last_power)

if succeeded:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join(map(str, effects))}")
if power:
    print(f"Explosive Power left: {', '.join(map(str, power))}")

for key, value in fireworks.items():
    print(f"{key}: {value}")
