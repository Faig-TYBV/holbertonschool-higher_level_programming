#!/usr/bin/python3
# learnig python
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for i in lst:
            print("{:d}".format(i), end=' ')
        print("$")
