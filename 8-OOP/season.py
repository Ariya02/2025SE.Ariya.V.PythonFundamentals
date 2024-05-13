from datetime import date


def main():
    print("Enter your date of birth")
    year()
    month()
    day()
    date_today = str(date.today())
    year_today, month_today, day_today = date_today.split("-")
    # birth_year = year_today -
    print()


def year():
    while True:
        year = input("Year (YYYY format): ")
        if len(year) != 4:
            print("Incorrect format")
            continue
        if len(year) == 4:
            break
    return year


def month():
    while True:
        month = input("Month (MM format): ")
        if len(month) != 2:
            print("Incorrect format")
            continue
        if len(month) == 2:
            break
        if month >= 12:
            break
        if month >= 12:
            print("Enter a month between 1 and 12")
            continue


def day():
    while True:
        day = input("Day (DD format): ")
        if len(day) != 2:
            print("Incorrect format")
            continue
        if len(day) == 2:
            break


if __name__ == "__main__":
    main()
