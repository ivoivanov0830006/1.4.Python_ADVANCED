number_usernames = int(input())
unique_usernames = set()

for _ in range(number_usernames):
    current_name = input()
    unique_usernames.add(current_name)

print("\n".join(unique_usernames))


"""
------------------------------------- Another Solution -----------------------------

print(*{input() for _ in range(int(input()))}, sep="\n")


------------------------------------- Problem to resolve ------------------------------

Write a program that reads from the console a sequence of N usernames and keeps a collection only of the
unique ones. On the first line, you will receive an integer N. On the next N lines, you will receive a
username. Print the collection on the console (the order does not matter):
-------------------------------------- Example inputs ----------------------------------
Input	            
6                 
George            
George            
George
Peter
George
NiceGuy1234
Output
George
Peter
NiceGuy1234
----------------------------------
Input
10                
Peter             
Maria             
Peter             
George            
Steve
Maria
Alex
Peter
Steve
George
Output
Peter
Maria
George
Steve
Alex

"""

