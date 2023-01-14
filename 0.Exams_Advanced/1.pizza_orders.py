from collections import deque


pizza_orders = deque([int(x) for x in input().split(", ")])
employees = deque([int(x) for x in input().split(", ")])

total_pizzas = 0
completed = False

while True:
    if not pizza_orders:
        completed = True
        break
    if not employees:
        break
    first_order = pizza_orders.popleft()
    if 0 < first_order <= 10:
        last_employee = employees.pop()

        if first_order <= last_employee:
            total_pizzas += first_order
        else:
            rest_order = first_order - last_employee
            if employees:
                pizza_orders.appendleft(rest_order)
                total_pizzas += last_employee
            else:
                pizza_orders.appendleft(rest_order)

if completed:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    if employees:
        print(f"Employees: {', '.join(map(str, employees))}")

else:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, pizza_orders))}")
