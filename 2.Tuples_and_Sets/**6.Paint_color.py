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


"""
------------------------------------- Problem to resolve ------------------------------

Write a program that finds colors in a string. You will be given a string on a single line containing 
substrings (separated by a single space) from which you will be able to form the following colors: 
Main colors: "red", "yellow", "blue"
Secondary colors: "orange", "purple", "green"
To form a color, you should concatenate the first and the last substrings and check if you can get 
any of the above colors' names. If there is only one substring left, you should use it to do the same check.
You can only keep a secondary color if the two main colors needed for its creation could be formed 
from the given substrings:
            orange = red + yellow
            purple = red + blue
            green = yellow + blue
Note: You could find some of the main colors needed to keep a secondary color after it is found. 
When you form a color, remove both substrings. Otherwise, you should remove the last character of each 
substring and return them in the middle of the original string. If the string contains an odd number of 
substrings, you should put the substrings one position ahead.
For example, if you are given the string "re yellow bye" you could not form a color with the substring 
"re" and "bye", so you should remove the last character and return them in the middle of the string: 
"r by yellow".
In the end, print out the list with colors in the order in which they are found.
Input
Single line string
Output
The list with the collected colors
Constrains
You will not receive an empty string
Please consider only the colors mentioned above
There won't be any cases with repeating colors
-------------------------------------- Example inputs ----------------------------------
Input	
d yel blu e low redd	
Output
['yellow', 'blue', 'red']
-----------------------------------
Input	
r ue nge ora bl ed	
Output
['red', 'blue']
------------------------------------
Input
re ple blu pop e pur d	
Output
['red', 'purple', 'blue']

"""
