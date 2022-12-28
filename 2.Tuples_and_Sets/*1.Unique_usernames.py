number_usernames = int(input())
unique_usernames = set()

for _ in range(number_usernames):
    current_name = input()
    unique_usernames.add(current_name)

print("\n".join(unique_usernames))


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that reads from the console a sequence of N usernames and keeps a collection only of the
# unique ones. On the first line, you will receive an integer N. On the next N lines, you will receive a
# username. Print the collection on the console (the order does not matter):
# -------------------------------------- Example inputs ----------------------------------
# Input	            Output
# 6                 George
# George            Peter
# George            NiceGuy1234
# George
# Peter
# George
# NiceGuy1234
# ----------------------------------
# 10                Peter
# Peter             Maria
# Maria             George
# Peter             Steve
# George            Alex
# Steve
# Maria
# Alex
# Peter
# Steve
# George
