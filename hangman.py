import random
import sys

steps = ['''
       _
       |     
       |    
       |    
       |    
       |
       |
       |
=========== ''',
''' 
     ___
       |     
       |    
       |    
       |    
       |
       |
       |
=========== ''',
'''
   _____
       |     
       |    
       |    
       |    
       |
       |
       |
=========== ''',
'''
 _______
       |     
       |    
       |    
       |    
       |
       |
       |
=========== ''',
'''
 _______
 |     |     
       |    
       |    
       |    
       |
       |
       |
=========== ''',

'''
 _______
 |     |     
 O     |    
       |    
       |    
       |
       |
       |
=========== ''',
'''
 _______
 |     |
 0     |
/      |
       |
       |
       |
       |
=========== ''',
'''
 _______
 |     |
 0     |
/|     |
       |
       |
       |
       |
=========== ''',

'''
 _______
 |     |
 0     |
/|\    |
       |
       |
       |
       |
=========== ''',
'''
 _______
 |     |
 0     |
/|\    |
/      |
       |
       |
       |
=========== ''',
'''
 _______
 |     |
 0     |
/|\    |
/ \    |
       |
       |
       |
=========== ''',]

print ("HANGMAN\nNOTE! You have 10 chances to guess.")

# Ponizszy kawalek mozna uruchomic w przypadku, gdyby sie mialo zapisane wszystkie powyzsze obrazki w
# pliku (niestety, nie moge go zalaczyc)
# (w tym pliku obrazki sa rozdzielone przecinkami)
#with open("tok.txt", "r") as f:
#    lines = f.read().split(',')
#    steps = list(lines)
#    print (steps[0])

# Drukujemy obrazek poczatkowy
print (steps[0])

# Plik ze slowami, podany jako argument, bedzie przeczytany i zostanie wylosowane slowo
with open(sys.argv[1], "r") as f:
    lines = f.readlines()
    nl_number = len(lines)
    rand_line = random.randint(0, nl_number)
    word = lines[rand_line - 1].strip()


word_length = len(word)
covered = "_" * word_length
chances = 10

print (covered, "[", word_length, "liter ]")
print ("Podaj litere by zgadnac slowo.\n")

# Tok gry (sprawdzanie, czy podana litera jest "poprawna" i nastepujace zwiazane z tym operacje
# outputu
# k - zmienna do iteracii po obrazkach
k = 0
wykorzystane_litery = []
# dopoki uzytkownik nie wykorzysta wszystkich szans:
while chances:
    letter = input("Podales: ")
    if letter in word:
        wykorzystane_litery.append(letter)
        print ("Zgadles juz: ", wykorzystane_litery)
        for i in range(len(word)):
            if letter == word[i]:
                covered_list = list(covered)
                covered_list[i] = word[i]
                covered = "".join(covered_list)
            if "_" not in covered:
                print ("BRAVO! Wygrales!")
                sys.exit("Szukanym slowem bylo: " + covered)
    else:
        k += 1
        chances -= 1
        print ("Zla literka. Tracisz szanse (masz obecnie:", chances, ")")
        print ("Zgadles juz: ", wykorzystane_litery)

# ponizsze drukowanie pozwala uzytkownikowi widziec, jak  mu idzie
    print (covered)
    print (steps[k])

# jesli uzytkownik wczesniej nie zgadl slowa i nie skonczyl, to poniewaz
# wykorzystal wszystkie szanse, to przegral (rukuje sie odpowiedni komunikat)
print ("PRZEGRALES. Szukanym slowem bylo:", word)
