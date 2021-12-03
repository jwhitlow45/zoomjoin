import file_handler as fh
import webbrowser


def add(name: str, link: str, passwd: str = ''):
    # value for name key in dict
    value = {'link': link, 'passwd': passwd}
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
    # write to file
    fh.write_meetings_file(meetings)
    print(f'Added meeting {name}.')


def remove(name: str):
    try:
        meetings = fh.read_meetings_file()
        del meetings[name]
        fh.write_meetings_file(meetings)
    except KeyError as k:
        print(f'Meeting {name} does not exist.')
        return
    except Exception as e:
        print(e)
        print(f'Overwriting original meetings file.')
        fh.write_meetings_file({})
        return

    print(f'Removed meeting {name}.')


def remove_all():
    print('Are you sure you want to delete all meetings?(y/N): ', end='')
    response = input()
    if response == 'y':
        fh.write_meetings_file({})
        print('Deleted all meetings.')


def join(name: str):
    try:
        meetings = fh.read_meetings_file()
        link = meetings[name]['link']
        passwd = meetings[name]['passwd']

        if passwd:
            print(f'Password: {passwd}')
        webbrowser.open(link)

    except Exception as e:
        print(f'Could not join meeting due to malformed meetings file.')
        return

    print(f'Joining meeting {name}...')


def list_meetings():
    meetings: any
    try:
        meetings = fh.read_meetings_file()
    except Exception as e:
        print(e)
    print(f'Available meetings are: {[key for key in meetings]}')


def help():
    commands = ['add', 'remove', 'join', 'ls']
    print(f'Available commands are: {commands}')
