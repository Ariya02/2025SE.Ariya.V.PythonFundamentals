import sys
from tabulate import tabulate
import csv


def main():
    command_line()
    file_exist()
    with open("regular.csv", newline="") as file:
        reader = csv.DictReader(file)
        table = [row for row in reader]
        print(tabulate(table, tablefmt="grid"))


def command_line():
    # Check command line arguements
    if len(sys.argv) > 2:
        sys.exit("Too many command line arguements")
    if len(sys.argv) < 2:
        sys.exit("To few command line arguements")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")


def file_exist():
    try:
        open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.exit("File does not exist")


main()
