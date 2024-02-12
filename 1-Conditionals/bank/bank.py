greeting = input("Type a greeting ")

bank_greeting = greeting.strip().lower()

if bank_greeting.startswith("hello"):
    print("$0")
elif bank_greeting.startswith("h"):
    print("$20")
else:
    print("$100")
