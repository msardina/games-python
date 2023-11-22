#init
import pygame
import random
from pygame import mixer

#images

#sounds

#constants
WIDTH = 1200
HEIGHT = 800
FPS= 60

#vars
run = True
clock = pygame.time.Clock()

#setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Adventure of Sky-Man')

#game loop

while run:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
            
    #draw
    
    screen.fill('light blue')

    #move
    
    #update
    clock.tick(FPS)
    pygame.display.update()