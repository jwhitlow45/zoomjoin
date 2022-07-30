import sys
import commands as c
from commands import Command

class Input():
    ARGSIZE = len(sys.argv) - 1

    # ARGUMENTS
    COMMAND = sys.argv[1]
    NAME: str
    LINK: str
    PASSWORD: str
    if ARGSIZE > 1:
        NAME = sys.argv[2]
    if ARGSIZE > 2:
        LINK = sys.argv[3]
    if ARGSIZE > 3:
        PASSWORD = sys.argv[4]

def main():
    match Input.COMMAND:
        case Command.ADD.value:
            c.add(Input.NAME, Input.LINK, Input.PASSWORD)
        case Command.REMOVE.value:
            c.remove(Input.NAME)
        case Command.REMOVE_ALL.value:
            c.remove_all()
        case Command.JOIN.value:
            c.join(Input.NAME)
        case Command.LS.value:
            c.list_meetings()
        case Command.HELP.value:
            c.help()
        case _:
            print('Invalid command. Use `zm help` for help.')


if __name__ == "__main__":
    main()
