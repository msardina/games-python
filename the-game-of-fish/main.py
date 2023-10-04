# Import

import pygame
import random
from pygame import mixer
import time

# Init

pygame.init()
mixer.init()


# Images

background_start = pygame.image.load('assets/start-screen.png')
level = pygame.image.load('assets/level.png')
fish = pygame.image.load('assets/fish.png')

# Variables

run = False
start = True
timer = 0
timer_2 = 0
mouse_down = False

# Consts

WIDTH = background_start.get_width()
HEIGHT = background_start.get_height()

print(WIDTH)
print(HEIGHT)


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
        
    def draw(self, mouse_down):
        if self.state == 'hooking':
            self.pos = pygame.mouse.get_pos()
            self.ex = self.pos[0]
            self.ey = self.pos[1]
            
        elif self.state == 'fishing':
            self.pos = pygame.mouse.get_pos()
            self.ex = self.pos[0]
            
        elif self.state == 'fish getting caught':
            print(mouse_down)
            if self.ex < WIDTH:
                self.ex += 0
                
            elif mouse_down:
                self.ex -= 10

                
            else:
                self.state = 'broken line'
        
        if not self.state == 'broken line':
            pygame.draw.line(self.screen, (0, 0, 0), (self.sx, self.sy), (self.ex, self.ey), 3)
            
    def state_handler(self):
            if self.state == 'hooking':
                self.state = 'fishing'
                self.ey = 650
                
            #elif self.state == 'fishing':
            #    self.state = 'hooking'
                
            #elif self.state == 'fish getting caught':
            #    screen.blit(fish, (self.pos[0], self.pos[1]))
            #    pygame.display.flip()
            #    fishing_rod.state = 'hooking'
            
        

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
    
    # Draw Screen    
    screen.blit(level, (0, 0))
    fishing_rod.draw(mouse_down)    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
        if event.type == pygame.MOUSEBUTTONUP:
            fishing_rod.state_handler()

            
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        else:
            mouse_down = False
    # rasie Timer
    
    if fishing_rod.state == 'fishing':
        timer += 0.010
        if timer > 3:
            print('Fish Caught')
            timer = 0
            fishing_rod.state = 'fish getting caught'
            
        
            


    
    # Update Mouse Pos
    
    # Update
    
    pygame.display.flip()
            
pygame.quit()