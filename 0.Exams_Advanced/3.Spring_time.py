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
