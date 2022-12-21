number_students = int(input())
students = {}

for _ in range(number_students):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for data in students.items():
    all_grades = " ".join(f"{element:.2f}" for element in data[1])
    average = sum(data[1]) / len(data[1])
    print(f"{data[0]} -> {all_grades} (avg: {average:.2f})")
