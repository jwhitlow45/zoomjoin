import file_handler as fh

def add(name: str, link: str, passwd: str = ''):
    pass

def remove(meeting_name: str):
    pass

def join(meeting_name: str):
    pass

def list_meetings():
    try:
        meetings = fh.read_meetings_file()
    except Exception as e:
        print(e)
    print(f'Available meetings are: {[key for key in meetings]}')

def help():
    commands = ['add','remove','join','ls']
    print(f'Available commands are: {commands}')
