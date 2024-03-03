# List of months
months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12",
}

numeric_months = {
    "1": "01",
    "2": "02",
    "3": "03",
    "4": "04",
    "5": "05",
    "6": "06",
    "7": "07",
    "8": "08",
    "9": "09",
    "10": "10",
    "11": "11",
    "12": "12",
}

while True:
    try:
        # Get user input
        print("Enter a date in Month-Day-Year format ")
        date = input().replace(",", " ").replace("/", " ")
        # Split input into month date year
        date = date.split()
        month, day, year = date

        # Capitalise first letter in month
        month = month.title()

        # Make day an integer
        day = int(day)
        if 1 <= day <= 31:
            pass
        else:
            print("Invalid: ")
            continue

        if month in months:
            print(year, "-", months[month], "-", day)
        elif month in numeric_months:
            print(year, "-", numeric_months[month], "-", day)
            break
        else:
            print("Invalid re-enter: ")
            continue
    except ValueError:
        pass
