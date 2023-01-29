from collections import deque

children = deque(input().split())
kicked_child = int(input())

current_child = 1

while len(children) > 1:
    child = children.popleft()
    if current_child == kicked_child:
        print(f"Removed {child}")
        current_child = 1
    else:
        children.append(child)
        current_child += 1

last_child = children.popleft()
print(f"Last is {last_child}")


"""
------------------------------------- Another Solution -----------------------------

from collections import deque

children = deque(input().split())
kicked_child = int(input())

while len(children) > 1:
    children.rotate(-kicked_child)
    child = children.pop()
    print(f"Removed {child}")

last_child = children.popleft()
print(f"Last is {last_child}")


------------------------------------- Problem to resolve ------------------------------

Hot Potato is a game in which children form a circle and toss a hot potato. The counting starts with
the first kid. Every nth toss, the child holding the potato leaves the game. When a kid leaves the
game, it passes the potato to the next kid. It continues until there is only one kid left.
Create a program that simulates the game of Hot Potato. On the first line, you will receive kids'
names, separated by a single space. On the second line, you will receive the nth toss (integer) in
which a child leaves the game.
Print every kid who is removed from the circle in the format "Removed {kid}". In the end, print the
only kid left in the format "Last is {kid}".
-------------------------------------- Example inputs ----------------------------------
Input	                                    
Tracy Emily Daniel                        
2	                                        
Output
Removed Emily
Removed Tracy
Last is Daniel
--------------------------------------------------------
Input	
George Peter Michael William Thomas       
10
Output
Removed Thomas
Removed Peter
Removed Michael
Removed George
Last is William
---------------------------------------------------------
Input
George Peter Michael William Thomas       
1
Output
Removed George                                        
Removed Peter
Removed Michael
Removed William
Last is Thomas

"""

