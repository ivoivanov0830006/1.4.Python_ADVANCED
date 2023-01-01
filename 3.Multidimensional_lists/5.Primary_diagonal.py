def get_primary_diagonal(current_matrix):
    return sum(current_matrix[i][i] for i in range(len(current_matrix)))
    # len(matrix) because rows = columns


n = int(input())

matrix = []
for _ in range(n):
    row = [int(x) for x in input().split(" ")]
    matrix.append(row)

print(get_primary_diagonal(matrix))


"""
------------------------------------- Another Solution ---------------------------------

# def get_primary_diagonal(current_matrix):
#     the_sum = 0
#     for i in range(len(matrix)):
#         the_sum += matrix[i][i]
#     return the_sum
#
#
# n = int(input())
#
# matrix = []
# for _ in range(n):
#     row = [int(x) for x in input().split(" ")]
#     matrix.append(row)
#
# print(get_primary_diagonal(matrix))

------------------------------------ Problem to resolve --------------------------------


-------------------------------------- Example inputs ----------------------------------
Input	
3
11 2 4
4 5 6
10 8 -12	
Output
4	
-------------------
Input
3
1 2 3
4 5 6
7 8 9
Output
15

"""
