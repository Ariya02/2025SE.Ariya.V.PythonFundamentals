import sys
from pyfiglet import Figlet

fonts = Figlet().getFonts()

# Check for validity
if len(sys.argv) > 1:
    firstargv = sys.argv[1]
    secargv = sys.argv[2]
else:
    sys.exit("Invalid Usage")

if firstargv == "-f" or "--font":
    input = input("User input: ")
else:
    sys.exit("Does not start with -f or --font")


if secargv in fonts:
    set_font = Figlet(font=secargv)
    print(set_font.renderText(input))
else:
    sys.exit("Invalid Usage")
