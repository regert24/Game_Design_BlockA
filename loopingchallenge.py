star = int(input("How many stars")) 
print("stars", star)
line=star
for I in range (line):
    for space in range (I):
        print("   ", end=" ")
    for counter in range(star):
       print(" * ", end=" ")
    print() 
    star-=1
print("Thank you ")

