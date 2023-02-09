def students_credits(*args):
    result = {}
    total_credit = 0
    for course_info in args:
        current_credit = 0
        info = course_info.split("-")
        course, credit, max_points, current_points = info[0], int(info[1]), int(info[2]), int(info[3])
        current_credit += credit / (max_points / current_points)
        if course not in result:
            result[course] = 0
        result[course] = current_credit
        total_credit += current_credit

    if total_credit >= 240:
        print(f"Diyan gets a diploma with {total_credit} credits.")
    else:
        needed_credit = 240 - total_credit
        print(f"Diyan needs {needed_credit} credits more for a diploma.")

    sorted_result = [f"{key} - {value:.1f}" for key, value in sorted(result.items(), key=lambda x: (-x[1], x[0]))]
    return "\n".join(sorted_result)


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
