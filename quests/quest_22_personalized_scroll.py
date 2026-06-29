#!/usr/bin/python3

# Quest 22: Personalized Scroll
def personalized_greeting(name, quest):
    print(f"{name}, your quest is {quest}.")

name = input("Enter your name: ")
quest = input("Enter your quest: ")

personalized_greeting(name, quest)
