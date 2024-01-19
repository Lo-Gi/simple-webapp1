# simple mastermind game in python 3.12

import random

def generate_code():
    colors = ['R', 'G', 'B', 'Y', 'O', 'P']  # Available colors
    code = random.choices(colors, k=4)  # Generate a random code of 4 colors
    return code

def evaluate_guess(code, guess):
    correct_color_and_position = 0
    correct_color_only = 0

    for i in range(len(code)):
        if guess[i] == code[i]:
            correct_color_and_position += 1
        elif guess[i] in code:
            correct_color_only += 1

    return correct_color_and_position, correct_color_only

def MastermindGame():
    code = generate_code()
    attempts = 0

    print("Welcome to Mastermind!")
    print("Guess the 4-color code (R, G, B, Y, O, P).")

    while True:
        guess = input("Enter your guess: ").upper()

        if len(guess) != 4 or any(color not in 'RGBYOP' for color in guess):
            print("Invalid guess. Please enter a valid 4-color code.")
            continue

        attempts += 1
        correct_color_and_position, correct_color_only = evaluate_guess(code, guess)

        if correct_color_and_position == 4:
            print(f"Congratulations! You guessed the code in {attempts} attempts.")
            break
        else:
            print(f"Correct color and position: {correct_color_and_position}")
            print(f"Correct color only: {correct_color_only}")

MastermindGame()
