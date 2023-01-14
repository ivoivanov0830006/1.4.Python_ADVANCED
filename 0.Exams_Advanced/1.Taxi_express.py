from collections import deque

customers = deque([int(x) for x in input().split(", ")])
taxis = deque([int(x) for x in input().split(", ")])

total_time = 0

while True:
    if not customers or not taxis:
        break
    first_customer = customers.popleft()
    last_taxi = taxis.pop()

    if last_taxi >= first_customer:
        total_time += first_customer
    else:
        customers.appendleft(first_customer)

if customers:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(map(str, customers))}")
else:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
