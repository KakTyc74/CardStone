import pygame
import time
import random

display_width = 1024
display_height = 768

white = (255,255,255)
black = (0,0,0)
red = (180,80,20)

card_width = 150
card_height = 300

pygame.init()
gameDisplay = pygame.display.set_mode ((display_width,display_height))

pygame.display.set_caption('CardStone')
clock = pygame.time.Clock()
CardImg = pygame.image.load('card1.png')
