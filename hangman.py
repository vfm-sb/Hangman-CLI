"""Hangman CLI"""

__author__ = "VFM | SB"
__email__ = "vfm_sb@proton.me"
__copyright__ = "Copyleft 2022"
__license__ = "MIT"
__version__ = "0.2.4"
__maintainer__ = "VFM | SB"
__status__ = "Development"

import os # Built-in Modules

from helpers import read_file # Local Modules
from helpers import random_word
from art import LOGO, STAGES


# Functions
def repr_word(secret_word: list) -> None:
    word = [char for char in secret_word]
    word_length = len(word)
    edge = f'+{"-" * (word_length * 2 + 1)}+'
    middle = f'| {" ".join(word)} |'
    print(edge + "\n" + middle + "\n" + edge)

# Main Function
def main():
    print(LOGO, " " * 18 ,__version__, "\n", sep="")
    # get a random word
    chosen_word = random_word(read_file("words.txt"))
    word_length = len(chosen_word)
    secret_word = ["_" for _ in range(word_length)]
    # test
    # print(f"Solution is {chosen_word}")
    repr_word(secret_word)
    print()
    end_of_game = False
    lives = 7
    chosen_chars = []
    while not end_of_game:
        chosen_char = input("Guess a Letter: ").lower()
        os.system("clear")
        # check if character already guessed before:
        if (
            chosen_char in secret_word
            or chosen_char in chosen_chars
        ):
            print(f'You\'ve Already Guessed Letter "{chosen_char}" Before!\n')
            repr_word(secret_word)
            print(STAGES[lives])
            continue
        chosen_chars.append(chosen_char)
        occurances = 0
        for i in range(word_length):
            if chosen_char == chosen_word[i]:
                secret_word[i] = chosen_char
                occurances += 1
        # if given character not found in the secret_word,
        # reduces lives by 1
        if chosen_char not in chosen_word:
            print(
                f'The Letter "{chosen_char}" was not Found! '
                "You've Lost a Life!"
            )
            lives -= 1
        else:
            print(
                f'The Letter "{chosen_char}" was Found in {occurances} '
                f'{"Place" if occurances < 2 else "Different Places"}.'
            )
        # if no more lives left, end_of_game = True,
        # game is lost
        if lives == 0:
            end_of_game = True
            print("You've Lost!")
            print()
            print("The Word was:")
            repr_word(list(chosen_word))
        else:
            print()
            repr_word(secret_word)
        # if all characters guessed correctly, end_of_game = True,
        # game is won
        if "_" not in secret_word:
            end_of_game = True
            print("You've Won!")
        # display respective hangman art
        print(STAGES[lives])


# Execute
main()
