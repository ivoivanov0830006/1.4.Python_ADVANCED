from collections import deque

all_colors = ["red", "yellow", "blue", "orange", "purple", "green"]
secondary_colors = {
    'orange': ('red', 'yellow'),
    'purple': ('red', 'blue'),
    'green': ('yellow', 'blue')
}

final_colors = []
input_string = deque(input().split())

while input_string:

    right = ""
    if len(input_string) > 1:
        right = input_string.pop()
    left = input_string.popleft()

    first_combination = left + right
    second_combination = right + left

    for searched_color in (first_combination, second_combination):
        if searched_color in all_colors:
            final_colors.append(searched_color)
            break
    else:
        left = left[:-1]
        right = right[:-1]
        middle_of_string = len(input_string) // 2
        for item in (left, right):
            if item:
                input_string.insert(middle_of_string, item)

for sec_color, needed_colors in secondary_colors.items():
    # if any(x not in final_colors and sec_color in final_colors for x in needed_colors):
    if sec_color in final_colors:
        for needed_color in needed_colors:
            if needed_color not in final_colors:
                final_colors.remove(sec_color)


print(final_colors)
