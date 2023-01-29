from collections import deque

green_window = int(input())
free_window = int(input())
total_cars = 0
cars = deque()
crashed = False

command = input()

while command != "END":
    if command != "green":
        cars.append(command)
    else:
        current_green = green_window
        while current_green > 0 and cars:
            car = cars.popleft()
            time = current_green + free_window
            if len(car) > time:
                print("A crash happened!")
                print(f"{car} was hit at {car[time]}.")
                crashed = True
                break
            current_green -= len(car)
            total_cars += 1
        if crashed:
            break
    if crashed:
        break
    command = input()

if not crashed:
    print("Everyone is safe.")
    print(f"{total_cars} total cars passed the crossroads.")
