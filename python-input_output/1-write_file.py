#!/usr/bin/python3
""" Some text """


def read_file(filename=""):
    """ some code """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
