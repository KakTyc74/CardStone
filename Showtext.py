import pygame
import time
import random

display_width = 800
display_height = 600

white = (255,255,255)
black = (0,0,0)
red = (180,80,20)

rhsb_width = 150

pygame.init()
gameDisplay = pygame.display.set_mode ((display_width,display_height))

pygame.display.set_caption('RHSB')
clock = pygame.time.Clock()
#rhsbImg = pygame.image.load('prototype.png')


def btn(btnx, btny, btnw, btnh, color, text, fontsize):
    pygame.draw.rect(gameDisplay, color, [btnx, btny, btnw, btnh])
    message_display(text, btnx+btnw/2, btny+btnh/2, fontsize)

def text_objects(text, font):
    TextSurface = font.render(text, True, red, black)
    return TextSurface, TextSurface.get_rect()

def message_display(text,x,y,fontsize):
    largeText = pygame.font.Font('freesansbold.ttf', fontsize)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y) 
    gameDisplay.blit(TextSurf, TextRect)

    
def choice():
    message_display("Выбери карту из 4", display_width/2, display_height/2,35)
    btn(display_width/2, display_height/2+100, 50, 50, red, 'card1', 12)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    gameDisplay.fill(white)
    choice()
    pygame.display.update()
    clock.tick(60)
