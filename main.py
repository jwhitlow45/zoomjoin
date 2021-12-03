import sys
import commands as c


class Input():
    ARGSIZE = len(sys.argv) - 1

    # ARGUMENTS
    COMMAND = sys.argv[1]
    NAME = ''
    LINK = ''
    PASSWORD = ''
    if ARGSIZE > 1:
        NAME = sys.argv[2]
    if ARGSIZE > 2:
        LINK = sys.argv[3]
    if ARGSIZE > 3:
        PASSWORD = sys.argv[4]


def main():
    if Input.COMMAND == 'add':
        c.add(Input.NAME, Input.LINK, Input.PASSWORD)
    elif Input.COMMAND == 'remove':
        c.remove(Input.NAME)
    elif Input.COMMAND == 'remove_all':
        c.remove_all()
    elif Input.COMMAND == 'join':
        c.join(Input.NAME)
    elif Input.COMMAND == 'ls':
        c.list_meetings()
    elif Input.COMMAND == 'help':
        c.help()
    else:
        raise ValueError('Invalid command given.')


if __name__ == "__main__":
    main()
