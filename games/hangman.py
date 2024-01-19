# simple hangman game in python 3.12

import random

def HangmanGame():
    words = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(words)
    word_set = set(word)
    guessed_letters = set()
    tries = 8

    print("H A N G M A N")

    while tries > 0:
        print()
        print("".join([letter if letter in guessed_letters else "-" for letter in word]))

        letter = input("Input a letter: ")

        if len(letter) != 1:
            print("You should input a single letter")
            continue

        if letter in guessed_letters:
            print("You already typed this letter")
            continue

        if letter not in "abcdefghijklmnopqrstuvwxyz":
            print("It is not an ASCII lowercase letter")
            continue

        guessed_letters.add(letter)

        if letter in word_set:
            if word_set == guessed_letters:
                print("You guessed the word!")
                print("You survived!")
                break
        else:
            print("No such letter in the word")
            tries -= 1

    else:
        print("You are hanged!")

HangmanGame()