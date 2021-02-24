import random
import string
from cryptography.fernet import Fernet
import os
import time

# password gen vars
gen_or_see = 2  # 0 for gen, 1 for see
passLength = 1
letters = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation


# Generates a key and save it into a file
# def write_key():
#     key = Fernet.generate_key()
#     with open("pass.key", "wb") as key_file:
#         key_file.write(key)
#
#
# # key loading feature
# def load_key():
#     return open("key.key", "rb").read()
#
# # encrypt/decrypt vars
# key = load_key()
# fer = Fernet(key)

# print line slow method

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


def pogInput(gensee):
    if pogInput == "gen":
        gensee = "y"
        return gensee
    else:
        gen_or_see = "n"


# take input

while gen_or_see == 2:
    if os.path.exists("pin.txt"):
        pinFile = open("pin.txt", "r")
        gensee = str(input("Would you like to access: (gen)erator, password (view)er, (new) pin? or (reset) program? "))
        if gensee == "gen":
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
            specialChar = str(input("Would you like punctuation? y/n "))
            if special(specialChar):
                continue
            if final(lettersChar, numberChar, passLength, specialChar):
                print(final)
                password = final
            username = str(input("What is the username associated with this password? "))
            f = open("passwords.txt", "a")
            f.write(f"{username}:{password}\n")
            f.close()
        elif gensee == "view":
            viewPass = str(input("Enter your pin. "))
            if viewPass == pinFile.read():
                username = str(input("What is the username of the password you are trying to find? "))
                f = open("passwords.txt", "r")
                for line in f:
                    if f"{username}" in line:
                        print(line)
                        found = "y"
                    else:
                        found = "n"
                        continue
                if found == "y":
                    continue
                elif found == "n":
                    print("Username not found.")
            elif viewPass != "1234":
                print("Incorrect Password")
                break
        elif gensee == "new":
            viewPass = str(input("Enter your pin. "))
            if viewPass == pinFile.read():
                pinFile = open("pin.txt", "w")
                resetPin = str(input("Please choose a pin! "))
                pinFile.write(resetPin)
            else:
                print("Incorrect Password")
                break
        elif gensee == "reset":
            really = str(input("This action will reset your pin, passwords, and key. "
                               "Are you sure you want to do this? y/n "))
            if really == "y":
                viewPass = str(input("Enter your pin. "))
                if viewPass == pinFile.read():
                    pinFile.close()
                    f = open("passwords.txt")
                    f.close()
                    print("Removing pin...")
                    os.remove("pin.txt")
                    time.sleep(0.5)
                    print("\nRemoving passwords...")
                    os.remove("passwords.txt")
                    time.sleep(0.5)
                    print("\nDone Successfully! Please re-run the program.")
                    break
                else:
                    print("Incorrect Pin!")
                    time.sleep(0.5)
                    print("\nExiting...")
                    break
        else:
            print("Unknown request. Try again.")
            continue
    else:
        # write_key()
        pinFile = open("pin.txt", "w")
        newPin = str(input("Please choose a pin! "))
        pinFile.write(newPin)
# end of code
