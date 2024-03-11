import inflect

p = inflect.engine

name = input("Enter names")
name = {}
plural = p.join(name, final_sep="")
adieu = "Adieu, adieu to"

try:
    while True:
        size = len(name)
        if size > 1:
            print(plural)
        elif size == 1:
            print(adieu, name)
        else:
            "incorrect input"
except EOFError:
    ("No more names")
