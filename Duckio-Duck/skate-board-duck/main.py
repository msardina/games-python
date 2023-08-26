# Importations

import pygame
import random
from pygame import  mixer

# Initialise

pygame.init()
mixer.init()

# Imgs
background_img_level_1 = pygame.image.load('assets/backgrounds/background_l1.png')
duck = pygame.image.load('assets/duck.png')
floor = pygame.image.load('assets/backgrounds/floor.png')
start_screen_img = pygame.image.load('assets/backgrounds/startScreen.png')
chips = pygame.image.load('assets/food/chips.png')
pizza = pygame.image.load('assets/food/pizza.png')

# Fonts

font = pygame.font.SysFont('pixel', 50)
title_font = pygame.font.SysFont('pixel', 100)

# Vars
run = False
start = True
jump = False

# Constants
WIDTH = background_img_level_1.get_width()
HEIGHT = background_img_level_1.get_height()

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Skate Board Duck')


# Music
back_music = pygame.mixer.Sound('sound/background.wav')
connect = pygame.mixer.Sound('sound/Connect.wav')
jump_sound = pygame.mixer.Sound('sound/jump.wav')
back_music.play(-1)

# Classes

class Player:
    def __init__(self, x, y, width, height, img, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.img = img
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        #pygame.draw.rect(self.screen, (	255,255,0), self.rect)
        screen.blit(self.img, (self.x, self.y))
        
    def move(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
class Food:
    def __init__(self, x, y, width, height, img, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.img = img
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        #pygame.draw.rect(self.screen, (	255,255,0), self.rect)
        screen.blit(self.img, (self.x, self.y))
        
    def move(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        

player = Player(100, HEIGHT - 200, duck.get_width(), duck.get_height(), duck, screen)
food = Food(WIDTH, random.randint(HEIGHT / 2, HEIGHT - floor.get_height()), chips.get_width(), chips.get_height(), chips, screen)

# Start Loop



# Start presentation

title = title_font.render(f'Skate Board Duck', True, (0, 0, 0))
play = font.render(f'Press Enter to Play', True, (0, 0, 0))
screen.blit(start_screen_img, (0, 0))
screen.blit(title, (100, 100))
screen.blit(play, (100, 170))
pygame.display.flip()

while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            start = False
            break
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        connect.play()
        start = False
        run = True
        break
    
    # Update
    pygame.display.flip()
        

# Game loop

while run:
    
    # X Button
    for event in pygame.event.get():#
        if event.type == pygame.QUIT:
            run = False
            break

    
    # Keys
    keys = pygame.key.get_pressed()
    
    
    # Flight
    if keys[pygame.K_SPACE]:
        player.y -= 5
        if jump == False:
            jump_sound.play()
            
        jump = True
    else:
        if player.y < HEIGHT - 200:
            player.y += 5
            
        else:
            jump = False
    
    # Right - Left
    
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_LEFT]:
        player.x -= 5
        
    
    
    # Move Food Object
    
    food.x -= 5
    if food.x < 0:
        food.x = WIDTH
        food.y = random.randint(HEIGHT / 2, HEIGHT - floor.get_height())
        
    # Collisions
    
    collide = pygame.Rect.colliderect(player.rect, food.rect)
    
    if collide:
        food.x = WIDTH
        food.y = random.randint(HEIGHT / 2, HEIGHT - floor.get_height())
        
    # Move Screen
    player.move()
    food.move()
    
    # Draw
    screen.blit(background_img_level_1, (0, 0))
    screen.blit(floor, (0, HEIGHT - floor.get_height()))
    player.draw()
    food.draw()
    
    # Update
    pygame.display.flip()
    
    
pygame.quit()