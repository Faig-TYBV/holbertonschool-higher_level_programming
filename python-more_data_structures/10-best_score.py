#!/usr/bin/python3
# learning python
from functools import reduce
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return reduce(
        lambda a, b: a if a_dictionary[a] >= a_dictionary[b] else b,
        a_dictionary.keys()
    )
