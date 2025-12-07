#!/usr/bin/python3
# learning python
def square_matrix_simple(matrix=[]):
    ans = []
    for row in matrix:
        ans.append(list(map(lambda x: x ** 2, row)))
    return ans