#!/usr/bin/python3
""" some comment """


def append_write(filename="", text=""):
    """ some code """
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
