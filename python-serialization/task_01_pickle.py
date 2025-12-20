#!/usr/bin/python3
# Pickle


import pickle


class CustomObject:
    '''Class'''

    def __init__(self, n, a, iS):
        # Init

        self.name = n
        self.age = a
        self.is_student = iS

    def display(self):
        # Information

        print("Name: {}\nAge: {}\nIs Student: {}"
              .format(self.name, self.age, self.is_student))

    def serialize(self, filename):
        # Serializing instances

        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (EOFError, pickle.UnpicklingError, FileNotFoundError):
            return None
