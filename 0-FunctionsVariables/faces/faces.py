def main():
    convert = input("write a sentence with either a smiley face or frown face ")
    convert = convert.replace(":)", "🙂")
    convert = convert.replace(":(", "🙁")
    print(convert)


main()
