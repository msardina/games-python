# Import

import pygame
import random
from pygame import mixer

# Init

pygame.init()
mixer.init()


# Images

background_start = pygame.image.load('assets/start-screen.png')
level = pygame.image.load('assets/level.png')

# Variables

run = False
start = True

# Consts

WIDTH = background_start.get_width()
HEIGHT = background_start.get_height()



# Music

background_music = pygame.mixer.Sound('sounds/background.wav')
background_music.play(-1)
# Setup Screen

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Game of Fish || Produced by MS Coporation Team')

# Classes

class Fish_Rod:
    def __init__(self, sx, sy, screen):
        self.pos = pygame.mouse.get_pos()
        self.sx = sx
        self.sy = sy
        self.ex = self.pos[0]
        self.ey = self.pos[1]
        self.state = 'hooking'
        self.screen = screen
        
    def draw(self):
        if self.state == 'hooking':
            self.pos = pygame.mouse.get_pos()
            self.ex = self.pos[0]
            self.ey = self.pos[1]
            
        elif self.state == 'fishing':
            self.pos = pygame.mouse.get_pos()
            self.ex = self.pos[0]
        pygame.draw.line(self.screen, (0, 0, 0), (self.sx, self.sy), (self.ex, self.ey), 3)
        

# Start Loop

while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    
    # Draw
    
    screen.blit(background_start, (0, 0))
    
    # Enter Key
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RETURN]:
        start = False
        run = True
        
    # Update
    
    pygame.display.flip()


#  Reset

screen.fill('black')


# Objects

fishing_rod = Fish_Rod(260, 460, screen)

# Game Loop

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
        if event.type == pygame.MOUSEBUTTONUP:
            if fishing_rod.state == 'hooking':
                fishing_rod.state = 'fishing'
                fishing_rod.ey = 650
                
            elif fishing_rod.state == 'fishing':
                fishing_rod.state = 'hooking'
    
    # Draw Screen
    
    screen.blit(level, (0, 0))
    fishing_rod.draw()
    
    # Update Mouse Pos
    
    # Update
    
    pygame.display.flip()
            
pygame.quit()