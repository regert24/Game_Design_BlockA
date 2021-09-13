# Tom Reger
# 09/07/2021
# We are going to learn how to loop

import os

os.system('cls')

star = int(input("How many stars")) #input always gives you a string
# type casting = changing the type of data
print("stars", star)
line=star
for x in range(line):
    for counter in range(star):
        print("*", end="")
        #print(counter+1, end=" ") #print on the same line
    print() #print a return to create a new line
    star-=1
print("Thank you ")

