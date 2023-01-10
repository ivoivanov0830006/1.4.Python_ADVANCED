from collections import deque

total_food = list(map(int, input().split(", ")))
total_stamina = deque(map(int, input().split(", ")))

peaks = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)
])

conquered_peaks = []
succeeded = False
day = 1

while True:
    if len(conquered_peaks) == 5:
        succeeded = True
        break
    if not total_stamina or not total_food or day > 7:
        break
    food = total_food.pop()
    stamina = total_stamina.popleft()
    energy = food + stamina
    peak = peaks.popleft()
    peak_name = peak[0]
    peak_energy = peak[1]
    if energy >= peak_energy:
        conquered_peaks.append(peak_name)
    else:
        peaks.appendleft(peak)
    day += 1

if succeeded:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    print('\n'.join(conquered_peaks))
