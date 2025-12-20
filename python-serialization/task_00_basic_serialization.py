#!/usr/bin/python3
# Learning serizalization


import pickle

def serialize_and_save_to_file(data, filename):
    # Serialization

    with open("data.pkl", "wb") as filename:
        pickle.dump(data, filename)

def load_and_deserialize(filename): 
    # Deserialization
    
    with open("data.pkl", "rb") as file:
        loaded_data = pickle.load(filename)
    return loaded_data
