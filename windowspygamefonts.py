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

Setting_messages1 = ["SCREEN SIZE", "BACKGROUND COLOR","OBJECT COLOR","SOUNDS (ON/OFF)"]    #Setting Messages

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

def displayTitle(title):    #Title print function
    pygame.time.delay(100)
    text = title_font.render(title,1,red)
    #win.blit(text,(width/2-text.get_width()/2, height/2-text.get_height()/2))
    win.blit(text,(width/2-text.get_width()/2,30))
    pygame.display.update()
    pygame.time.delay(100)

def displayMenu():  #Subtitle print function
    pygame.time.delay(100)
    x = 70
    y = 190
    square.x = x
    square.y = y
    for i in range (0, len(Setting_messages1)):
        word = Setting_messages1[i]
        pygame.draw.rect(win, purple, square)
        text = subtitle_font.render(word,1,red)
        win.blit(text,(x+wbox+10, y-10))
        pygame.display.flip()
        pygame.time.delay(100)
        y +=100
        square.y = y

run=True
count = 0
while run:
    pygame.time.delay(10)
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run=False
    if eve.type==py.MOUSEBUTTONDOWN:
        mouse_pressed=py.mouse.get_pressed()
        if mouse_pressed[0]:
            mouse_pos=py.mouse.get_pos()
            if square.collidepoint(mouse_pressed):
                win.fill(green)
        
    if count == 0:
        displayTitle("SETTINGS")
        displayMenu()
        count+=1
    mouse_pressed=py.mouse.get_pressed()
    mouse_pos=py.mouse.get_pos()
    y_min=190
    y_max=212

    y_min2=291
    y_max2=312

    y_min3=390
    y_max3=413

    y_min4=491
    y_max4=514
    if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min and mouse_pos[1]<=y_max:
        if mouse_pressed:
            win.fill(blue)
    if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min2 and mouse_pos[1]<=y_max2:
        if mouse_pressed:
            win.fill(blue)
    if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min3 and mouse_pos[1]<=y_max3:
       if mouse_pressed:
            win.fill(blue)
    if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min4 and mouse_pos[1]<=y_max4:
        if mouse_pressed:
            win.fill(blue)

    


    #x,y=pygame.mouse.get_pos()
   #print("( "+ str(x)+ ", "+ str(y)+" )")
    #pygame.quit()

