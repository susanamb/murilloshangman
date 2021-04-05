from words import palabras,lives_pic
import random
import colorama 

colors = list(vars(colorama.Fore).values())#list of colors
lives = 0 #initialize lives
def good_word(words): # choose a word
        word = random.choice(words)
        while '-' in word or ' ' in word:
            word = random.choice(words)
        return word

print("\nWelcome to the Hangman game, let's play (;")
word = good_word(palabras)
word_list = list(word.upper()) #set and split the words all uppercase
count_letters = len(word_list) #letters to guess
used_letters = set()#used letters

while count_letters > 0 or lives == 6:
    print("Guess the word or phrase")
    print(used_letters)
    print(word_list)
    for i in word_list:
        if i.isupper():
            colored_chars = [random.choice(colors)+ " _ " ]#choose random color
            print(" ".join(colored_chars),end="") #print the colored lines          
        else:
            print(i,end="") #print the guessed letters
    print(colorama.Style.RESET_ALL + " ")

    letter = input("\nLetter: ").upper() # INPUT
    repeat_letter = True
    if letter in used_letters: #if the letter is repeated
            print("U already try with that one")
            repeat_letter = False

    if letter.isalpha() and len(letter) == 1: #validate the input
        con = 0 #initialize guess counter
        used_letters.add(letter)
        
        for i in range(len(word_list)):          
            if letter == word_list[i]: #if guess the letter
                word_list[i] = letter.lower()
                con = con + 1 # num of letters guessed

        if con == 0 and repeat_letter: #not guess and no repeat letter
            lives = lives + 1 #lose a live
        else:                
            count_letters = count_letters - con #letra menos           

        print(lives_pic[lives])
        if lives == 6: # if u run out of lives
            print("U lose! The word was: ", word)
            break
            
        if count_letters == 0: #if there's no more letters to guess
            print(word, " Great! U WIN!")
            
    else: #invalid input
        print("Invalid input, try again")  
        print("Remember, type only one letter")

                
