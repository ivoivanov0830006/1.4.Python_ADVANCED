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

    
"""
------------------------------------- Problem to resolve ------------------------------

First, you will be given two sequences of integers representing chocolates and cups of milk.
You have to start from the last chocolate and try to match it with the first cup of milk. 
If their values are equal, you should make a milkshake and remove both ingredients. 
Otherwise, you should move the cup of milk at the end of the sequence and decrease the value of 
the chocolate by 5 without moving it from its position.
If any of the values are equal to or below 0, you should remove them from the records right before 
mixing them with the other ingredient.
When you successfully prepare 5 chocolate milkshakes, or you have no more chocolate or cups of milk 
left, you need to stop making chocolate milkshakes.
Input
On the first line of input, you will receive the integers representing the chocolate, separated by  ", ". 
On the second line of input, you will receive the integers representing the cups of milk, separated by ", ".
Output
On the first line, print:
If you successfully made 5 milkshakes: "Great! You made all the chocolate milkshakes needed!"
Otherwise: "Not enough milkshakes."
On the second line - print:
If there are chocolates left: "Chocolate: {chocolate1}, {chocolate2}, (…)"
Otherwise: "Chocolate: empty"
On the third line - print:
If there are cups of milk left: "Milk: {milk1}, {milk2}, {milk3}, (…)"
Otherwise: "Milk: empty"
Constraints
All given args will be valid integers in the range [-100 … 100].
-------------------------------------- Example inputs ----------------------------------
Input	Output
20, 24, -5, 17, 22, 60, 26
26, 60, 22, 17, 24, 10, 55	
Output
Great! You made all the chocolate milkshakes needed!
Chocolate: 20
Milk: 10, 55
--------------------------------------------------------
Input	
-10, -2, -30, 10
-5	Not enough milkshakes.
Chocolate: -10, -2, -30, 10
Milk: empty
2, 3, 3, 7, 2
2, 7, 3, 3, 2, 14, 6	
Output
Great! You made all the chocolate milkshakes needed!
Chocolate: empty
Milk: 14, 6

"""
