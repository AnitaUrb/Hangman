# Hangman

A simple version of the popular [Hangman](https://en.wikipedia.org/wiki/Hangman_(game)) game with the only difference that the game uses a randomly selected word from a limited set of words. That set of words that can be used in the game are placed in .txt file separated by new line. Example file: *list_of_words.txt*. <br />

*game_flow.txt* file contains drawings of the game progress, it should be immutable and downloaded to the same direction as the *hangman.py* file. <br />

User follows the instructions displayed on the screen, like *"Enter your letter"*; additional information like number of attempts is also displayed. Program is *case-sensitive*.<br />

To start the game:<br />

call:~$ *path_to_hangman.py file_with_words*

Note: requires *Python3* (otherwise errors related to user input will be produced).

Comments concerning the flow of the game are placed in the code.
