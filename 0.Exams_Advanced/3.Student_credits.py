def students_credits(*args):
    exams_result = {}
    total_credit = 0
    for course_info in args:
        current_credit = 0
        info = course_info.split("-")
        course, credit, max_points, current_points = info[0], int(info[1]), int(info[2]), int(info[3])
        current_credit += credit * (current_points / max_points)
        if course not in exams_result:
            exams_result[course] = 0
        exams_result[course] = current_credit
        total_credit += current_credit

    if total_credit >= 240:
        final_strings = f"Diyan gets a diploma with {total_credit:.1f} credits.\n"
    else:
        needed_credit = 240 - total_credit
        final_strings = f"Diyan needs {needed_credit:.1f} credits more for a diploma.\n"

    sorted_result = sorted(exams_result.items(), key=lambda x: (-x[1], x[0]))

    for key, value in sorted_result:
        final_strings += f"{key} - {float(value):.1f}\n"

    return final_strings


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)


"""
------------------------------------- Another Solution ---------------------------------

def students_credits(*args):
    diyan_total_credits = 0
    diyan_credits_info = dict()
    final_strings = []

    for info in args:
        course_name, course_credits, max_test_points, dian_points = info.split("-")
        current_percentage = int(dian_points) / int(max_test_points)
        diyan_current_credits = current_percentage * int(course_credits)
        diyan_total_credits += diyan_current_credits
        diyan_credits_info[course_name] = diyan_current_credits

    if diyan_total_credits >= 240:
        final_strings.append(f"Diyan gets a diploma with {diyan_total_credits:.1f} credits.")
    else:
        final_strings.append(f"Diyan needs {240-diyan_total_credits:.1f} credits more for a diploma.")
    sorted_dian_points_info = sorted(diyan_credits_info.items(), key=lambda a: -a[1])

    for course, points in sorted_dian_points_info:
        final_strings.append(f"{course} - {float(points):.1f}")

    return "\n".join(final_strings)
    
    
------------------------------------ Problem to resolve --------------------------------

Write a function students_credits which receives a different number of strings. 
Each string will be in the format: 
    "{course name}-{credits}-{max test points}-{diyan's points}".
Your task is to calculate the credits Diyan manages to get from all courses. The credits he gets 
are proportional to his points on the test. For example, if the credits of a course are 25, and 
Diyan achieved to get 50 of 100 max test points, he will get 12.5 credits for the course.
Also, you need to keep track of each course and Diyan's credits and sort them in descending order 
by Diyan's credits. Finally, return a string on multiple lines containing:
Diyan's achievement message:
If the sum of all of Diyan's credits is more than or equal to 240, return: 
    "Diyan gets a diploma with {total credits} credits."
Otherwise, return: 
    "Diyan needs {credits needed} credits more for a diploma."
Information for each course and Diyan's credits:
    "{course name} - {diyan's credits}"
Note: Each course data should be on a new line.
All credits must be formatted to the first decimal place.
Note: Submit only the function in the judge system
Input
There will be no input, just any number of strings with courses data passed to your function
Output
The function should return a string in the format described above:
Constraints:
There will always be at least one course.
There will not be two or more courses with the same name.
All points and all credits will be whole numbers
-------------------------------------- Example inputs ----------------------------------
Test Code	
print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)	
Output
Diyan needs 198.0 credits more for a diploma.
Algorithms - 24.5
Computer Science - 10.0
Basic Algebra - 7.5
------------------------------------------------
Test Code
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)	
Output
Diyan gets a diploma with 243.3 credits.
Game Engine Development - 49.0
Algorithms Advanced - 45.0
Discrete Maths - 36.0
C++ Development - 24.3
Mobile Development - 22.5
AI Development - 20.0
QA - 20.0
Python Development - 15.0
JavaScript Development - 11.5
------------------------------------------------
Test Code
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
Output
Diyan needs 184.2 credits more for a diploma.
C++ Development - 24.3
Python Development - 15.0
JavaScript Development - 11.5
Java Development - 5.0

"""
