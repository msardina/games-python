# Importations

import pygame
import random
from pygame import mixer

# Initialise

pygame.init()
mixer.init()






# Images

duck = pygame.image.load('assets/new-assets/duck.png')
level = pygame.image.load('assets/new-assets/level.png')
background_level = pygame.image.load('assets/new-assets/background1.png')

# Vars
run = True
falling_speed = -3

# Constants
WIDTH, HEIGHT = background_level.get_width(), background_level.get_height()

# Setup Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Duck Land - By Marcos Sardina')

# Music

background = pygame.mixer.Sound('sound/background.wav')
background.play(-1)
# Classes

class Player:
    def __init__(self, x, y, width, height, img, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
        self.mask_img = self.mask.to_surface()
        
    def draw(self):
        #pygame.draw.rect(self.screen, (	255,255,0), self.rect)
        screen.blit(self.img, (self.x, self.y))
        #screen.blit(self.mask_img, (self.x, self.y))
        
    def move(self):
        self.mask = pygame.mask.from_surface(self.img)
        #self.mask_img = self.mask.to_surface()
        

class Level:
    def __init__(self, x, y, width, height, img, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
        self.mask_img = self.mask.to_surface()
        
    def draw(self):
        #pygame.draw.rect(self.screen, (	255,255,0), self.rect)
        screen.blit(self.img, (self.x, self.y))
        #screen.blit(self.mask_img, (self.x, self.y))
        
    def move(self):
        self.mask = pygame.mask.from_surface(self.img)


# Make Objects
player = Player(WIDTH // 2, HEIGHT // 2, duck.get_width(), duck.get_height(), duck, screen)
floor = Level(WIDTH // 2, (HEIGHT // 2) + 100, level.get_width(), level.get_height(), level, screen)

#floor = Player(0, 0, level.get_width, level.get_height(), level, screen)

# Main game loop

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    # Keys
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]:
        floor.x -= 8
    if keys[pygame.K_LEFT]:
        floor.x += 8
    if keys[pygame.K_SPACE]:
        floor.y += 5
    
    
    # Level Mask
    # Add Gravity Element
    floor.y += falling_speed
    
    level_mask = level.get_masks()
    player_mask = duck.get_masks()
    
    # Collisions
    #if level_mask.overlap(player_mask, (floor.x - player.x, floor.y - player.y))
   #     falling_speed = 0
   #else:
   #     falling_speed = -3
        
    # Move Screen
    player.move()
    floor.move()
    
    # Draw Screen
    
    screen.blit(background_level, (0, 0))
    floor.draw()
    player.draw()
    
    # Update Screen
    
    pygame.display.flip()
    
print(floor.y)
print(floor.x)
pygame.quit()