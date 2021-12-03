import json
import os
import shutil

from json_classes import Meeting

MEETINGS_FILE = '.meetings.json'

def read_meetings_file():
    if not os.path.exists(MEETINGS_FILE):
        print('No meetings file exists, try adding some meetings with the `zm add` command!')
        return None
    
    # read in and return json file
    meetings_data: dict
    with open(MEETINGS_FILE, 'r') as FILE:
        try:
            meetings_data = json.load(FILE)
        except Exception as e:
            print('Exception occured!')
            print(f'Exception info: {e}')
            print('Malformed meetings file, making backup and then allowing overwriting.')
            shutil.copyfile(MEETINGS_FILE, MEETINGS_FILE + '.old')
            return None
    return meetings_data

def write_meetings_file():
    pass