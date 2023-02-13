def get_magic_triangle(rows):
    magic_triangle = [[1], [1, 1]]
    for row in range(2, rows):
        new_row = []
        for num in range(len(magic_triangle[row - 1])):
            if num + 1 <= len(magic_triangle[row - 1]) - 1:
                new_row.append(magic_triangle[row - 1][num] + magic_triangle[row - 1][num + 1])
            else:
                break
        magic_triangle.append([1, *new_row, 1])

    return magic_triangle


print(get_magic_triangle(5))
