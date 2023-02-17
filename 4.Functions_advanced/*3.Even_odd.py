def even_odd(*args):
    command = args[-1]  # can't be popped because it's tuple
    if command == "even":
        return [n for n in args[:-1] if n % 2 == 0]
    elif command == "odd":
        return [n for n in args[:-1] if n % 2 == 1]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))


"""
------------------------------------- Another Solution ---------------------------------

def even_odd(*args):
    command = args[-1]
    result = []

    for n in args[:-1]:
        if int(n) % 2 == 0 and command == "even":
            result.append(n)
        elif int(n) % 2 == 1 and command == "odd":
            result.append(n)

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))


------------------------------------ Problem to resolve --------------------------------

Create a function called even_odd() that can receive a different quantity of numbers and a direction at the 
end. The direction can be "even" or "odd". Filter the numbers depending on the direction and return them in a 
list. Submit only the function in the judge system.
-------------------------------------- Example inputs ----------------------------------
print(even_odd(1, 2, 3, 4, 5, 6, "even"))	[2, 4, 6]
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))	[1, 3, 5, 7, 9]

"""

