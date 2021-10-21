#tom reger
#10/15/21
#changing window size, basic game loops, learning display, opening windows, 
import os, random
import pygame
os.system('cls')

#fist thing we have to do is initialize pygame
pygame.init()
check=True
height=""
width=""
colors={'black':(0,0,0), 'red':(255,0,0), 'green':(0,255,0), 'blue':(0,0,255), 'white':(255,255,255),'purple':(150,0,150)}
while check:
    height=input("Height of the window: (100-1000) ")
    width=input("width of your window: (10-1000) ")
    colornames=('black', 'red', 'green', 'blue', 'white', 'purple')
    randcolor=random.choice(colornames)

    try:
        height=int(height)
        width=int(width)
        check=False
    except ValueError:
        check = True
color=colors.get(str(randcolor))
window=pygame.display.set_mode((400,400))
window.fill((color))
#RGB-255 max per color
pygame.display.flip() #refresh window with new color
pygame.display.set_caption("My game window")
pygame.display.flip()
hbox=50
wbox=50
speed=5
rect=pygame.Rect(width/2,height/2, wbox, hbox)
pygame.draw.rect(window, (150, 200, 20), rect)
pygame.display.flip()
run=True

#main loop for tge game:
while run:
    pygame.time.delay(100)
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            run=False
   # x,y=pygame.mouse.get_pos()
   # print("( "+ str(x)+ ", "+ str(y)+" )")
    keyPressed = pygame.key.get_pressed()
    if keyPressed[pygame.K_UP]:
        rect.y -= speed
    if keyPressed[pygame.K_DOWN]:
        rect.y += speed
    if keyPressed[pygame.K_LEFT]:
        rect.x -= speed
    if keyPressed[pygame.K_RIGHT]:
        rect.x += speed
    window.fill(color)
    pygame.draw.rect(window, colors.get('purple'), rect)
    pygame.display.flip()



pygame.quit()

