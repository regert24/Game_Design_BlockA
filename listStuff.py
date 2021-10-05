#Tom Reger
# Collections in py

import random, os

def updateWord(word, guesses):
  for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print('_', end=' ')
#define func for mmenu
def Menu():
    print("# instructions#")
    print("# Menu ##")
    print("      1. Animals             ")
    print("      2. Fruits              ")
    print("      3. Computer Parts      ")
    print("      4. Exit                ")
    sel=input("What would you like to play?")
    sel=int(sel)
    return sel
def selWord(sel):
    if sel == 1:
        word=random.choice(animals)
    elif sel ==2:
        word=random.choice(myfruits)
    else:
        word=random.choice(compParts)

animals=["tiger, elephant"]
myfruits = ["apple","bananas","oranges","grapes","strawberries","blackberries","blackberries"]
compParts=["keyboard, computer"]


print("Word Game")
print("Guess what fruit I am thinking of")
name=input("What is your name?")
counter=0
sel=Menu()
while sel !=4:
    print(name, "good luck, you have 5 chances")
    turns=5
    counter +=1
    word= random.choice(myfruits)
    word=word.lower()
    print(word) #revove later
    guesses=''
    updateWord(word, guesses)
    while turns>0:
        newguess=input("Give me a letter")
        newguess=newguess.lower()
        if newguess in word:
            guesses += newguess
            print("You guessed right")
        else:
            turns -=1
            print ("Sorry you have", turns, "left")
answer=input(name+ "do you want to play again")
    sel=Menu()























# for x in MyFruits:
#     print (x)
# for x in MyFruits[0]:
#     print( "_", end="")
