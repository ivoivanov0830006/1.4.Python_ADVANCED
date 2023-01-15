from collections import deque

effects = deque([int(x) for x in input().split(", ")])
casings = deque([int(x) for x in input().split(", ")])

pouch = {"Datura Bombs": 0,
         "Cherry Bombs": 0,
         "Smoke Decoy Bombs": 0
}

succeeded = False

while True:
    if not effects or not casings:
        break
    if pouch["Datura Bombs"] >= 3 and \
            pouch["Cherry Bombs"] >= 3 and \
            pouch["Smoke Decoy Bombs"] >= 3:
        succeeded = True
        break
    first_effect = effects.popleft()
    last_casing = casings.pop()
    total_sum = first_effect + last_casing

    if total_sum == 40:
        pouch["Datura Bombs"] += 1
    elif total_sum == 60:
        pouch["Cherry Bombs"] += 1
    elif total_sum == 120:
        pouch["Smoke Decoy Bombs"] += 1
    else:
        effects.appendleft(first_effect)
        last_casing -= 5
        casings.append(last_casing)


if succeeded:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if effects:
    print(f"Bomb Effects: {', '.join(map(str, effects))}")
else:
    print("Bomb Effects: empty")
if casings:
    print(f"Bomb Casings: {', '.join(map(str, casings))}")
else:
    print("Bomb Casings: empty")
for key, value in sorted(pouch.items(), key=lambda x: x[0]):
    print(f"{key}: {value}")
