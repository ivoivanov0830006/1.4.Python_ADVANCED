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
