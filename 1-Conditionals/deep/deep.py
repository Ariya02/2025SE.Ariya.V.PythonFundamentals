answer = str(
    input("What is the answer to the Great Question of Life, Universe and Everything? ")
)

if answer == "42":
    print("Yes")
elif answer == "forty two":
    print("Yes")
elif answer == "forty-two":
    print("Yes")
else:
    print("No")
