# Importations

import pygame
import time
import random
from pygame import mixer


# Init
pygame.init()
mixer.init()

# Constants
WIDTH = 1200
HEIGHT = 800

# Variables
run = True
score = 0

# Images
background = pygame.image.load('assets/winter background.svg')
snow_man = pygame.image.load('assets/snow man.png')
snow_ball_img = pygame.image.load('assets/snow ball.svg')

# Music

collect = pygame.mixer.Sound('music/collect.wav')
background_music = pygame.mixer.Sound('music/music.wav')
background_music.play(-1)

# Text

font = pygame.font.SysFont(None, 50)
title_font = pygame.font.SysFont(None, 100)


# Constants

# Set up Screen

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Snow Man')

# Classes

class Player:
    def __init__(self, x, y, width, height, img, screen):
        self.x = x
        self.y = y
        self.img = img
        self.screen = screen
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
    
    def move(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

class Snow:
    def __init__(self, x, y, width, height, img, screen):
        self.x = x
        self.y = y
        self.img = img
        self.screen = screen
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
    
    def move(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


# Create Objects

snow_ball = Snow(random.randint(0, WIDTH), 0, snow_ball_img.get_width(), snow_ball_img.get_height(), snow_ball_img, screen)
player = Player(WIDTH / 2, 500, snow_man.get_width(), snow_man.get_height(), snow_man, screen)

# Start Screen

screen.fill((173, 216, 230))
title = title_font.render(f'Snow Man', True, (0, 0, 0))
play = font.render(f'Press Enter to Play', True, (0, 0, 0))
screen.blit(title, (450, 100))
screen.blit(play, (0, HEIGHT - 50))
screen.blit(snow_man, (WIDTH // 2, HEIGHT // 2))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        break



# Main Game

while run:

    for event in pygame.event.get():
      
        # Check for X button(Close/Quit)      
        if event.type == pygame.QUIT:
            run = False
            
    # Keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.x += 8
    if keys[pygame.K_LEFT]:
        player.x -= 8
    
    
    # Collisions
    collide = pygame.Rect.colliderect(snow_ball.rect, player.rect)
 
    if collide:
        snow_ball = Snow(random.randint(0, WIDTH), 0, snow_ball_img.get_width(), snow_ball_img.get_height(), snow_ball_img, screen)
        collect.play()
        score += 1
    # Move Snow Ball
    snow_ball.y += 7
    if snow_ball.y > HEIGHT:
        snow_ball = Snow(random.randint(0, WIDTH), 0, snow_ball_img.get_width(), snow_ball_img.get_height(), snow_ball_img, screen)
    # Move Screen
    player.move()
    snow_ball.move()
    
    # Set Text
    
    score_t = font.render(f'Score: {score}', True, (0, 0, 0))
    
    # Draw Screen
    screen.blit(background, (0, 0))
    player.draw()
    snow_ball.draw()
    screen.blit(score_t, (0, 0))
    
    # Update
    
    pygame.display.flip()