#!/usr/bin/python3
""" some code """
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
arguments = []
if os.path.exists('add_item.json'):
    arguments = load_from_json_file('add_item.json')
for arg in sys.argv[1:]:
    if arg not in arguments:
        arguments.append(arg)
save_to_json_file(arguments, "add_item.json")
