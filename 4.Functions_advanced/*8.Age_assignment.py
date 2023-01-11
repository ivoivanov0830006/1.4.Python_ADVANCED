def age_assignment(*args, **kwargs):
    result = {}

    for name in args:
        first_letter = name[0]
        age = kwargs[first_letter]
        result[name] = age

    sorted_result = [f"{key} is {value} years old." for key, value in sorted(result.items(), key=lambda x: x[0])]
    return "\n".join(sorted_result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))


"""
------------------------------------ Problem to resolve --------------------------------

Create a function called age_assignment() that receives a different number of names and a different number 
of key-value pairs. The key will be a single letter (the first letter of each name) and the value - a number
(age). Find its first letter in the key-value pairs for each name and assign the age to the person's name.
Then, sort the names in ascending order (alphabetically) and return the information for each person on a 
new line in the format: 
    "{name} is {age} years old."
-------------------------------------- Example inputs ----------------------------------
Test Code	
print(age_assignment("Peter", "George", G=26, P=19))	
Output
George is 26 years old.
Peter is 19 years old.
-------------------------------------------------------
Test Code	
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))	Amy is 22 years old.
Output
Bill is 61 years old.
Willy is 36 years old.

"""
