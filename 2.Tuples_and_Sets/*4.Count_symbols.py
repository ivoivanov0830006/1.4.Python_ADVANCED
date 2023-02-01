text = input()

unique_chars = {}

for char in text:
    if char not in unique_chars:
        unique_chars[char] = 0
    unique_chars[char] += 1

# for key, value in sorted(unique_cars.items()):
for key, value in sorted(unique_chars.items(), key=lambda x: x[0]):
    print(f"{key}: {value} time/s")


"""
------------------------------------- Another Solution -----------------------------

occurrences = {}

for letter in input():
    occurrences[letter] = occurrences.get(letter, 0) + 1

for key, value in sorted(occurrences.items()):
    print(f"{key}: {value} time/s")
