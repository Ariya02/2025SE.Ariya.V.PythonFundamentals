import csv
import sys


def main():
    command_line()
    exist()
    open_file()


def command_line():
    if len(sys.argv) > 3:
        sys.exit("Too many command line arguements")
    if len(sys.argv) < 3:
        sys.exit("Too little command line arguements")
    if "csv" not in sys.argv:
        print("Not a csv file")


def exist():
    try:
        open(sys.argv[1], "r")
    except FileNotFoundError:
        print("File does not exist")


def open_file():
    with open("before.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        order = []
        for row in reader:
            name = row[name]
            house = row[house]
            last_name, first_name = name.split(",")
            order.append({"first": first_name, "last": last_name, "house": house})
            with open(sys.argv[2], "w") as file:
                writer = csv.DictWriter(file)
                for row in order:
                    writer.writerow(row)
