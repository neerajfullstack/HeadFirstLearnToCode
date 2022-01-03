from sys import argv

# unpack the arguments

script, bookLength, currentPage = argv

# Cast them to integers
bookLength = int(bookLength)
currentPage = int(currentPage)

name = input("What is your name?")

# Calculate the how much progress(%) the reader has made

progress = currentPage/bookLength
progress = round(progress * 100)
remaining = 100 - progress
print(f"Hi {name}, You have read about {progress}% of the book, {remaining}% more to go.")
