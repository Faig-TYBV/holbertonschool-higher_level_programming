#!/usr/bin/python3
# learning python
def multiply_list_map(my_list=[], number=0):
    """Multiply all elements of a list by a number using map."""
    return list(map(lambda x: x * number, my_list))