with open("myText.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    line = int(line)
    number = line + 1
    n = f"{number}"
    file = open("myText.txt", "w")
    file.write(n)
    file.close()
