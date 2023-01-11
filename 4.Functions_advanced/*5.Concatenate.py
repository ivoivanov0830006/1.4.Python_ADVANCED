def concatenate(*args, **kwargs):
    text = "".join(args)

    for key, value in kwargs.items():
        text = text.replace(key, value)

    return text


print(concatenate("Soft", "UNI", " ", "Is", " ", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))


"""
------------------------------------ Problem to resolve --------------------------------

Write a concatenate() function that receives some strings as arguments and some named arguments (the key 
will be a string, and the value will be another string).
First, you should concatenate all arguments successively. Next, take each key successively, and if it is 
present in the resulted string, change all matching parts with the key's value. In the end, return the 
final string.
-------------------------------------- Example inputs ----------------------------------
Test Code	
print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
Output
SoftUniIsGreat!
---------------------------------------------------------------------------------
Test Code
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))	
Output
I Love Python

"""
