import sys
import csv


def main():
    command_line()
    file_exist()
    file()


def command_line():
    if len(sys.argv) > 3:
        sys.exit("Too many command arguements")
    if len(sys.argv) < 3:
        sys.exit("Too few command line arguements")


def file_exist():
    try:
        open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.exit("File does not exist")


def file():
    with open("before.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        order = []
        for row in reader:
            name = row["name"]
            hhouse = row["house"]
            last_name, first_name = name.split(",")
            order.append({"first": first_name, "last": last_name, "house": hhouse})
            with open(sys.argv[2], "w") as file:
                writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in order:
                    writer.writerow(row)


main()
