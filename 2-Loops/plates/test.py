plate = input("Plate: ")

# slice the first two letters
letters = plate[0:2]
# Check if input has two letters
if letters.isalpha():
    # Check length of input (ensure between 2 and 6)
    if 2 <= len(plate) <= 6:
        if plate[-2].isdigit():
            if plate.startswith("0"):
                print("Invalid")
            else:
                print("valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
else:
    print("Invalid")
