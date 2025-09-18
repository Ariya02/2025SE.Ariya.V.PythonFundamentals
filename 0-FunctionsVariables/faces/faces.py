userInput = input("Enter something: ")
emoji = ":)" or ":("

if emoji in userInput:
    converted = userInput.replace(":)", "🙂") or (":(", "🙁")
    print(converted)
else:
    print(userInput)
