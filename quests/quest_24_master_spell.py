#!/usr/bin/python3

# Quest 24: Master Spell
def ask_for_age():
    age = int(input("Enter your age: "))
    return age

def can_they_vote(age):
    if age >= 18:
        print("You can vote.")
    else:
        print("You cannot vote.")

age = ask_for_age()
can_they_vote(age)
