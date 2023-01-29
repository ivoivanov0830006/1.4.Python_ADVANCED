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
