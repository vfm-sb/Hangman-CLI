"""
Helper Functions for Hangman CLI
"""

from random import choice # Built-in Modules

# Helper Functions
def read_file(filename: str) -> list:
    words = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            words.append(line.strip())
    return words

def random_word(words: list) -> str:
    return choice(words)



# Function Testing
if __name__ == "__main__":
    # testing read_file() function:
    words_list = read_file("words.txt")
    # print(words_list)
    # testing random_word() function:
    for _ in range(5):
        word = random_word(words_list)
        print(word)