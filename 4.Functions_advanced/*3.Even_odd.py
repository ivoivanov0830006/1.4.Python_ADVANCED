def even_odd(*args):
    command = args[-1]
    checking = 0 if command == "even" else 1
    result = []
    for idx in range(len(args) - 1):
        number = args[idx]
        if number % 2 == checking:
            result.append(number)

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))


"""
------------------------------------- Another Solution ---------------------------------

def even_odd(*args):
    result = []
    if args[-1] == "even":
        result = [x for x in args[:len(args) - 1] if x % 2 == 0]
    elif args[-1] == "odd":
        result = [x for x in args[:len(args) - 1] if x % 2 != 0]
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))


------------------------------------ Problem to resolve --------------------------------

Create a function called even_odd() that can receive a different quantity of numbers and a command at the 
end. The command can be "even" or "odd". Filter the numbers depending on the command and return them in a 
list. Submit only the function in the judge system.
-------------------------------------- Example inputs ----------------------------------
print(even_odd(1, 2, 3, 4, 5, 6, "even"))	[2, 4, 6]
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))	[1, 3, 5, 7, 9]

"""
