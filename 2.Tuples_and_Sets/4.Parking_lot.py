number_cars = int(input())
cars = set()

for _ in range(number_cars):
    direction, number = input().split(", ")
    if direction == "IN":
        cars.add(number)
    elif direction == "OUT":
        cars.discard(number)

if len(cars) > 0:
    print("\n".join(cars))
else:
    print("Parking Lot is Empty")


"""
------------------------------------- Problem to resolve ------------------------------

Write a program that:
  * Records a car number for every car that enters the parking lot
  * Removes a car number when the car leaves the parking lot
On the first line, you will receive the number of commands - N. On the following N lines, you will
receive the direction and car's number in the format:
      "{direction}, {car_number}". The direction could
only be "IN" or "OUT". Print the car numbers which are still in the parking lot. Keep in mind that all
car numbers must be unique. If the parking lot is empty, print:
      "Parking Lot is Empty"
Note: The order in which we print the result does not matter.
-------------------------------------- Example inputs ----------------------------------
Input	                            
10                                
IN, CA2844AA                      
IN, CA1234TA                      
OUT, CA2844AA                     
IN, CA9999TT
IN, CA2866HI
OUT, CA1234TA
IN, CA2844AA
OUT, CA2866HI
IN, CA9876HH
IN, CA2822UU
Output
CA2844AA
CA9999TT
CA2822UU
CA9876HH
--------------------------------------------------------------
Input
4                                 
IN, CA2844AA
IN, CA1234TA
OUT, CA2844AA
OUT, CA1234TA
Output
Parking Lot is Empty

"""
