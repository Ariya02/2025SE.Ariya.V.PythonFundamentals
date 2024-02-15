# Get user input
camelcase = input("Name a variable in camel case ")
# Find uppercase letter
for letter in camelcase:
    if letter.isupper():
        print("_" + letter.lower(), end="")
    else:
        print(letter, end="")

print()
