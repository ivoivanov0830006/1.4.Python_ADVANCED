number_usernames = int(input())
unique_usernames = set()

for _ in range(number_usernames):
    current_name = input()
    unique_usernames.add(current_name)

print("\n".join(unique_usernames))
