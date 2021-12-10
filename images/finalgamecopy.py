from typing import Text
import pygame as py
import os
position = 150,150
os.environ['SDL_VIDEO_WINDOW_POS'] = str(position[0]) + "," + str(position[1])
from pygame.constants import MOUSEBUTTONDOWN
os.system('cls')
py.init()
width2 = 40
height2 = 60

width3=700
height3=800
HEIGHT=394
screen=py.display.set_mode((width3, height3))
WIDTH=900
run=True
clock=py.time.Clock()
#Colors and their values
boulder=py.Rect(WIDTH-300, HEIGHT-300, 100, 50)
red=(255,0,0)
green=(0,255,0) 
blue=(0,0,255)
purple=(150,0,150) 
yellow=(255,255,0)
black = (0,0,0)
white=(255,255,255)
width=800
height = 800
isJump = False
COLOR=white
flag=False
Setting_messages1 = ["BACKGROUND COLOR","WINDOW SIZE"]    #Setting Messages
WindowMessages= ["900x900", "1000x1000", "800x800"]
Menu_messages=["Instructions", "Level 1", "Level 2", "Settings", "Scoreboard", "Exit"]
bg_messages=["Red","Blue", "Green", "Black"]
walkRight = [py.image.load('images\Pygame-Tutorials-master\Game\R1.png'), py.image.load('images\Pygame-Tutorials-master\Game\R2.png'), py.image.load('images\Pygame-Tutorials-master\Game\R3.png'), py.image.load('images\Pygame-Tutorials-master\Game\R4.png'), py.image.load('images\Pygame-Tutorials-master\Game\R5.png'), py.image.load('images\Pygame-Tutorials-master\Game\R6.png'), py.image.load('images\Pygame-Tutorials-master\Game\R7.png'), py.image.load('images\Pygame-Tutorials-master\Game\R8.png'), py.image.load('images\Pygame-Tutorials-master\Game\R9.png')]
walkLeft = [py.image.load('images\Pygame-Tutorials-master\Game\L1.png'), py.image.load('images\Pygame-Tutorials-master\Game\L2.png'), py.image.load('images\Pygame-Tutorials-master\Game\L3.png'), py.image.load('images\Pygame-Tutorials-master\Game\L4.png'), py.image.load('images\Pygame-Tutorials-master\Game\L5.png'), py.image.load('images\Pygame-Tutorials-master\Game\L6.png'), py.image.load('images\Pygame-Tutorials-master\Game\L7.png'), py.image.load('images\Pygame-Tutorials-master\Game\L8.png'), py.image.load('images\Pygame-Tutorials-master\Game\L9.png')]
char = py.image.load('images\Pygame-Tutorials-master\Game\standing.png') 
lava=py.image.load('images\\lavaspritetest.png')
rock=py.image.load('images\\rockspritetest.png')
winimage=py.image.load('images\\YOUWIN.jpg')
walkCount = 0
title_font=py.font.SysFont('comicsans',80)
subtitle_font=py.font.SysFont('comicsans',30, italic=True)
text_font=py.font.SysFont('comicsans',30)
speed = 10
colors = {'red':(150,0,0),'green':(0,200,0), 'blue':(0,0,255), 'purple':(150, 0, 150), 'white':(255,255,255), 'black':(0,0,0) }
boulderColor=colors.get('red')
win = py.display.set_mode((WIDTH,HEIGHT))
boulderColor=colors.get('blue')
objColor=colors.get('red')
#Square
hbox = 25
wbox = 25
square = py.Rect(10,10, wbox, hbox)
x = 50
y = 400
width2 = 40
height2 = 60
vel = 5



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




def level1_game():
    win = py.display.set_mode((WIDTH,HEIGHT))
    bg=py.image.load("images\\volcanofinal.jpg")
    char = py.image.load('images\Pygame-Tutorials-master\Game\standing.png') 
    x = 100
    y = 250
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

        elif keys[py.K_RIGHT] and x < 900- vel - width:  
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
        if x > 850:
            win.blit(winimage, (200,50))
            py.display.update()
        if x > 120 and x<210 and y<305:
            win.blit(winimage, (200,50))
            py.display.update()
        win.blit(bg, (0,0))
        redrawGameWindow() 
        win.blit(lava, (155-5,310))
        win.blit(rock, (0,310-95))
        win.blit(lava, (370-15,310))
        win.blit(rock, (215-10,310-95))
        win.blit(lava, (585-25,310))
        win.blit(rock, (430-20,310-95))
        win.blit(rock, (645-30, 310-95))
        win.blit(rock, (750-30, 310-95))
        py.display.flip()

        #if x<50:
        #  Left=False
    #  if x>300:
        #  Right=False
        
        
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
instructions=5
Scoreboard=6

def changeScreenSize(width_new,height_new):
    global width 
    width= width_new
    global height
    height = height_new
    win = py.display.set_mode((width_new,height_new))
    win.fill(currentBackColor)
    displayTitle("SCREEN SIZE",True)
    displayMenu(WindowMessages)
    py.display.update

count = 0
win = py.display.set_mode((width,height))
py.display.update
run=True
win.fill('black')
py.display.set_caption("Setting Window")
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
            if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min and mouse_pos[1]<=y_max:
                win.fill(black)
                displayTitle("Instructions", 40)
                displayText("Jump across the rocks before the volcano explodes",160)
                displayText("Don't touch the lava!", 200)
                displayTitle("Back", height-50)
                
            if mouse_pos[0]>=320 and mouse_pos[0]<=485 and mouse_pos[1]>=height-100 and mouse_pos[1]<=height:
                win.fill(black)
                displayTitle("Menu", 40)
                displayMenu(Menu_messages)
                

            
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
               
                page=Mainmenu

        # if page==settings:
        #     if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min and mouse_pos[1]<=y_max:
        #         win.fill(black)
        #         displayTitle("Background Color",40)
        #         page = bgcolor
        #         displayTitle("Back", height-100)
                
            
            if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min2 and mouse_pos[1]<=y_max2:
                win.fill(black)
                displayTitle("Window size",40)
                displayMenu(WindowMessages)
                displayTitle("Back", height-100)
    
                page = windowsettings
        if page==windowsettings:
            if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min and mouse_pos[1]<=y_max:
                win=py.display.set_mode((900, 900))
                win.fill(black)
                displayTitle("Window size",40)
                page = windowsettings

                displayMenu(WindowMessages)
                displayTitle("Back", height-100)
                py.display.update
                page=settings
            if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min2 and mouse_pos[1]<=y_max2:
                win=py.display.set_mode((1000, 1000))
                win.fill(black)
                displayTitle("Window size",40)
                page = windowsettings
                displayMenu(WindowMessages)
                displayTitle("Back", height-100)
                py.display.update
                page=settings
            if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min3 and mouse_pos[1]<=y_max3:
                win=py.display.set_mode((800, 800))
                win.fill(black)
                displayTitle("Window size",40)
                
                displayMenu(WindowMessages)
                displayTitle("Back", height-100)
                py.display.update
                page=settings
        
        if page==settings:
            if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min and mouse_pos[1]<=y_max:
                win.fill(black)
                displayMenu(bg_messages)
                page=bgcolor
                if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min and mouse_pos[1]<=y_max:
                    currentBackColor = red
                    displayTitle("BACKGROUND COLOR",True)
                elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+100 and mouse_pos[1]<=y_max+100:
                    currentBackColor = blue
                    displayTitle("BACKGROUND",True)
                elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+200 and mouse_pos[1]<=y_max+200:
                    currentBackColor = green
                    displayTitle("BACKGROUND",True)
                elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+300 and mouse_pos[1]<=y_max+300:
                    currentBackColor = black
                    displayTitle("BACKGROUND",True)
        # #if page == bgcolor or windowsettings:
        #     if mouse_pos[0]>=320 and mouse_pos[0]<=485 and mouse_pos[1]>=height-100 and mouse_pos[1]<=height:
        #         win.fill(black)
        #         displayTitle("Settings", 40)
        #         displayMenu(Setting_messages1)
        #         count=0
        #         page=settings
        #         displayTitle("Back", height-100)
    mouse_pos = (0,0)
            




# while run:
#     #py.time.delay(10)
#     for eve in py.event.get():
#         if eve.type == py.QUIT:
#             run=False
#     if eve.type==py.MOUSEBUTTONDOWN:
#         mouse_pressed=py.mouse.get_pressed()
#         if mouse_pressed[0]:
#             mouse_pos=py.mouse.get_pos()
#             if square.collidepoint(mouse_pos):
#                 win.fill(green)
        
#         mouse_pressed=py.mouse.get_pressed()
#         mouse_pos=py.mouse.get_pos()
#         #print(mouse_pos)
#         y_min=190
#         y_max=212

#         y_min2=291
#         y_max2=312

#         y_min3=390
#         y_max3=413

#         y_min4=491
#         y_max4=514

#         # if page == Mainmenu:
        #     if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min and mouse_pos[1]<=y_max:
        #         displayTitle("INSTRUCTIONS",True)
        #         page = instructions
        #     elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min2 and mouse_pos[1]<=y_max2:
        #         level1_game()
        #         page = level1_game
        #         displayTitle("Back", height-100)
        #     elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min3 and mouse_pos[1]<=y_max3:
        #         level2_game()
        #         displayTitle("Back", height-100)
        #         page = level2_game
        #     elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min4 and mouse_pos[1]<=y_max4:
        #         displayTitle("SETTINGS",True)
        #         displayMenu(Setting_messages1)
        #         page = settings
        #     elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+400 and mouse_pos[1]<=y_max+400:
        #         displayTitle("SCOREBOARD",True)
        #         page = Scoreboard
        #     elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+500 and mouse_pos[1]<=y_max+500:
        #         break

        #     #Reset the mouse position
        #     mouse_pos = (0,0)

        
        # if (page == instructions or page == level1_game or page == level2_game  or page==Scoreboard or page==settings or page == windowsettings or page == bgcolor):
        #     if mouse_pos[0]>=50 and mouse_pos[0]<=200 and mouse_pos[1]>=height-100 and mouse_pos[1]<=height-150:
        #         displayTitle("MENU",False)
        #         win.fill(black)
        #         page = Mainmenu
        #         displayMenu(Menu_messages)

        
        # if page==instructions:
        #     win.fill(black)
        #     displayTitle("Instructions", 40)
        #     displayText("Jump across the rocks before the volcano explodes",160)
        #     displayText("Don't touch the lava!", 200)
        #     displayTitle("Back", height-100)

        # #Settings navigation
        # if page==settings:
        #     if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min and mouse_pos[1]<=y_max:
        #         displayTitle("SCREEN SIZE",True)
        #         page = windowsettings
        #     elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+100 and mouse_pos[1]<=y_max+100:
        #         displayTitle("BACKGROUND",True)
        #         page = bgcolor
            
        #     #Reset the mosue position
        #     mouse_pos = (0,0)

        # #If you click back when Settings was the previous page


        # #Screen Size Menu
        # if page== windowsettings:
        #     displayMenu()
        #     if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min and mouse_pos[1]<=y_max:
        #         changeScreenSize(800,800)
        #     elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+100 and mouse_pos[1]<=y_max+100:
        #         changeScreenSize(700,700)
        #     elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+200 and mouse_pos[1]<=y_max+200:
        #         changeScreenSize(600,600)

        # #Background Color Menu
    

        # #Reset the mouse position
        # mouse_pos = (0,0)            

py.quit()
    #Credit to vivaan for the code determining the mouse position to click the button
