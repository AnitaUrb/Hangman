# Hangman

A simple version of the popular [Hangman](https://en.wikipedia.org/wiki/Hangman_(game)) game with the only difference that the program uses a randomly selected word from a limited set of words. That set of words that can be used in the game are placed in *.txt* file separated by new line. Sample file: *"list_of_words.txt"*. <br />

The *"game_flow.txt"* file contains drawings of the game progress, cannot be changed and should be downloaded in the same directory as the *"hangman.py"* file. <br />

User follows the instructions on the screen, like *"Enter your letter"*; additional information like number of attempts is also displayed. Program is *case-sensitive*.<br />

To start the game:<br />

call:~$ *path_to_hangman.py path_to_file_with_words*<br />

Note: Requires *Python3* (otherwise user input errors will be generated).<br />

Comments concerning the flow of the game are placed in the code.
