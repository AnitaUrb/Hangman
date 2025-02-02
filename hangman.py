import random
import sys


print ("HANGMAN GAME\nYou have 10 attempts to guess.\nAttention! Program is case-sensitive.\n")


# loading drawings from "game_flow.txt" file and printing the initial one:
with open("game_flow.txt", "r") as f:
   lines = f.read().split(',')
   steps = list(lines)
   print (steps[0])


# The file containig words given as the argument will be read and the word to guess will be drawn:
with open(sys.argv[1], "r") as f:
    lines = f.readlines()
    nl_number = len(lines)
    rand_line = random.randint(0, nl_number)
    word = lines[rand_line - 1].strip()


word_length = len(word)
covered = "_" * word_length
chances = 10

print (covered, "[", word_length, "letters ]")
print ("Enter the letters to guess the word.\n")

# Game flow (checking is the entered letter is "correct" and the following output operations: 
# k - drawing iteration variable
k = 0
used_letters = []
# until the user seizes all the chances:
while chances:
    letter = input("Enter your letter: ")
    if letter in word:
        for i in range(len(word)):
            if letter == word[i]:
                covered_list = list(covered)
                covered_list[i] = word[i]
                covered = "".join(covered_list)
            if "_" not in covered:
                print ("WELL DONE! You won!")
                sys.exit("The covered word was: " + covered)
        used_letters.append(letter)
        print ("Good! Already guessed letters: ", used_letters)
    else:
        k += 1
        chances -= 1
        print ("Bad letter :(. Attempts left:", chances)
        print ("Already guessed: ", used_letters)

# the printing below allows the user to see how he is doing
    print (covered)
    print (steps[k])

# if the user did not guess the word and finished,
# the following message will be printed:

print ("YOU LOST.\nThe covered word was:", word)
