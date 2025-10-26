greeting = (input("Enter greeting: ")).lower()

if greeting == "hello":
    print("$0")
elif greeting.startswith("h") == True:
    print("$20")
else:
    print("$100")
