#!/usr/bin/python3
# learning python
def add_tuple(tuple_a=(), tuple_b=()):
    sum1 = 0 
    sum2 = 0
    if len(tuple_a) > 1:
        sum1 += tuple_a[0]
        sum2 += tuple_a[1]
    elif len(tuple_a) > 0:
        sum1 += tuple_a[0]
    if len(tuple_b) > 1:
        sum1 += tuple_b[0]
        sum2 += tuple_b[1]
    elif len(tuple_b) > 0:
        sum1 += tuple_b[0]
    new_tuple = (sum1, sum2)
    return new_tuple
