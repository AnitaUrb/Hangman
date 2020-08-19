import random
import sys


print ("HANGMAN\nNOTE! You have 10 chances to guess.")


# loading images from file and printing the initial image
with open("game_flow.txt", "r") as f:
   lines = f.read().split(',')
   steps = list(lines)
   print (steps[0])


# The file containig words given as the argument will be read and the word will be drawn
with open(sys.argv[1], "r") as f:
    lines = f.readlines()
    nl_number = len(lines)
    rand_line = random.randint(0, nl_number)
    word = lines[rand_line - 1].strip()


word_length = len(word)
covered = "_" * word_length
chances = 10

print (covered, "[", word_length, "liter ]")
print ("Enter a letter to guess a word.\n")

# Game flow (checking is the specified letter is "correct" and the following output operations 
# k - image iteration variable
k = 0
wykorzystane_litery = []
# until the user seizes all the chances:
while chances:
    letter = input("Enter a letter: ")
    if letter in word:
        wykorzystane_litery.append(letter)
        print ("You already guessed: ", wykorzystane_litery)
        for i in range(len(word)):
            if letter == word[i]:
                covered_list = list(covered)
                covered_list[i] = word[i]
                covered = "".join(covered_list)
            if "_" not in covered:
                print ("BRAVO! You win!")
                sys.exit("The searched word was: " + covered)
    else:
        k += 1
        chances -= 1
        print ("Bad letter. You're losing your chances (you currently have:", chances, ")")
        print ("You already guessed: ", wykorzystane_litery)

# the printing below allows the user to see how he is doing
    print (covered)
    print (steps[k])

# if the user did not guess the word before and finished  because
# he used all the chances, he lost (an appropriate message is printed)

print ("YOU LOST. Searched word was:", word)
