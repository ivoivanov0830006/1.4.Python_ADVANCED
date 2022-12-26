number_cars = int(input())
cars = set()

for _ in range(number_cars):
    direction, number = input().split(", ")
    if direction == "IN":
        cars.add(number)
    elif direction == "OUT":
        cars.discard(number)

if len(cars) > 0:
    print("\n".join(cars))
else:
    print("Parking Lot is Empty")
