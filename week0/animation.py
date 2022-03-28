import time

ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def face_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + "   /-----\ ")
    print(sp + "  / . | . \ ")
    print(sp + "(|    <    |) ")
    print(sp + "  \ (===) / ")
    print(sp + "   \_____/  ")
    print(RESET_COLOR)


def face():

    # loop control variables
    start = 0  # start at zero
    distance = 60  # how many times to repeat
    step = 2  # count by 2

    # loop purpose is to animate ship sailing
    for position in range(start, distance, step):
        face_print(position)  # call to function with parameter
        time.sleep(.1)
