from collections import deque

seats_sequence = input().split(", ")
first_sequence = deque(map(int, input().split(", ")))
second_sequence = deque(map(int, input().split(", ")))

taken_seats = []
rotations_count = 0

while True:
    
    if len(taken_seats) == 3 or rotations_count == 10:
        break
        
    first_number = first_sequence.popleft()
    last_number = second_sequence.pop()
    current_sum = first_number + last_number
    ascii_character = chr(current_sum)
    seat_combination_1 = f"{first_number}{ascii_character}"
    seat_combination_2 = f"{last_number}{ascii_character}"
    
    for seat in [seat_combination_1, seat_combination_2]:
        if seat in seats_sequence:
            taken_seats.append(seat)
            seats_sequence.remove(seat)
        if seat in taken_seats:
            break
    else:
        first_sequence.append(first_number)
        second_sequence.appendleft(last_number)

    rotations_count += 1

print(f'Seat matches: {", ".join(taken_seats)}')
print(f'Rotations count: {rotations_count}')
