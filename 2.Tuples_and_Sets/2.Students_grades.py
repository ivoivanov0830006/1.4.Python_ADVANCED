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

    
# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that reads students' names and their grades and adds them to the student record.
# On the first line, you will receive the number of students – N. On the following N lines, you will be
# receiving a student's name and their grade.
# For each student print all his/her grades and finally his/her average grade, formatted to the second
# decimal point in the format:
#       "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
# The order in which we print the result does not matter.
# -------------------------------------- Example inputs ----------------------------------
# Input	                    Output
# 7                         Mark -> 5.50 2.50 3.46 (avg: 3.82)
# Peter 5.20                Peter -> 5.20 3.20 (avg: 4.20)
# Mark 5.50                 Alex -> 2.00 3.00 (avg: 2.50)
# Peter 3.20
# Mark 2.50
# Alex 2.00
# Mark 3.46
# Alex 3.00
# ---------------------------------------------------------------
# 4                         Ted -> 3.00 3.66 (avg: 3.33)
# Scott 4.50                Scott -> 4.50 5.00 (avg: 4.75)
# Ted 3.00
# Scott 5.00
# Ted 3.66
# ----------------------------------------------------------------
# 5                         Peter -> 4.40 (avg: 4.40)
# Lee 6.00                  Lee -> 6.00 5.50 6.00 (avg: 5.83)
# Lee 5.50                  Kenny -> 3.30 (avg: 3.30)
# Lee 6.00
# Peter 4.40
# Kenny 3.30
