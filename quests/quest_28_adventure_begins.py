#!/usr/bin/env python3


def start():
    print("\nYou wake up at a crossroads deep in the forest.")
    direction = input("Do you go LEFT or RIGHT? ").strip().lower()

    if direction == "left":
        dark_cave()
    elif direction == "right":
        sunny_meadow()
    else:
        print("You stood still and a wolf found you. Game over.")

def dark_cave():
    print("\nYou enter a dark cave. You hear growling ahead.")
    choice = input("Do you PROCEED or RETREAT? ").strip().lower()

    if choice == "proceed":
        print("\nYou face a dragon — but it was sleeping! You sneak past and find a chest of gold.")
        print("ENDING 1: You become the richest adventurer in the land. 🏆")
    elif choice == "retreat":
        print("\nYou back away slowly and escape the cave safely, but leave empty-handed.")
        print("ENDING 2: You live to fight another day, but with nothing to show for it.")
    else:
        print("You froze in place. The dragon woke up. Game over.")

def sunny_meadow():
    print("\nYou walk into a sunny meadow. A fairy appears and offers you a gift.")
    gift = input("Do you accept a SWORD or a MAP? ").strip().lower()

    if gift == "sword":
        print("\nArmed with the magic sword, you defeat a nearby troll and become a hero.")
        print("ENDING 3: Songs are sung of your bravery across the kingdom. ⚔️")
    elif gift == "map":
        print("\nThe map leads you to a hidden village that needed help. You become their leader.")
        print("ENDING 4: You build a thriving community and rule with wisdom. 🗺️")
    else:
        print("You offended the fairy. She turned you into a frog. Game over.")

start()