
# Re-commenting Quest 27 (FizzBuzz) as my reflective scribe submission.

# Loop through every number from 1 to 100 (range stops before 101)
for i in range(1, 101):

    # Check for FizzBuzz FIRST — if we checked Fizz or Buzz first,
    # multiples of both (like 15) would only print "Fizz" or "Buzz" instead of "FizzBuzz"
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    # % is the modulo operator — it gives us the remainder of a division.
    # If i % 3 == 0, there is no remainder, meaning i is divisible by 3.
    elif i % 3 == 0:
        print("Fizz")

    # Same logic for multiples of 5
    elif i % 5 == 0:
        print("Buzz")

    # If none of the above conditions are true, just print the number itself
    else:
        print(i)




#  Re-commenting quest_28_adventure_begins.py

# Each function represents a different location in the adventure.
# Breaking the game into functions keeps the code organized and reusable.

def start():
    # Print the opening scene to set the story context
    print("\nYou wake up at a crossroads deep in the forest.")
    
    # Ask the player to choose a direction; strip() removes accidental spaces,
    # lower() makes the comparison case-insensitive
    direction = input("Do you go LEFT or RIGHT? ").strip().lower()

    # Route the player to the correct location based on their choice
    if direction == "left":
        dark_cave()       # Call the dark_cave function if they go left
    elif direction == "right":
        sunny_meadow()    # Call the sunny_meadow function if they go right
    else:
        # Handle any input that isn't "left" or "right"
        print("You stood still and a wolf found you. Game over.")

def dark_cave():
    # This is the left-path location — a risky cave with a sleeping dragon
    print("\nYou enter a dark cave. You hear growling ahead.")
    
    # Give the player a second decision inside this location (nested choice)
    choice = input("Do you PROCEED or RETREAT? ").strip().lower()

    if choice == "proceed":
        # Brave choice leads to Ending 1 — the best reward
        print("\nYou face a dragon — but it was sleeping! You sneak past and find a chest of gold.")
        print("ENDING 1: You become the richest adventurer in the land. 🏆")
    elif choice == "retreat":
        # Safe choice leads to Ending 2 — survival but no reward
        print("\nYou back away slowly and escape the cave safely, but leave empty-handed.")
        print("ENDING 2: You live to fight another day, but with nothing to show for it.")
    else:
        # Catch-all for unrecognized input
        print("You froze in place. The dragon woke up. Game over.")

def sunny_meadow():
    # This is the right-path location — a peaceful meadow with a fairy
    print("\nYou walk into a sunny meadow. A fairy appears and offers you a gift.")
    
    # A third decision point — leads to two more possible endings
    gift = input("Do you accept a SWORD or a MAP? ").strip().lower()

    if gift == "sword":
        # Choosing the sword leads to Ending 3 — a warrior's path
        print("\nArmed with the magic sword, you defeat a nearby troll and become a hero.")
        print("ENDING 3: Songs are sung of your bravery across the kingdom. ⚔️")
    elif gift == "map":
        # Choosing the map leads to Ending 4 — a leader's path
        print("\nThe map leads you to a hidden village that needed help. You become their leader.")
        print("ENDING 4: You build a thriving community and rule with wisdom. 🗺️")
    else:
        # Catch-all for unrecognized input
        print("You offended the fairy. She turned you into a frog. Game over.")

# Entry point — the game begins here
start()




# Re-commenting quest_29_code_breaker.py

# Store the secret code as a constant (ALL_CAPS signals it shouldn't change)
SECRET_CODE = 42

# Maximum number of guesses the player is allowed
MAX_ATTEMPTS = 3

print("Welcome, Agent. You have 3 attempts to enter the secret code.")

# range(1, MAX_ATTEMPTS + 1) gives us [1, 2, 3] so the attempt number
# displayed to the user is human-friendly (starts at 1, not 0)
for attempt in range(1, MAX_ATTEMPTS + 1):
    
    # Convert input to int immediately — input() always returns a string,
    # and we need a number to compare against SECRET_CODE
    guess = int(input(f"Attempt {attempt}/{MAX_ATTEMPTS} — Enter the code: "))

    if guess == SECRET_CODE:
        # Correct guess — congratulate the player and exit the loop early
        print("Access granted. The mission is yours.")
        break  # break stops the for loop immediately; no more attempts needed
    
    elif attempt < MAX_ATTEMPTS:
        # Wrong guess but still has attempts left — encourage them to retry
        print("Wrong code. Try again.")
    
    else:
        # Wrong guess on the final attempt — game over message
        # This runs instead of the elif because attempt == MAX_ATTEMPTS
        print("3 failed attempts. System locked. Mission failed.")