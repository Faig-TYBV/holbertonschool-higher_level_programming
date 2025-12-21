#!/usr/bin/python3
# CSV to JSON


import csv
import json


def convert_csv_to_json(csv_name):
    # converting csv to json

    data = []
    try:
        with open(csv_name, newline='\n') as cn:
            line = csv.DictReader(cn)
            for row in line:
                data.append(row)

        # Serialize list of dictionaries to JSON and write to file
        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)
        return True
    except Exception:
        return False
