import random
import string
isDone = 0
passLength = 1
letters = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation

def special(specialChar):
    if(specialChar) == "y":
        specialChar = "y"
    else:
        specialChar = "n"

# check if letters
def letter(lettersChar):
    if lettersChar == "y":
        lettersChar = "y"
    else:
        lettersChar = "n"

# check if numbers
def number(numberChar):
    if numberChar == "y":
        numberChar = "y"
    else:
         numberChar = "n"

# check if special
#string.punctuation

# check final generator args
def final(lettersChar, numberChar, specialChar, passLength):
    if lettersChar == "y" and numberChar == "y":
        printable = f"{letters}{numbers}"
        printable = list(printable)
        random.shuffle(printable)
        password = random.choices(printable, k=passLength)
        password = " ".join(password)
        password = password.replace(" ","")
        print(password)
        return False
    if lettersChar == "y" and numberChar == "n":
        printable = f"{letters}"
        printable = list(printable)
        random.shuffle(printable)
        password = random.choices(printable, k=passLength)
        password = " ".join(password)
        password = password.replace(" ","")
        print(password)
        return False
    if lettersChar == "n" and numberChar == "y":
        printable = f"{numbers}"
        printable = list(printable)
        random.shuffle(printable)
        password = random.choices(printable, k=passLength)
        password = " ".join(password)
        password = password.replace(" ","")
        print(password)
        return False
    else:
        print("Why are you using it then..?")

def anotherPass(anotherPassword):
    if anotherPassword == "y":
        isDone = 1
    else:
        isDone = 0

# take input
while isDone == 0:
    passLength = int(input("How long would you like the password to be? 1-99 "))
    if passLength >= 100:
        print("Please pick a number between 1 and 99.")
        continue
    lettersChar = str(input("Would you like letters? y/n "))
    if letter(lettersChar):
        continue

    numberChar = str(input("Would you like numbers? y/n "))
    if number(numberChar):
        continue

    if final(lettersChar, numberChar, passLength):
        print(final)
    anotherPassword = str(input("Would you like to generator another password? y/n "))
    if anotherPass(anotherPassword):
        continue
    else:
        break


