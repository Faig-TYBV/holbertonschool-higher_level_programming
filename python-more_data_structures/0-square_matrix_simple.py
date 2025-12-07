#!/usr/bin/python3
# learning python
def square_matrix_simple(matrix=[]):
  ans=list()
  for i in matrix:
    ans.append(list(map(lambda x: x**2, i)))
  return ans