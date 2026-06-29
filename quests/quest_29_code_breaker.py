#!/usr/bin/env python3


SECRET_CODE = 42
MAX_ATTEMPTS = 3

print("Welcome, Agent. You have 3 attempts to enter the secret code.")

for attempt in range(1, MAX_ATTEMPTS + 1):
    guess = int(input(f"Attempt {attempt}/{MAX_ATTEMPTS} — Enter the code: "))

    if guess == SECRET_CODE:
        print("Access granted. The mission is yours.")
        break
    elif attempt < MAX_ATTEMPTS:
        print("Wrong code. Try again.")
    else:
        print("3 failed attempts. System locked. Mission failed.")