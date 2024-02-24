while True:

    while True:
        amount = input("Enter how much fuel is in the tank (only as a fraction) ")
        x, y, z = [fuel for fuel in amount]
        x = int(x)
        z = int(z)
        percent = (x / z) * 100
        if 100 >= percent >= 99:
            print("F")
            break
        elif percent <= 1:
            print("E")
            break
        elif percent > 100:
            print("Incorrect amount")
            continue
        else:
            print(percent, "%")
            break
