from words import palabras
import colorama
from colorama import Fore,init
init()
import random
colors = list(vars(colorama.Fore).values())

print("Welcome to the Hangman game, let's play (;")
print("Guess the word or phrase\n")

def good_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

word = good_word(palabras)

#print (word)
for i in word:
    colored_chars = [random.choice(colors) + " _ "]
    print(" ".join(colored_chars),end="")
#print(" - p"*len(word))
print("")