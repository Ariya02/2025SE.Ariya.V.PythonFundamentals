amount = 0
while amount < 50:
    coins = int(input("Insert coin (5, 10, 25 only) "))
    if coins not in [5, 10, 25]:
        print("not accepted, amount due: ", amount)
        continue
    else:
        amount += coins
        due = 50 - amount
        if due > 0:
            print("Amount due: ", due)
            continue
        elif due < 0:
            change = amount - 50
            print("Change owed: ", change)
            break
