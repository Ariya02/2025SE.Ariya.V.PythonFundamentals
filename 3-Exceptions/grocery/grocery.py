def main():
    print("Enter your grocery items:")
    groceries = {}

    try:
        while True:
            items = input().strip().lower()
            if items == "":
                continue
            groceries[items] = groceries.get(items, 0) + 1
    except EOFError:
        pass

    print("Grocery list:")
    for items in sorted(groceries.keys()):
        count = groceries[items]
        print(count, items.upper())


main()
