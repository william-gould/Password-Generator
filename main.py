import random
import string

isDone = 0
passLength = 1
letters = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation

# check if letters
def letter(lettersChar):
    if lettersChar == "y":
        return
    else:
        lettersChar = "n"


# check if numbers
def number(numberChar):
    if numberChar == "y":
        return
    else:
        numberChar = "n"

# check if special
def special(specialChar):
    if (specialChar) == "y":
        return
    else:
        specialChar = "n"

# check final generator args
def final(lettersChar, numberChar, passLength, specialChar):
    if lettersChar == "y" and numberChar == "y":
        if specialChar == "y":
            printable = f"{letters}{numbers}{punctuation}"
            printable = list(printable)
            random.shuffle(printable)
            password = random.choices(printable, k=passLength)
            password = " ".join(password)
            password = password.replace(" ", "")
            print(password)
        else:
            printable = f"{letters}{numbers}"
            printable = list(printable)
            random.shuffle(printable)
            password = random.choices(printable, k=passLength)
            password = " ".join(password)
            password = password.replace(" ", "")
            print(password)
        return False
    if lettersChar == "y" and numberChar == "n":
        if specialChar == "y":
            printable = f"{letters}{punctuation}"
            printable = list(printable)
            random.shuffle(printable)
            password = random.choices(printable, k=passLength)
            password = " ".join(password)
            password = password.replace(" ", "")
            print(password)
        else:
            printable = f"{letters}"
            printable = list(printable)
            random.shuffle(printable)
            password = random.choices(printable, k=passLength)
            password = " ".join(password)
            password = password.replace(" ", "")
            print(password)
        return False

    if lettersChar == "n" and numberChar == "y":
        if specialChar == "y":
            printable = f"{numbers}{punctuation}"
            printable = list(printable)
            random.shuffle(printable)
            password = random.choices(printable, k=passLength)
            password = " ".join(password)
            password = password.replace(" ", "")
            print(password)
            return False
        else:
            printable = f"{numbers}"
            printable = list(printable)
            random.shuffle(printable)
            password = random.choices(printable, k=passLength)
            password = " ".join(password)
            password = password.replace(" ", "")
            print(password)
            return False
    if lettersChar == "n" and numberChar == "n":
        if specialChar == "y":
            printable = f"{punctuation}"
            printable = list(printable)
            random.shuffle(printable)
            password = random.choices(printable, k=passLength)
            password = " ".join(password)
            password = password.replace(" ", "")
            print(password)
            return False
        else:
            print("What are you using it for then?")


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
    specialChar = str(input("Would you like punctation? y/n "))
    if special(specialChar):
        continue
    if final(lettersChar, numberChar, passLength,specialChar):
        print(final)