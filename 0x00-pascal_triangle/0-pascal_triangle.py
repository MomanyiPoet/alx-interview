#!/usr/bin/python3
'''pascals triangle'''

def pascal_triangle(t):
    """
    Pascal's triangle
    Args:
        t (int): The number of rows of the triangle
    Returns:
        integers representing the Pascals triangle
    """
    if t <= 0:
        return[]
    triangle = [[1]]
    for i in range(1, t):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
