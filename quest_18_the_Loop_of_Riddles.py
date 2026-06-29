#!/usr/bin/python3
number = 7
while True:
    guess = int(input("Guess the number: "))

    if guess == number:
        print("Congratulations!, you guessed right")
        break
    else:
        print("Wrong guess. Try again!")
