import random
import string

# password gen vars
gen_or_see = 0 # 0 for gen, 1 for see
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
            global password
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

pogInput = input("Would you like to generate or find password? gen/see")
if pogInput == "gen":
    gen_or_see = 0
else:
    gen_or_see = 1

# take input
while gen_or_see == 0:
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
        password = final
    username = str(input("What is the username associated with this password? "))
    f = open("passwords.txt", "a")
    f.write(f"{username}:{password}\n")
    f.close()

while gen_or_see == 1:
    username = str(input("What is the username of the password you are trying to find?"))
# close connect