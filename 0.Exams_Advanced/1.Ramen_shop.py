from collections import deque

bowls = deque([int(x) for x in input().split(", ")])
customers = deque([int(x) for x in input().split(", ")])

all_served = False
out_of_ramen = False

while True:
    if len(customers) == 0:
        all_served = True
        break
    if len(bowls) == 0:
        out_of_ramen = True
        break
    last_bowl = bowls.pop()
    first_customer = customers.popleft()
    if last_bowl > first_customer:
        last_bowl -= first_customer
        bowls.append(last_bowl)
    elif last_bowl < first_customer:
        first_customer -= last_bowl
        customers.appendleft(first_customer)

if all_served:
    print("Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls)}")

if out_of_ramen:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join(str(x) for x in customers)}")
