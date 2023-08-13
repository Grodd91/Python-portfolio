def generate_pascals_triangle(num_rows):
    triangle = [[1] * (i + 1) for i in range(num_rows)]

    for i in range(2, num_rows):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle
