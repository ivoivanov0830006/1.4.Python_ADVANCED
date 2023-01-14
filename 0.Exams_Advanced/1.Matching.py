from collections import deque

males = deque([int(x) for x in input().split(" ")])
females = deque([int(x) for x in input().split(" ")])

matches = 0

while True:
    if not males or not females:
        break
    first_female = females.popleft()
    last_male = males.pop()

    # INVALID -------------------------------------------
    if first_female <= 0:
        males.append(last_male)
        continue
    elif last_male <= 0:
        females.appendleft(first_female)
        continue

    # SPECIAL -------------------------------------------
    elif first_female % 25 == 0:
        next_female = females.popleft()
        males.append(last_male)
        continue
    elif last_male % 25 == 0:
        next_male = males.pop()
        females.appendleft(first_female)
        continue

    # MATCH ---------------------------------------------
    elif last_male == first_female:
        matches += 1

    # NO MATCH ------------------------------------------
    else:
        last_male -= 2
        males.append(last_male)

print(f"Matches: {matches}")
if males:
    males = reversed(males)
    print(f"Males left: {', '.join(map(str, males))}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print("Females left: none")
