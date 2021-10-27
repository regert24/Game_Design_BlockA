#tom reger
#learn fonts

import pygame as py, os, random, time

py.init()

width = 800
height = 800
BLACK=(255,255,255)
win=py.display.set_mode((width, height))
py.display.set_caption("Setting window")

#TITLE_FONT=py.font.SysFont(name, size, bold=False,italic=False)
TITLE_FONT=py.font.SysFont('comicsans', 80)
subtitle_font=py.font.SysFont('comicsans',40, italic=True )
def display_message(message):
    py.time.delay(100)
    text= TITLE_FONT.render(message,1,BLACK)
    win.blit(text, (width/2-text.get_width()/2, 30))
    py.display.update()
    py.time.delay(100)
def display_subtitle(message, x, y):
    py.time.delay(100)
    text = subtitle_font.render(message, 1,BLACK)
    win.blit(text, (x, y))
    py.display.flip()
    py.time.delay(100)
run=True
while run:
    for eve in py.event.get():
        if eve.type == py.QUIT:
            run=False
            py.quit()
    display_message("settings")
    py.time.delay(300)
    win.fill((0,0,0))
    display_subtitle("window color", 90, 250)
    display_subtitle("sound", 90, 350)
    display_subtitle("quit game", 90, 450)
#py.quit()




