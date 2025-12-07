#!/usr/bin/python3
# learning python
def best_score(a_dictionary):
    """Return the key with the highest integer value."""
    if not a_dictionary:
        return None

    # Select the key with the maximum value
    return max(a_dictionary, key=a_dictionary.get)
