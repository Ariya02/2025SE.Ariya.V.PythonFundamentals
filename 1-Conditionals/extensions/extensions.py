suffix = input("Enter a file name suffix ")

if suffix.endswith(".gif"):
    print("image/gif")
elif suffix.endswith(".jpg"):
    print("image/jpg")
elif suffix.endswith(".jpeg"):
    print("image/jpeg")
elif suffix.endswith(".png"):
    print("image/png")
elif suffix.endswith(".pdf"):
    print("application/pdf")
elif suffix.endswith(".txt"):
    print("image/txt")
elif suffix.endswith(".zip"):
    print("file/zip")
else:
    print("application/octet-stream")
