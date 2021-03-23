from words import palabras
import random
import colorama #c
from colorama import Fore,init#c
init()#c
colors = list(vars(colorama.Fore).values())#c lista de colores
lives_pic = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
lives = 0

def good_word(words):
        word = random.choice(words)
        while '-' in word or ' ' in word:
            word = random.choice(words)
        return word

print("\nWelcome to the Hangman game, let's play (;")
word = good_word(palabras).upper()
word_list = list(word) #separa las letras en una lista
count_letters = len(word_list) #cantidad de letras a adivinar

while count_letters > 0 or lives == 6:
    print("Guess the word or phrase")

    print(word_list)
    for i in word_list:
        if i.isupper():
            #print(" _ ",end="")
            colored_chars = [random.choice(colors)+ " _ " ]#random color
            print(" ".join(colored_chars),end="") #c 
            
        else:
            print(i,end="")

    print("")

    letter = input("\nLetter: ").upper()
    if letter.isalpha() and len(letter) == 1:
        con = 0
        for i in range(len(word_list)):          
            if letter == word_list[i]:
                word_list[i] = letter.lower()
                con = con + 1
        if con == 0:
            lives = lives + 1 
        else:                
            count_letters = count_letters - con #letra menos           
            #print("Bien!, te faltan solo ",count_letters)

        print(lives_pic[lives])
        if lives == 6:
            print("U lose!")
            break
            
        if count_letters == 0:
            print("Great! U WIN!")
    else:
        print("Invalid input, try again")  
        print("Remember, type only one letter")

                
