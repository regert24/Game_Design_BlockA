#using random numbers
#guess a number

import os
import random 

os.system('cls')

# random.seed(20)
# for i in range(10):
#     randy = random.randint(3,5)
#     print(randy)
#     randy2 = random.randint()
#     randy2 *= 100
#     print(int(randy2))

# fruits=["apple", "banana", "berries"]
# myFruit= random.choice(fruits)
# print(myFruit)

randy=random.randint(1,50)
print("You have 5 tries to guess the number")
for counter in range(10):
    guess=input("give me a number")
    if guess == randy:
        print("you got it")
        break
    else: ("Not quite..")

print(randy)
    

