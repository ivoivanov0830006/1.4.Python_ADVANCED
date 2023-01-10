from collections import deque

milligrams_caffeine = list([int(x) for x in input().split(", ")])
energy_drinks = deque([int(x) for x in input().split(", ")])

maximum_caffeine = 300
total_caffeine = 0

while energy_drinks:
    
    if len(milligrams_caffeine) == 0 or len(energy_drinks) == 0:
        break
        
    current_milligrams = milligrams_caffeine.pop()
    current_drink = energy_drinks.popleft()
    current_caffeine = current_milligrams * current_drink
    
    if current_caffeine <= maximum_caffeine:
        total_caffeine += current_caffeine
        maximum_caffeine -= current_caffeine
    else:
        energy_drinks.append(current_drink)
        if total_caffeine >= 30:
            total_caffeine -= 30
            maximum_caffeine += 30
        else:
            total_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(list(map(str, energy_drinks)))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
