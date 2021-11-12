import pygame
pygame.init()
HEIGHT=700
WIDTH=800
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game")


walkRight = [pygame.image.load('images\Pygame-Tutorials-master\Game\R1.png'), pygame.image.load('images\Pygame-Tutorials-master\Game\R2.png'), pygame.image.load('images\Pygame-Tutorials-master\Game\R3.png'), pygame.image.load('images\Pygame-Tutorials-master\Game\R4.png'), pygame.image.load('images\Pygame-Tutorials-master\Game\R5.png'), pygame.image.load('images\Pygame-Tutorials-master\Game\R6.png'), pygame.image.load('images\Pygame-Tutorials-master\Game\R7.png'), pygame.image.load('images\Pygame-Tutorials-master\Game\R8.png'), pygame.image.load('images\Pygame-Tutorials-master\Game\R9.png')]
walkLeft = [pygame.image.load('images\Pygame-Tutorials-master\Game\L1.png'), pygame.image.load('images\Pygame-Tutorials-master\Game\L2.png'), pygame.image.load('images\Pygame-Tutorials-master\Game\L3.png'), pygame.image.load('images\Pygame-Tutorials-master\Game\L4.png'), pygame.image.load('images\Pygame-Tutorials-master\Game\L5.png'), pygame.image.load('images\Pygame-Tutorials-master\Game\L6.png'), pygame.image.load('images\Pygame-Tutorials-master\Game\L7.png'), pygame.image.load('images\Pygame-Tutorials-master\Game\L8.png'), pygame.image.load('images\Pygame-Tutorials-master\Game\L9.png')]
bg = pygame.image.load('images\scenery.2.0.jpg')
char = pygame.image.load('images\Pygame-Tutorials-master\Game\standing.png')
win.blit(bg, (0,0))

boulder=pygame.Rect(WIDTH-300, HEIGHT-300, 100, 300)

x = 50
y = 400
width = 40
height = 60
vel = 5

clock = pygame.time.Clock()

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
        
    pygame.display.update() 
    


run = True

while run:
    #print(pygame.mouse.get_pos())

    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:  
        x += vel
        left = False
        right = True
        
    else: 
        left = False
        right = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
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

    redrawGameWindow() 
    
pygame.quit()

#50, 460
#748, 460

