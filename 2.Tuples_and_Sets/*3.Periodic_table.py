number_elements = int(input())
unique_elements = set()

for _ in range(number_elements):
    compound = set(input().split())
    unique_elements = unique_elements.union(compound)

print("\n".join(unique_elements))
