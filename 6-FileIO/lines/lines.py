import sys


def main():
    command_line()
    # Open file
    try:
        f = open(sys.argv[1], "r")
        line = f.readline()
    # If file does not exist, catch exception
    except FileNotFoundError:
        sys.exit("File does not exist")
    lines = 0
    for word in line:
        if check_lines(word) == False:
            lines += 1
    print(lines)


def command_line():
    # Check number of arguements in command line
    if len(sys.argv) < 2:
        sys.exit("Too few command line arguements")
    if len(sys.argv) > 2:
        sys.exit("Too many command line arguements")
    # Check if python file
    if ".py" not in sys.argv[1]:
        sys.exit("Not python file")


def check_lines(word):
    if word.isspace:
        return True
    if word.lstrip().startswith("#"):
        return True


main()
