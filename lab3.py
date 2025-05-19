import random

# 1. Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

def arrayCheck(numbers):
    for i in range(len(numbers) - 2):
        print(f"Checking position {i}: {numbers[i]}")
        if numbers[i] == 1:
            print("Found 1")
            if numbers[i + 1] == 2:
                print("Found 2 after 1")
                if numbers[i + 2] == 3:
                    print("Found 3 after 1, 2")
                    return True
    return False

print(arrayCheck([123, 123, 1,2,3, 123]))


# 2. Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".
def myString(string = "hello"):
    newstring =""
    for char in range(0, len(string), 2):
        newstring += string[char]
        print(string[char])
    return newstring
myString("Hello")


# 3. Given a string, return a string where for every char in the original,
# # there are two chars. Example:
# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def addDoubleCharsToString(string = "hello"):
    newstring =""
    for char in string:
        newstring += char
        newstring += char
        print(char)
    return newstring

print(addDoubleCharsToString("Hello"))



# 4. Return the number of even integers in the given array/list.
# Examples:
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0


def count_evens(numbers):
    numberOfEvens = 0
    for num in numbers:
        if num % 2 == 0:
            numberOfEvens += 1
    return numberOfEvens

print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2,2,0]))
print(count_evens([1,3,5]))


# 5. Optional Lab:

######
# WORK IN PROGRESS!

def game_loop():
    print("Loop start")

    print("Loop end")

def player_guess(guess):
    print(guess)

def number_guessing_game():
    computer_number = random.randint(100,999)
    player_guess = 0
    game_over = False
    while not game_over:
        player_guess(input((int("Please guess a number"))))

    print(computer_number)

