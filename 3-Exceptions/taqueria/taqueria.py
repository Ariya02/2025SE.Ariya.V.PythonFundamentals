amount = 0
while True:
    try:
        order = input("What is your order? ")

        # Menu dictionary
        menu = {
            "Baja Taco": 4.25,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00,
        }

        if order in menu:
            amount += menu[order]
            print("Total: $", amount)
            continue
        elif order in menu:
            amount += menu[order]

        else:
            print("Not on Menu, please re-order ")
            continue

    except EOFError:
        print("Finalised order")
        break
