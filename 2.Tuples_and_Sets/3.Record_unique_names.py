number_names = int(input())
unique_names = set()

for _ in range(number_names):
    name = input()
    unique_names.add(name)

for person in unique_names:
    print(person)


"""
------------------------------------- Problem to resolve ------------------------------

Write a program, which will take a list of names and print only the unique names in the list.
The order in which we print the result does not matter.
-------------------------------------- Example inputs ----------------------------------
Input	            
8                 
Lee               
Joey              
Lee               
Joe               
Alan
Alan
Peter
Joey
Output
Alan
Joey
Lee
Joe
Peter
------------------------------------------------------
Input
7                 
Lyle              
Bruce             
Alice             
Easton            
Shawn
Alice
Shawn
Output
Easton
Lyle
Alice
Bruce
Shawn
-------------------------------------------------------
Input
6                 
Adam
Output
Adam
"""
