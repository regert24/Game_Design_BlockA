#tom reger
#10/15/21
#changing window size, basic game loops, learning display, opening windows, 
import os, random
import pygame
os.system('cls')

#fist thing we have to do is initialize pygame
pygame.init()
check=True
height=600
width=600
colors={'black':(0,0,0), 'red':(255,0,0), 'green':(0,255,0), 'blue':(0,0,255), 'white':(255,255,255),'purple':(150,0,150)}
# while check:
#     height=input("Height of the window: (100-1000) ")
#     width=input("width of your window: (10-1000) ")
#     colornames=('black', 'red', 'green', 'blue', 'white', 'purple')
#     randcolor=random.choice(colornames)

#     try:
#         height=int(height)
#         width=int(width)
#         check=False
#     except ValueError:
#         check = True
color=colors.get('red')
window=pygame.display.set_mode((height,width))
window.fill((color))
#RGB-255 max per color
pygame.display.flip() #refresh window with new color
pygame.display.set_caption("My game window")
pygame.display.flip()
x=width/2
y=height/2
hbox=50
wbox=50
speed=10
xc=random.randint(25,550)
yc=random.randint(25,550)
rcircle=hbox/2
rect=pygame.Rect(x,y, wbox, hbox)
pygame.draw.rect(window, (150, 200, 20), rect)
pygame.draw.circle(window, colors.get('blue'), (xc,yc), rcircle)
pygame.display.flip()
run=True


#main loop for tge game:
while run:
    
    pygame.time.delay(10)
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            run=False
   # x,y=pygame.mouse.get_pos()
   # print("( "+ str(x)+ ", "+ str(y)+" )")
    keyPressed = pygame.key.get_pressed()
    if keyPressed[pygame.K_UP]:
        if rect.y < 0:
            rect.y = height
        else:
            rect.y -= speed
    if keyPressed[pygame.K_DOWN]:
        if rect.y>height:
            rect.y = 0
        else:
            rect.y += speed
    if keyPressed[pygame.K_LEFT]:
        if rect.x < 0:
            rect.x=width
        else:
            rect.x -= speed
    if keyPressed[pygame.K_RIGHT]:
        if rect.x>width:
            rect.x=0
        else:
            rect.x += speed
    window.fill(color)
    

    if keyPressed[pygame.K_w] and yc>rcircle:
            yc -= speed
    if keyPressed[pygame.K_s] and yc<height-rcircle:
            yc += speed
    if keyPressed[pygame.K_a] and xc>rcircle:
            xc -= speed
    if keyPressed[pygame.K_d] and xc<width-rcircle:
            xc += speed
    

    point =(xc, yc)   
    collide=rect.collidepoint(point)
    #collide function
    if collide:
        rcircle=rcircle+(hbox/6)
        x=random.randrange(0,width)
        y=random.randrange(0,height)
        rect=pygame.Rect(x,y,wbox,hbox)
    pygame.draw.rect(window, colors.get('purple'), rect)
    pygame.draw.circle(window, colors.get('blue'), (xc,yc), rcircle)
    pygame.display.flip()
    if rcircle == hbox*2:
        pygame.quit
        break
pygame.quit()

