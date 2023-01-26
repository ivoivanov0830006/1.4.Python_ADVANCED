from collections import deque

total_food = list(map(int, input().split(", ")))
total_stamina = deque(map(int, input().split(", ")))

peaks = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)
])

conquered_peaks = []
succeeded = False
day = 1

while True:
    if len(conquered_peaks) == 5:
        succeeded = True
        break
    if not total_stamina or not total_food or day > 7:
        break
    food = total_food.pop()
    stamina = total_stamina.popleft()
    energy = food + stamina
    peak = peaks.popleft()
    peak_name = peak[0]
    peak_energy = peak[1]
    if energy >= peak_energy:
        conquered_peaks.append(peak_name)
    else:
        peaks.appendleft(peak)
    day += 1

if succeeded:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    print('\n'.join(conquered_peaks))

    
"""
------------------------------------ Problem to resolve --------------------------------

You will have to keep information for all the conquered peaks if any.
Every day, Alex will use one portion of his daily food supplies and will exhaust one of his daily stamina.
First, you will be given a sequence of numbers, representing the quantities of the daily portions of food 
supplies in his backpack.
Afterward, you will be given another sequence of numbers, representing the quantities of the daily stamina he 
will have at his disposal for the next seven days.
You have to sum the quantity of the last daily food portion with the quantity of the first daily stamina. 
He will start climbing from the first peak in the table below to the last one.
    ⦁	If the sum is equal to or greater than the corresponding Mountain Peak’s Difficulty level from the table 
        below, it means that the peak is conquered. In this case, you should remove both quantities from the 
        sequences and continue with the next ones towards the next peak.
    ⦁	If the sum is less than the corresponding Mountain Peak’s Difficulty level from the table below, the peak 
        remains unconquered. You should remove both quantities from the sequences. Alex will have to sleep in his tent. 
        On the next day, he will try the same peak once again.

                    Mountain Peaks	    Difficulty level
                            Vihren	    80
                            Kutelo	    90
                    Banski Suhodol	    100
                          Polezhan	    60
                         Kamenitza	    70

Alex will try to conquer as many peaks as he can in seven days. 
If he manages to climb all the peaks, the journey ends and the output is printed on the Console.
Finally, print on the Console all the conquered peaks(in the order of climbing).
    ⦁	On the first line – print whether Alex managed to reach his goal and climb all the peaks in his list:
    ⦁	If he managed to conquer all: "Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK"
    ⦁	If he didn't manage to climb all of the peaks: "Alex failed! He has to organize his journey better 
    next time -> @PIRINWINS"
    ⦁	Then, in either case, you need to print all the conquered peaks (in the order of climbing) if any:
        "Conquered peaks:
         {peak1}
         {peak2}
          …
         {peakn}"
    ⦁	If there are no concurred peaks, do NOT print this message.
-------------------------------------- Example inputs ----------------------------------
Input	
40, 40, 40, 40, 40, 40, 40
40, 50, 60, 20, 30, 5, 2	
Output
Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK
Conquered peaks:
Vihren
Kutelo
Banski Suhodol
Polezhan
Kamenitza
------------------------------------------------------------------------------
Input	
10, 20, 34, 26, 12, 10, 45
30, 28, 17, 17, 13, 10, 10	
Output
Alex failed! He has to organize his journey better next time -> @PIRINWINS


"""
