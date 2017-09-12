import pygame
import time
import random

display_width = 800
display_height = 600

white = (255,255,255)
black = (0,0,0)
red = (180,80,20)
bright = (10,10,10)

rhsb_width = 150

pygame.init()
gameDisplay = pygame.display.set_mode ((display_width,display_height))

pygame.display.set_caption('RHSB')
clock = pygame.time.Clock()
#rhsbImg = pygame.image.load('prototype.png')

def btn(btn1pos, color, text, fontsize, active = False):
    if active:
        r = color[0]
        g = color[1]
        b = color[2]
        color = ((r+20), (g+20), (b+20))
    pygame.draw.rect(gameDisplay, color, btn1pos)
    [btnx,btny,btnw,btnh] = btn1pos
    message_display(text, btnx+btnw/2, btny+btnh/2, fontsize)
    if active:
        return True
    
def text_objects(text, font):
    TextSurface = font.render(text, True, red, black)
    return TextSurface, TextSurface.get_rect()

def message_display(text,x,y,fontsize):
    largeText = pygame.font.Font('freesansbold.ttf', fontsize)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y) 
    gameDisplay.blit(TextSurf, TextRect)
    
def choice():
    message_display("Выбери 2 карты", display_width/2, display_height/2-150,35)
    choicelist = []
    for i in range(4):
        tempx = display_width/2 - (4*100 + (4-1)*50)/2 + (50+100)*i
        choicelist.append ([tempx, display_height/2, 100, 150])
    for btni in choicelist:
        btn(btni, red, 'Выход', 12, mouse_pos_in_rect(btni))

def mouse_pos_in_rect(btn1pos):
    [x,y,width,height] = btn1pos
    mouse = pygame.mouse.get_pos()
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        return True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        mbd = (event.type == pygame.MOUSEBUTTONDOWN)
        mbu = (event.type == pygame.MOUSEBUTTONUP)

    gameDisplay.fill(white)
    choice()
    pygame.display.update()
    clock.tick(60)
