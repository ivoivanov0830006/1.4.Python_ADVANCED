from collections import deque


def flights(*args):
    final_flights = {}
    all_flights = deque(args)
    while all_flights:
        city = all_flights.popleft()
        if city == "Finish":
            break
        if city not in final_flights.keys():
            final_flights[city] = 0
        passengers = all_flights.popleft()
        final_flights[city] += passengers

    return final_flights


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
