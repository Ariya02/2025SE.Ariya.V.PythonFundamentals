def main():
    x = int(input("Enter a value for x: "))
    y = input("Enter either a +, -, *, /: ")
    z = int(input("Enter a value for y: "))
    x = float(x)
    z = float(z)
    if y == ("+"):
        print(x + z)
    elif y == ("-"):
        print(x - z)
    elif y == ("*"):
        print(x * z)
    elif y == ("/"):
        print(x / z)


main()
