from datetime import date
import inflect

p = inflect.engine()


class seasons:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


def main():
    # Conversions
    birth_year = int(get_year())
    birth_month = int(get_month())
    birth_day = int(get_day())
    date_today = str(date.today())
    year_today, month_today, day_today = date_today.split("-")
    year_today = int(year_today)
    month_today = int(month_today)
    day_today = int(day_today)
    year = year_today - birth_year
    month = month_today - birth_month
    day = day_today - birth_day
    # Calculations
    year = 365 * year * 1440
    month = 30 * month * 1440
    day = day * 1440
    minutes = year + month + day
    words = p.number_to_words(minutes)
    print(words, "minutes")


def get_year():
    while True:
        year = input("Year (YYYY format): ")
        if len(year) != 4:
            print("Incorrect format")
            continue
        if len(year) == 4:
            break
    return year


def get_month():
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
    return month


def get_day():
    while True:
        day = input("Day (DD format): ")
        if len(day) != 2:
            print("Incorrect format")
            continue
        if len(day) == 2:
            break
    return day


if __name__ == "__main__":
    main()
