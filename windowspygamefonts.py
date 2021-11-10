#tom reger
#learn fonts

import os, pygame, random
os.system('cls')

pygame.init()
py=pygame
#Colors and their values

red=(255,0,0)
green=(0,255,0) 
blue=(0,0,255)
purple=(150,0,150) 
yellow=(255,255,0)
black = (0,0,0)
white=(255,255,255)
width=800
height = 800
COLOR=white
flag=False
Setting_messages1 = ["SCREEN SIZE", "BACKGROUND COLOR","OBJECT COLOR","SOUNDS (ON/OFF)"]    #Setting Messages
Menu_messages=["Instructions", "Level 1", "Level 2", "Settings", "Scoreboard", "Exit"]
win = pygame.display.set_mode((width,height))
win.fill(blue)
pygame.display.set_caption("Setting Window")

#Fonts 
title_font=pygame.font.SysFont('comicsans',80)
subtitle_font=pygame.font.SysFont('comicsans',30, italic=True)

#Square
hbox = 25
wbox = 25
square = pygame.Rect(10,10, wbox, hbox)

def displayTitle(title, yt):    #Title print function
    pygame.time.delay(100)
    text = title_font.render(title,1,red)
    #win.blit(text,(width/2-text.get_width()/2, height/2-text.get_height()/2))
    win.blit(text,(width/2-text.get_width()/2,yt))
    pygame.display.update()
    pygame.time.delay(100)

def displayMenu(message):  #Subtitle print function
    pygame.time.delay(100)
    x = 70
    y = 190
    square.x = x
    square.y = y
    for i in range (0, len(message)):
        word = message[i]
        pygame.draw.rect(win, purple, square)
        text = subtitle_font.render(word,1,red)
        win.blit(text,(x+wbox+10, y-10))
        pygame.display.flip()
        pygame.time.delay(100)
        y +=100
        square.y = y
Jumping=False
jumpCount=10




run=True
count = 0
displayTitle("Menu", 40)
displayMenu(Menu_messages)
while run:
    pygame.time.delay(10)
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run=False
    if eve.type==py.MOUSEBUTTONDOWN:
        mouse_pressed=py.mouse.get_pressed()
        if mouse_pressed[0]:
            mouse_pos=py.mouse.get_pos()
            if square.collidepoint(mouse_pos):
                win.fill(green)
        
        mouse_pressed=py.mouse.get_pressed()
        mouse_pos=py.mouse.get_pos()
        #print(mouse_pos)
        y_min=190
        y_max=212

        y_min2=291
        y_max2=312

        y_min3=390
        y_max3=413

        y_min4=491
        y_max4=514
        if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min and mouse_pos[1]<=y_max and count==0:
            win.fill(white)
            displayTitle("Instructions", 40)
            displayTitle("Back", height-100)
            count=1
        if mouse_pos[0]>=320 and mouse_pos[0]<=485 and mouse_pos[1]>=height-100 and mouse_pos[1]<=height and (count==1 or count==2 or count ==3 or count==5 and count==9 and count==4):
            win.fill(white)
            displayTitle("Menu", 40)
            displayMenu(Menu_messages)
            count=0



           
        #if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min2 and mouse_pos[1]<=y_max2:

           
        # if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min3 and mouse_pos[1]<=y_max3:
         
        if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min4 and mouse_pos[1]<=y_max4 and count==0:
            win.fill(COLOR)
            displayTitle("Settings", 40)
            displayMenu(Setting_messages1)
            displayTitle("Back", height-100)
            count=4
            
        if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min4 and mouse_pos[1]<=y_max4 and count==4:
            win.fill(COLOR)
            displayTitle("Sound", 40)
            displayTitle("Back", height-100)
            count=9
            flag=True
            print(count)
    
#count=0 main menu
#count 1 Instructions
#count 2 level 1  
#count 3 level 2 
#count 4 settings 
#count 5 score

    #x,y=pygame.mouse.get_pos()
   #print("( "+ str(x)+ ", "+ str(y)+" )")
    #pygame.quit()

