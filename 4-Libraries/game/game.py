import random

while True:
    try:
        n = int(input("Level: "))
        if n > 1:
            break
        elif n < 1:
            continue
    except ValueError:
        continue

random_number = random.randrange(1, n)

while True:
    try:
        if n > 1:
            guess = int(input("Guess: "))
            if guess < 0:
                continue
            elif guess == random_number:
                print("Just right!")
                n == 0
                break
            elif guess < random_number:
                print("Too Little!")
                continue
            elif guess > random_number:
                print("Too Large!")
                continue
            elif guess < 1:
                continue
        elif 0 < n < 1:
            continue
    except ValueError:
        continue
