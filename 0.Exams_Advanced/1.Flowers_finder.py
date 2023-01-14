from collections import deque

vowels = deque(input().split(" "))
consonants = deque(input().split(" "))

flowers = {"rose": "rose",
           "tulip": "tulip",
           "lotus": "lotus",
           "daffodil": "daffodil"
}

found = False
found_flower = ""

while True:
    if len(vowels) == 0 or len(consonants) == 0:
        break
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for flower in flowers.keys():
        flowers[flower] = flowers[flower].replace(vowel, "")
        flowers[flower] = flowers[flower].replace(consonant, "")
        if flowers[flower] == "":
            found_flower = flower
            found = True
            break
    if found:
        break
if found:
    print(f"Word found: {found_flower}")
else:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
