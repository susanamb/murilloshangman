from words import palabras
import random

print("Welcome to the Hangman game, let's play (;")
print("Guess the word or phrase\n")

word = random.choice(palabras)

for i in word:
    if i == "-":
        print(" -",end=" ") #poner el guion en caso necesario
    else:    
        print(" _ ",end="")

print("")
