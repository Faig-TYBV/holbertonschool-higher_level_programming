#!/usr/bin/python3
# learning python
def max_integer(my_list=[]):
    max = None
    for i in my_list:
        if max is None or max < i:
            max = i
    return max
