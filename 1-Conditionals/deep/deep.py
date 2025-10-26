question = input(
    "Provide an answer for the Great Question of Life, the Universe and Everything: "
)
answer = question.lower()

if answer == "42":
    print("Yes")
elif answer == "forty-two":
    print("Yes")
elif answer == "forty two":
    print("Yes")
else:
    print("No")
