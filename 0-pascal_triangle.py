#!/usr/bin/python3

def pascal_triangle(t):
    if t <= 0:
        return []
    triangle = [[1]]
    for i in range(1, t):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle