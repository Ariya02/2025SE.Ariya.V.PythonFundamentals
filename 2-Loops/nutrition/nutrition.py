# Fruit Dictionary
fruits = {
    "Apple": "calories : 130",
    "Avocado": "calories: 50",
    "Banana": "calories: 110",
    "Cantaloupe": "calories: 50",
    "Grapefruit": "calories: 60",
    "Grapes": "calories: 90",
    "Honeydew Melon": "calories: 50",
    "Kiwifruit": "calories: 90",
    "Lemon": "calories: 15",
    "Lime": "calories: 20",
    "Nectarine": "calories: 60",
    "Orange": "calories: 80",
    "Peach": "calories: 60",
    "Pear": "calories: 100",
    "Pineapple": "calories: 50",
    "Plums": "calories: 70",
    "Strawberries": "calories:50",
    "Sweet Cherries": "calories: 100",
    "Tangerine": "calories: 50",
    "Watermelon": "calories: 80",
}

# Ask for user input
fruit_name = input("Please enter a fruit name: ")


if fruit_name in fruits:
    print(fruits[fruit_name])
else:
    print("Not a fruit in the list")
