import random
import string
letterNum = random.randrange(0,27)
isDone = 0

#def special(specialChar):
#    if(specialChar) == True:


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
def final(lettersChar, numberChar):
    if lettersChar == "y" and numberChar == "y":
        print(f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"
              f"{random.choice(string.ascii_letters)}{random.choice(string.ascii_letters)}"
              f"{random.choice(string.ascii_letters)}{random.choice(string.ascii_letters)}"
              f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
              f"{random.choice(string.ascii_letters)}{random.choice(string.ascii_letters)}"
              f"{random.choice(string.ascii_letters)}{random.choice(string.ascii_letters)}")
        return False
    if lettersChar == "y" and numberChar == "n":
        print(f"{random.choice(string.ascii_letters)}{random.choice(string.ascii_letters)}"
              f"{random.choice(string.ascii_letters)}{random.choice(string.ascii_letters)}"
              f"{random.choice(string.ascii_letters)}{random.choice(string.ascii_letters)}"
              f"{random.choice(string.ascii_letters)}{random.choice(string.ascii_letters)}"
              f"{random.choice(string.ascii_letters)}{random.choice(string.ascii_letters)}"
              f"{random.choice(string.ascii_letters)}{random.choice(string.ascii_letters)}")
        return False
    if lettersChar == "n" and numberChar == "y":
        print(f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"
              f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"
              f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}")
        return False
    else:
        print("Why are you using it then..?")

# take input
while isDone == 0:

    lettersChar = str(input("Would you like letters? y/n "))
    if letter(lettersChar):
        continue

    numberChar = str(input("Would you like numbers? y/n "))
    if number(numberChar):
        continue

    if final(lettersChar, numberChar):
        print(final)

    isDone = 1
