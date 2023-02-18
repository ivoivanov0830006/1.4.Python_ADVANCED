from collections import deque

textile = deque(map(int, input().split()))
medicament = list(map(int, input().split()))

inventory = {"Patch": 0,
             "Bandage": 0,
             "MedKit": 0
             }

while True:
    if not textile or not medicament:
        break
    first_textile = textile.popleft()
    last_medicament = medicament.pop()
    total_sum = first_textile + last_medicament

    if total_sum == 30:
        inventory["Patch"] += 1
    elif total_sum == 40:
        inventory["Bandage"] += 1
    elif total_sum >= 100:
        inventory["MedKit"] += 1
        if total_sum > 100:
            rest = total_sum - 100
            next_medicament = medicament.pop()
            next_medicament += rest
            medicament.append(next_medicament)

    else:
        medicament.append(last_medicament + 10)

if not textile and not medicament:
    print("Textiles and medicaments are both empty.")

elif not textile:
    print("Textiles are empty.")

elif not medicament:
    print("Medicaments are empty.")

sorted_inventory = sorted(inventory.items(), key=lambda x: (-x[1], x[0]))
for key, value in sorted_inventory:
    if value > 0:
        print(f"{key} - {value}")

if medicament:
    medicament = reversed(medicament)
    print(f"Medicaments left: {', '.join(map(str, medicament))}")

if textile:
    print(f"Textiles left: {', '.join(map(str, textile))}")
