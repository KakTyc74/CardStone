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



def text_objects(text, font):
    TextSurface = font.render(text, True, red, black)
    return TextSurface, TextSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 35)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2)) 
    gameDisplay.blit(TextSurf, TextRect)

    
def choice():
    message_display("Выбери карту из 4")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    gameDisplay.fill(white)
    choice()
    pygame.display.update()
    clock.tick(60)



#def game_loop():

