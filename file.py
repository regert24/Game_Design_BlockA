import os, time
os.system('cls')


myFile=open('score.txt', 'w')
myFile.write("Hello, my name is Tom \t what is yours")
myFile.close()

myFile=open('score.txt', 'w')
myFile.write("and now we will play a game")
myFile.close()

fileMy=open('score.txt', 'r')
print(fileMy.read())
fileMy.close()
score=450
anotherFile=open('score.txt', 'a')
anotherFile.write("\n The highest score: \t" + str(score))
anotherFile.close()
