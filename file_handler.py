import json
import os
import shutil

MEETINGS_FILE = '.meetings.json'


def read_meetings_file():
    if not os.path.exists(MEETINGS_FILE):
        write_meetings_file({})
        return json.load(MEETINGS_FILE)

    # read in and return json file
    meetings_data: dict
    with open(MEETINGS_FILE, 'r') as FILE:
        try:
            meetings_data = json.load(FILE)
        except Exception as e:
            shutil.copyfile(MEETINGS_FILE, MEETINGS_FILE + '.old')
            raise Exception('Malformed meetings file, making backup.')
    return meetings_data


def write_meetings_file(meetings_dict: dict):
    # write dict to json file
    with open(MEETINGS_FILE, 'w') as FILE:
        json.dump(meetings_dict, FILE, sort_keys=True)
