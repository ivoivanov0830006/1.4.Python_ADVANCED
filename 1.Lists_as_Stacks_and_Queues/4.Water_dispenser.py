current_quantity = starting_quantity
queue = deque()

while True:
    current_name = input()
    if current_name == "Start":
        break
    queue.append(current_name)

while True:
    current_command = input()
    if current_command == "End":
        break
    command = current_command.split()
    action = command[0]
    if action == "refill":
        liters = int(command[1])
        current_quantity += liters
    else:
        liters = int(command[0])
        person = queue.popleft()
        if current_quantity >= liters:
            current_quantity -= liters
            print(f"{person} got water")
        else:
            print(f"{person} must wait")

print(f"{current_quantity} liters left")


"""
------------------------------------- Problem to resolve ------------------------------

Write a program that keeps track of people getting water from a dispenser and the amount of water
left at the end. On the first line, you will receive the starting quantity of water (integer) in a
dispenser. Then, on the following lines, you will be given the names of some people who want to get
water (each on a separate line) until you receive the command "Start". Add those people in a queue.
Finally, you will receive some commands until the command "End":
  * "{liters}" - litters (integer) that the current person in the queue wants to get. Check if there
    is enough water in the dispenser for that person. If there is enough water, print "{person_name}
    got water" and remove him/her from the queue. Otherwise, print "{person_name} must wait" and
    remove the person from the queue without reducing the water in the dispenser.
  * "refill {liters}" - add the given litters in the dispenser.
In the end, print how many liters of water have left in the format: "{left_liters} liters left".
-------------------------------------- Example inputs ----------------------------------
Input	            
2                 
Peter             
Amy               
Start
2
refill 1
1
End
Output
Peter got water
Amy got water
0 liters left
-----------------------------------
Input
10                
Peter             
George            
Amy               
Alice             
Start
2
3
3
3
End
Output
Peter got water
George got water
Amy got water
Alice must wait
2 liters left

"""
