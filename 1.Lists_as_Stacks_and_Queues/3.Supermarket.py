from collections import deque

people = deque()

while True:
    command = input()
    if command == "End":
        break
    if command == "Paid":
        while len(people):              # print("\n".join(people))
            print(people.popleft())     # people.clear()
    else:
        people.append(command)

print(f"{len(people)} people remaining.")


"""
------------------------------------- Problem to resolve ------------------------------

Tom is working at the supermarket, and he needs your help to keep track of his clients.
Write a program that reads lines of input consisting of a customer's name and adds it to the end of a
queue until "End" is received. If, in the meantime, you receive the command "Paid", you should print
each customer in the order they are served (from the first to the last one) and empty the queue.
When you receive "End", you should print the count of the remaining people in the queue in the format:
  "{count} people remaining.".
-------------------------------------- Example inputs ----------------------------------
Input	                        
George                        
Peter                         
William                       
Paid                          
Michael
Oscar
Olivia
Linda
End
Output
George
Peter
William
4 people remaining.
---------------------------------------------------
Input
Anna                          
Emma
Alexander
End
Output
3 people remaining.

"""
