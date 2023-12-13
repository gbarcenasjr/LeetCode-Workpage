matr = [[0, 0, 1, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0]]


def numSpecial(mat: list[list[int]]):
    m = len(mat)
    n = len(mat[0])
    row_count = [0] * m
    col_count = [0] * n

    for row in range(m):
        for col in range(n):
            if mat[row][col] == 1:
                row_count[row] += 1
                col_count[col] += 1

    special_count = 0
    for row in range(m):
        for col in range(n):
            if mat[row][col] == 1:
                if row_count[row] == 1 and col_count[col] == 1:
                    special_count += 1

    return special_count


print(numSpecial(matr))
