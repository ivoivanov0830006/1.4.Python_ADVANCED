n, m = list(map(int, input().split()))

n_numbers = set()
m_numbers = set()

unique_numbers = set()

for _ in range(n):
    current_number = input()
    n_numbers.add(current_number)
for _ in range(m):
n, m = list(map(int, input().split()))

n_numbers = set()
m_numbers = set()

unique_numbers = set()

for _ in range(n):
    current_number = input()
    n_numbers.add(current_number)
for _ in range(m):
    current_number = input()
    m_numbers.add(current_number)


unique_numbers = n_numbers.intersection(m_numbers)
print("\n".join(unique_numbers))


"""
------------------------------------- Another Solution -----------------------------

n, m = [int(x) for x in input().split()]

n_numbers = set((input()) for _ in range(n))
m_numbers = set((input()) for _ in range(m))

unique_numbers = set(n_numbers.intersection(m_numbers))
print("\n".join(unique_numbers))

------------------------------------- Problem to resolve ------------------------------

Write a program that prints a set of elements. On the first line, you will receive two numbers - n and m,
separated by a single space - representing the lengths of two separate sets. On the next n + m lines,
you will receive n numbers, which are the numbers in the first set, and m numbers, which are in the
second set. Find all the unique elements that appear in both and print them on separate lines
(the order does not matter).
For example:
Set with length n = 4: {1, 3, 5, 7}
Set with length m = 3: {3, 4, 5}
Set that contains all the elements that repeat in both sets -> {3, 5}
-------------------------------------- Example inputs ----------------------------------
Input	        
4 3           
1             
3
5
7
3
4
Output
3
5
-----------------------
Input
5             
2 2
1
3
1
5
Output
1
"""

