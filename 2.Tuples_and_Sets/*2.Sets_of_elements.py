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
