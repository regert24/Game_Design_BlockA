#Tom Reger
#Guesing game complete
#10/3/2021

import os
import random 
os.system('cls')

def updateWord(randWord,guesses):
    for letter in randWord:
        if letter in guesses:
            print (letter,end=" ")
        else:
            print("_",end=" ")

def menu():
    print("####################################################")
    print("#    This is a guessing game! Choose a category!   #")
    print("#                                                  #")
    print("#                       MENU                       #")
    print("#                                                  #")
    print("#                   1. ANIMALS                     #")
    print("#                   2. FRUITS                      #")
    print("#                   3. COMP PARTS                  #")
    print("#                   4. EXIT                        #")
    print("#                                                  #")
    print("# To play the game, select 1-3, to exit, select 4. #")
    print("#                                                  #")
    print("####################################################")
    print()
    sel=input("What would you like to play? ")
    try:
        sel = int(sel)  #Tries if it is an integer
        if sel < 5 and sel > 0:
            check = True
            return sel
    except ValueError:
        print("Give me a number from 1 - 4. Try Again")
        sel=input("What would you like to play? ")
        check = False
        
def selWord(sel):
    if sel == 1:
        randWord = random.choice(animals)
    if sel == 2:
        randWord = random.choice(fruits)
    if sel == 3:
        randWord = random.choice(compParts)
    return randWord

animals = ["tiger","elephant","monkey","lion","zebra","panther","rhino","dog","cat","bird","fish"]
compParts = ["keyboard","monitor","computer","case","trackpad","headphone","motherboard","microphone"]
fruits = ["peach","apple","orange","grape","cherry","watermelon","banana","strawberry","blueberry","mango"]

name = input("What is your name? ")
maxScore = 0
sel = menu()
game = "y"
while sel!=4 and ("Y" and "y" in game):
    randWord = selWord(sel)
    randWord = randWord.lower()
    wordCount = len(randWord)
    turns = len(randWord) + 3
    print("Good Luck ",name,"! You have ", turns," lives")
    print (randWord)
    guesses = ""
    updateWord(randWord,guesses)
    letCount = 0

    while turns > 0 and letCount<wordCount:
        letCount = 0
        print()
        newGuess = input("Guess a letter: ")
        newguess = newGuess.lower()
        if newGuess in randWord:
            guesses+=newGuess
            print("You guessed a correct letter!")
        else:
            turns -= 1
            print("That is not in the word. You have ", turns, " lives left")
        for letter in randWord:
            if letter in guesses:
                print (letter,end=" ")
                letCount+=1
            else:
                print("_",end=" ")

    if turns == 0:
        print("You lose!")
    else:
        print()
        print("You win!")
    os.system('cls')
    score = 3*wordCount+5*turns
    if score>maxScore:
        maxScore = score
    print (maxScore)
    game = input("Do you want to play again? Type Y for yes or N for no: ")
    if ("Y" and "y" in game):
        sel = menu()
    if ("n" and "N" in game):
        sel = 4

print("Thank you for playing!")
