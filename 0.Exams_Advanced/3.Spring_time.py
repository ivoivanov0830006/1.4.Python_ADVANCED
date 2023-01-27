def start_spring(**kwargs):
    result = ""
    spring_objects = {}
    for value, key in kwargs.items():
        if key not in spring_objects:
            spring_objects[key] = []
        spring_objects[key].append(value)

    sorted_spring_objects = sorted(spring_objects.items(), key=lambda x: (-len(x[1]), x[0]))
    for item in spring_objects.items():
        type_object = item[0]
        name_objects = item[1]
        result += f"{type_object}\n"
        for obj in name_objects:
            result += f"-{obj}\n"
    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))



"""
------------------------------------ Problem to resolve --------------------------------

Write a function called start_spring which will receive a different number of keyword arguments.
Each keyword holds a key with a name of the spring object (string), and each value holds its type (string). 
For example, dahlia="flower", shrikes="bird", dogwood="tree".
The function should sort the given spring objects in collections by their type:
The collections sorted by their number of elements in descending order. If two or more collections have 
the same number of elements in them, return them in ascending order (alphabetically) by the type's name. 
Each collection's elements should be sorted in ascending order (alphabetically) by the object's name.
Note: Submit only the function in the judge system
Input
There will be no input. Just parameters passed to your function.
Output
Return the result, sorted as described above in the format:
    "{type_one}:
    -{spring_object_of_this_type_one}
    -{spring_object_of_this_type_two}
    …
    -{spring_object_of_this_type_N}
    {type_two}:
    …
    {type_N}:
    …
    -{last_spring_object_of_typeN}"
