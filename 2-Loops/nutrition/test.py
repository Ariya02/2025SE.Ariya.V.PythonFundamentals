# Fruit Dictionary
fruits = {"Apple": "calories : 130", "Avocado": "calories: 50"}

# Ask for user input
user_input = print("Please enter a fruit name: ")


if user_input in fruits:
    print(fruits[user_input])
else:
    print("Not a fruit in the list")
