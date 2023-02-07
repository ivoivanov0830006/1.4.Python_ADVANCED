import os

while True:
    command, *info = input().split("-")

    if command == "Create":
        file = open(f"{info[0]}", "w")
        file.close()

    elif command == "Add":
        with open(f"{info[0]}", "a") as file:
            file.write(f"{info[1]}\n")

    elif command == "Replace":
        try:
            with open(f"{info[0]}", "r") as file:
                text = file.readlines()  # text = file.read()

            for i in range(len(text)):  # text = text.replace(info[1], info[2]) and without for loop
                text[i] = text[i].replace(info[1], info[2])

            with open(f"{info[0]}", "w") as file:
                file.write("".join(text))  # file.write(text)
        except FileNotFoundError:
            print("An error occurred!")

    elif command == "Delete":
        try:
            os.remove(f"{info[0]}")
        except FileNotFoundError:
            print("An error occurred!")

    elif command == "End":
        break
