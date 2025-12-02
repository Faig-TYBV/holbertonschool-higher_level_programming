#!/usr/bin/python3
# learnig python
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        ln = len(lst) - 1
        for i in range(ln):
            print("{:d}".format(lst[i]), end=' ')
        print("{:d}".format(lst[ln]))
    if len(matrix) == 0:
        print(" ")
