import sys

# Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguements")

for argv in sys.argv[1:]:
    # Print name tag
    print("Hello, my name is", argv)
