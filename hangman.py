from words import palabras
import random

print("Welcome to the Hangman game, let's play (;")
print("Guess the word or phrase\n")

def good_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

for i in good_word(palabras):
    print(" _ ",end="")

print("")
