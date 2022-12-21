sequence = input().split()
all_elements = []

for element in sequence:
    count = sequence.count(element)
    number = float(element)
    if element not in all_elements:
        all_elements.append(element)
        print(f"{number:.1f} - {count} times")
