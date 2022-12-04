# Hangman-CLI

A Generic Hangman Game on CLI

<br>

## How Hangman Game Works?

Hangman is a word guessing game. 
Computer randomly chooses a word from the available words. Currently there are over 200 words.
The player tries to guess the word by suggesting letters within a curtain number of guesses. In the current version of Hangman-CLI, 7 lives are available for the player.
If player finds the word before running out of 7 lives, the player wins the game.
If player cannot find the word before running out of lives, the player loses the game.

<br>

## Road Map

- Variable Lives
	- Based on Regular Difficulty (easy, normal hard)
	- Based on Characters Count (lives = len(secret_word))
	- Based on Complexity of the Secret Word

<br>

## License

Distributed under the MIT License. See `LICENSE` file for more information.