import file_handler as fh

def add(name: str, link: str, passwd: str = ''):
    # value for name key in dict
    value = {'link':link, 'passwd':passwd}
    meetings: any
    try:
        meetings = fh.read_meetings_file()
    except Exception as e:
        # create new meeting structure
        new_meeting_dict = {}
        new_meeting_dict[name] = value
        print(e)
        print(f'Overwriting original meetings file and adding {name}.')
        fh.write_meetings_file(new_meeting_dict)

    # add entry to existing dict in file
    meetings[name] = value
    print(meetings)
    # write to file
    fh.write_meetings_file(meetings)

def remove(meeting_name: str):
    pass

def join(meeting_name: str):
    pass

def list_meetings():
    meetings: any
    try:
        meetings = fh.read_meetings_file()
    except Exception as e:
        print(e)
    print(f'Available meetings are: {[key for key in meetings]}')

def help():
    commands = ['add','remove','join','ls']
    print(f'Available commands are: {commands}')
