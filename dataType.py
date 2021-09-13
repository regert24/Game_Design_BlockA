# Tom Reger
# 09/13/2021

# This is about data types
# how strings work

import os
os.system('cls')

# int - 4 bytes 
# long - 8 bytes 
# float - 4 bytes 
# double - bytes 
# boolean T-F

userInput=input("type something")
print (type(userInput))
try:
    int(userInput)
    check=True
except ValueError:
    check=False
print(check)

if (check):
    print()
else:
    print(len(userInput))
for i in userInput:
    print(i) 
if len(userInput>3):
    print(userInput[3])





# if(type(userInput)==int):
#     print("you gave me an integer")
# else:
#     print("your input is not an integer")


