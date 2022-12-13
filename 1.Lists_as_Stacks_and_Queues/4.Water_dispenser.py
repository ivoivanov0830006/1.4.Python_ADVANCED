current_quantity = starting_quantity
queue = deque()

while True:
    current_name = input()
    if current_name == "Start":
        break
    queue.append(current_name)

while True:
    current_command = input()
    if current_command == "End":
        break
    command = current_command.split()
    action = command[0]
    if action == "refill":
        liters = int(command[1])
        current_quantity += liters
    else:
        liters = int(command[0])
        person = queue.popleft()
        if current_quantity >= liters:
            current_quantity -= liters
            print(f"{person} got water")
        else:
            print(f"{person} must wait")

print(f"{current_quantity} liters left")
