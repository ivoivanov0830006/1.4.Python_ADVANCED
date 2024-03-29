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

         
"""
------------------------------------ Problem to resolve --------------------------------

You will be given two sequences of integers, representing bomb effects and bomb casings.
You need to start from the first bomb effect and try to mix it with the last bomb casing. If the sum 
of their values is equal to any of the materials in the table below – create the bomb corresponding 
to the value and remove both bomb materials. Otherwise, just decrease the value of the bomb casing by 5.
You need to stop combining when you have no more bomb effects or bomb casings, or you successfully
filled the bombs pouch.
Bombs:
    ⦁	Datura Bombs: 40
    ⦁	Cherry Bombs: 60
    ⦁	Smoke Decoy Bombs: 120
To fill the bomb pouch, Ezio needs three of each of the bomb types.
Input
    ⦁	On the first line, you will receive the integers representing the bomb effects, separated by ",".
    ⦁	On the second line, you will receive the integers representing the bomb casings, separated by ", ".
Output
    ⦁	On the first line, print:
    ⦁	if Ezio succeeded to fulfill the bomb pouch: "Bene! You have successfully filled the bomb pouch!"
    ⦁	if Ezio didn't succeed to fulfill the bomb pouch: "You don't have enough materials to fill the bomb pouch."
    ⦁	On the second line, print all bomb effects left:
    ⦁	If there are no bomb effects: "Bomb Effects: empty"
    ⦁	If there are effects: "Bomb Effects: {bombEffect1}, {bombEffect2}, (…)"
    ⦁	On the third line, print all bomb casings left:
    ⦁	If there are no bomb casings: "Bomb Casings: empty"
    ⦁	If there are casings: "Bomb Casings: {bombCasing1}, {bombCasing2}, (…)"
    ⦁	Then, you need to print all bombs and the count you have of them, ordered alphabetically:
    ⦁  	"Cherry Bombs: {count}"
    ⦁	"Datura Bombs: {count}"
    ⦁	"Smoke Decoy Bombs: {count}"
-------------------------------------- Example inputs ----------------------------------
Input	
5, 25, 25, 115
5, 15, 25, 35	
Output
You don't have enough materials to fill the bomb pouch.
Bomb Effects: empty
Bomb Casings: empty
Cherry Bombs: 0
Datura Bombs: 3
Smoke Decoy Bombs: 1
---------------------------------------------------------
Input
30, 40, 5, 55, 50, 100, 110, 35, 40, 35, 100, 80
20, 25, 20, 5, 20, 20, 70, 5, 35, 0, 10	Bene! 
Output
You have successfully filled the bomb pouch!
Bomb Effects: 100, 80
Bomb Casings: 20
Cherry Bombs: 3
Datura Bombs: 4
Smoke Decoy Bombs: 3

"""
