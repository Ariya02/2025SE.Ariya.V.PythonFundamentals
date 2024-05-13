# Text Menu Practice
def main():
    print("Choose an option:\n 1.\n 2.\n 3.\n 4. Exit")
    while True:
        user = int(input("Which option would you like to choose? "))
        if user == 1:
            first_option()
            break
        if user == 2:
            second_option()
            break
        if user == 3:
            third_option()
            break
        if user == 4:
            exit()
            break
        else:
            print(user)


def first_option():
    name = input("What is your name? ")
    input(f"Hello, {name}. How are you? ")
    print("Thank you for telling me.\n You have now exited the program")


def second_option():
    print("Thank you for choosing option 2.")
    fact = input(" Would you like to know a fun fact? \n Reply Yes or No: ")
    while True:
        if fact == "Yes":
            print("Did you know that Australia is wider than the moon?")
            print("Thank you for playing along, we hope you learned something")
            break
        elif fact == "No":
            print("That's okay, maybe another day.\n ")
            print("Your program will now exit.")
            break
        else:
            print("Please only respond with Yes or No")
            continue


def third_option():
    print("Thank you for choosing option 3")


def exit():
    print("You have exited the program \nThank you ")


main()
