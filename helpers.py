"""
Helper Functions for Hangman CLI
"""

from random import choice # Built-in Modules

# Helper Functions
def read_file(filename: str) -> list:
    """
    Reads a Given Text File (individual words separated by newlines)\n
    and Returns a List of Words
    """
    words = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            words.append(line.strip())
    return words

def random_word(words: list) -> str:
    """
    Chooses a Word from a List of Words\n
    and Returns Chosen Word (str)
    """
    return choice(words)

def repr_word(secret_word: list) -> None:
    word = [char for char in secret_word]
    word_length = len(word)
    edge = f'+{"-" * (word_length * 2 + 1)}+'
    middle = f'| {" ".join(word)} |'
    print(edge + "\n" + middle + "\n" + edge)

# Function Testing
if __name__ == "__main__":
    pass
    # testing read_file() function:
    # words_list = read_file("words.txt")
    # print(words_list)
    # testing random_word() function:
    # for _ in range(5):
    #     word = random_word(words_list)
    #     print(word)
