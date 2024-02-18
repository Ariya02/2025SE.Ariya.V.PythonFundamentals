# Get user input
twttr = input("Type a word: ")
# Find and remove vowels
letter = (
    twttr.replace("a", "")
    .replace("e", "")
    .replace("i", "")
    .replace("o", "")
    .replace("u", "")
)
print(letter)
