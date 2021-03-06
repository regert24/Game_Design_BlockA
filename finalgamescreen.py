from typing import Text
import pygame as py
import os
os.system('cls')
py.init()

HEIGHT=394
WIDTH=900
run=True
clock=py.time.Clock()
py.init()
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
Setting_messages1 = ["BACKGROUND COLOR","WINDOW SIZE"]    #Setting Messages
WindowMessages= ["900x900", "1000x1000", "800x800"]
Menu_messages=["Instructions", "Level 1", "Level 2", "Settings", "Scoreboard", "Exit"]
win = py.display.set_mode((width,height))
win.fill('black')
py.display.set_caption("Setting Window")
walkRight = py.image.load('images\Pygame-Tutorials-master\Game\\R1.png')
walkLeft = py.image.load('images\Pygame-Tutorials-master\Game\\L1.png')
#Fonts 
title_font=py.font.SysFont('comicsans',80)
subtitle_font=py.font.SysFont('comicsans',30, italic=True)
text_font=py.font.SysFont('comicsans',30)

walkCount=0

#Square
hbox = 25
wbox = 25
square = py.Rect(10,10, wbox, hbox)



def displayTitle(title, yt):    #Title print function
    py.time.delay(100)
    text = title_font.render(title,1,COLOR)
    #win.blit(text,(width/2-text.get_width()/2, height/2-text.get_height()/2))
    win.blit(text,(width/2-text.get_width()/2,yt))
    py.display.update()
    py.time.delay(100)

def displayMenu(message):  #Subtitle print function
    py.time.delay(100)
    x = 70
    y = 190
    square.x = x
    square.y = y
    for i in range (0, len(message)):
        word = message[i]
        py.draw.rect(win, red, square)
        text = subtitle_font.render(word,1,COLOR)
        win.blit(text,(x+wbox+10, y-10))
        py.display.flip()
        py.time.delay(100)
        y +=100
        square.y = y

def displayText(text,yu):    #Text function
    py.time.delay(100)
    text = text_font.render(text,1,COLOR)
    #win.blit(text,(width/2-text.get_width()/2, height/2-text.get_height()/2))
    win.blit(text,(width/2-text.get_width()/2,yu))
    py.display.update()
    py.time.delay(100)


# def level1_game():
#     bg=py.image.load("images\\volcanofinal.jpg")
#     win = py.display.set_mode((WIDTH,HEIGHT))
#     py.display.set_caption("Final Game")
#     win.blit(bg,(0,0))
#     win.blit(walkRight, (0,0))
#     py.display.flip()
#     boulder=py.Rect(WIDTH-300, HEIGHT-300, 100, 300)
def level1_game():
    win = py.display.set_mode((WIDTH,HEIGHT))
    bg=py.image.load("images\\volcanofinal.jpg")
    char = py.image.load('images\Pygame-Tutorials-master\Game\standing.png') 
    x = 100
    y = 100
    width = 40
    height = 60
    vel = 5
    
    clock = py.time.Clock()

    isJump = False
    jumpCount = 10

    left = False
    right = False
    walkCount = 0


    def redrawGameWindow():
        global walkCount
        win.blit(bg, (0,0))  
        if walkCount + 1 >= 27:
            walkCount = 0
            
        if left:  
            win.blit(walkLeft[walkCount//3], (x,y))
            walkCount += 1                          
        elif right:
            win.blit(walkRight[walkCount//3], (x,y))
            walkCount += 1
        else:
            win.blit(char, (x, y))
            walkCount = 0
            
        py.display.update() 
        

    run = True

    while run:
        #print(pygame.mouse.get_pos())

        clock.tick(27)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        keys = py.key.get_pressed()
        
        if keys[py.K_LEFT] and x > vel: 
            x -= vel
            left = True
            right = False

        elif keys[py.K_RIGHT] and x < 600 - vel - width:  
            x += vel
            left = False
            right = True
            
        else: 
            left = False
            right = False
            walkCount = 0
            
        if not(isJump):
            if keys[py.K_SPACE]:
                isJump = True
                left = False
                right = False
                walkCount = 0
        else:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            else: 
                jumpCount = 10
                isJump = False
        win.blit(bg, (0,0))

        #if x<50:
        #  Left=False
    #  if x>300:
        #  Right=False
        redrawGameWindow() 
        
    py.quit()








def level2_game():
    bg=py.image.load("images\\volcanofinal.jpg")
    win = py.display.set_mode((WIDTH,HEIGHT))
    py.display.set_caption("Final Game")
    win.blit(bg, (0,0))
    py.display.flip()

Jumping=False
jumpCount=10

Mainmenu=1
settings=2
bgcolor=3
page=Mainmenu
windowsettings=4

run=True
count = 0
displayTitle("Menu", 40)
displayMenu(Menu_messages)
while run:
    py.time.delay(10)
    for eve in py.event.get():
        if eve.type == py.QUIT:
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
        if page==Mainmenu:
            if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min and mouse_pos[1]<=y_max and count==0:
                win.fill(black)
                displayTitle("Instructions", 40)
                displayText("Jump across the rocks before the volcano explodes",160)
                displayText("Don't touch the lava!", 200)
                displayTitle("Back", height-100)
                count=1
            if mouse_pos[0]>=320 and mouse_pos[0]<=485 and mouse_pos[1]>=height-100 and mouse_pos[1]<=height and (count==1 or count==2 or count ==3 or count==5 or count==9 or count==4):
                win.fill(black)
                displayTitle("Menu", 40)
                displayMenu(Menu_messages)
                count=0

            
            if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min2 and mouse_pos[1]<=y_max2:
                level1_game()

            
            if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min3 and mouse_pos[1]<=y_max3:
                level2_game()

            if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min4 and mouse_pos[1]<=y_max4:
                win.fill(black)
                displayTitle("Settings", 40)
                displayMenu(Setting_messages1)
                displayTitle("Back", height-100)
                page=settings
        if page == settings:
            if mouse_pos[0]>=320 and mouse_pos[0]<=485 and mouse_pos[1]>=height-100 and mouse_pos[1]<=height:
                win.fill(black)
                displayTitle("Menu", 40)
                displayMenu(Menu_messages)
                count=0
                page=Mainmenu

        if page==settings:
            if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min and mouse_pos[1]<=y_max and count==0:
                win.fill(black)
                displayTitle("Background Color",40)
                page = bgcolor
                displayTitle("Back", height-100)
            if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min2 and mouse_pos[1]<=y_max2 and count==0:
                win.fill(black)
                displayTitle("Window size",40)
                displayMenu(WindowMessages)
                displayTitle("Back", height-100)
                page = windowsettings
        if page==windowsettings:
            if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min and mouse_pos[1]<=y_max and count==0:
                win=py.display.set_mode((900, 900))
                win.fill(black)
                displayTitle("Window size",40)
                page = windowsettings

                displayMenu(WindowMessages)
                displayTitle("Back", height-100)
                py.display.update
                page=settings
            if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min2 and mouse_pos[1]<=y_max2 and count==0:
                win=py.display.set_mode((1000, 1000))
                win.fill(black)
                displayTitle("Window size",40)
                page = windowsettings
                displayMenu(WindowMessages)
                displayTitle("Back", height-100)
                py.display.update
                page=settings
            if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min3 and mouse_pos[1]<=y_max3 and count==0:
                win=py.display.set_mode((800, 800))
                win.fill(black)
                displayTitle("Window size",40)
                
                displayMenu(WindowMessages)
                displayTitle("Back", height-100)
                py.display.update
                page=settings
        # #if page == bgcolor or windowsettings:
        #     if mouse_pos[0]>=320 and mouse_pos[0]<=485 and mouse_pos[1]>=height-100 and mouse_pos[1]<=height:
        #         win.fill(black)
        #         displayTitle("Settings", 40)
        #         displayMenu(Setting_messages1)
        #         count=0
        #         page=settings
        #         displayTitle("Back", height-100)
    mouse_pos = (0,0)
            

#Credit to vivaan for the code determining the mouse position to click the button
