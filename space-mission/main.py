# Imports

import pygame
import random
from pygame import mixer


# Init

pygame.init()
mixer.init()

# Images

background_img = pygame.image.load('assets/background.png')
level = pygame.image.load('assets/level.png')
space_ship_img = pygame.image.load('assets/space-ship.png')
space_llama = pygame.image.load('assets/llama.png')
landed = False

# Music

talking = pygame.mixer.Sound('sounds/talking.wav')
background = pygame.mixer.Sound('sounds/background.wav')
release_llama = pygame.mixer.Sound('sounds/release llama.wav')
talking.play()
background.play(-1)

# Vars

run = False
start = True
# Consts
WIDTH, HEIGHT = background_img.get_width(), background_img.get_height()

# Setup Screen

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Space Mission || Produced by the MS Team')

# Classes

class Ship:
    def __init__(self, x, y, width, height, img, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = img
        self.screen = screen
        
    def draw(self):
        screen.blit(self.img, (self.x, self.y))

# Objects

ship = Ship(WIDTH // 2, -200, space_ship_img.get_width, space_ship_img.get_height, space_ship_img, screen)

# Start Loop

while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
    
    # Enter 

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RETURN]:
        start = False
        run = True
        
    # Draw
    
    screen.blit(background_img, (0, 0))
    
    # Move
    
    # Update
    pygame.display.flip()


screen.fill('black')

# Game loop

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    # Draw
    
    screen.blit(level, (130, 10))
    ship.draw()
    
    # Move
    
    if ship.y <= 200:
        ship.y += 3
    else:
        if landed == False:
            release_llama.play()
            landed = True
        screen.blit(space_llama, ((WIDTH // 2) + 120, 330))
    # Update
    pygame.display.flip()
    
pygame.quit()