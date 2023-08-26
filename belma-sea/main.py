# Imports

import pygame
from pygame import mixer
import random
from pygame import font

# Init

pygame.init()
mixer.init()
font.init()

# Fonts
font = pygame.font.SysFont(None, 50)
title_font = pygame.font.SysFont(None, 100)

# Images
background = pygame.image.load('assets/background.png')
submarine = pygame.image.load('assets/submarine.png')
start_screen = pygame.image.load('assets/start-screen.png')
shark = pygame.image.load('assets/shark.png')
jelly_fish = pygame.image.load('assets/jelly-fish.png')
pirana = pygame.image.load('assets/pirana.png')

# Music

background_music = pygame.mixer.Sound('sound/background.wav')
wave = pygame.mixer.Sound('sound/ocean-wave.wav')
background_music.play(-1)
wave.play()

# Variables
run = False
start = True
timer = 0
score = 0
score_t = font.render(f'Score: {score}', True, (0, 0, 0))

# Constants
WIDTH = background.get_width()
HEIGHT = background.get_height()

# Screen Setup

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Belma Sea')


run = True
# Classes

class Player:
    def __init__(self, x, y, width, height, img, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = img
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        
    def move(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
class Enemy:
    def __init__(self, x, y, width, height, img, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = img
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        
    def move(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
# Defs

def randomise_enemy():
    enemy_num = random.randint(1, 3)
    if enemy_num == 1:
        enemy_char = shark
    if enemy_num == 2:
        enemy_char = jelly_fish
    if enemy_num == 3:
        enemy_char = pirana
    return enemy_char

# Default so python knows this variable

enemy_character = shark

# Objects
player = Player(100, HEIGHT // 2, submarine.get_width(), submarine.get_height(), submarine, screen)
enemy =  Enemy(WIDTH,  random.randint(212, 568), enemy_character.get_width(), enemy_character.get_height(), enemy_character, screen)

# Start Screen

def start_screen_def():
    start = True
    # Text
    title = title_font.render(f'The Belma Sea', True, (0, 0, 0))
    play = font.render(f'Press Enter to Play', True, (0, 0, 0))

    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                true = False
                break
            
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RETURN]:
            start = False
            run = True
            enemy.x = WIDTH
            enemy.y = random.randint(212, 568)
            enemy_character = randomise_enemy()
            enemy.img = enemy_character
            enemy.width = enemy_character.get_width()
            enemy.height = enemy_character.get_height()
            
        # Draw
        screen.blit(start_screen, (0, 0))
        screen.blit(title, (0, 50))
        screen.blit(play, (0, 120))
        
        # Update
        pygame.display.flip()
        
start_screen_def()
enemy_character = randomise_enemy()



# Game loop

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        
    # Keys
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        if player.y > 212:
            player.y -= 2

    if keys[pygame.K_DOWN]:
        if player.y < 568:
            player.y += 2

    
    # Collisions
    collide = pygame.Rect.colliderect(enemy.rect, player.rect)
    
    if collide:
        screen.fill('black')
        score = 0
        start_screen_def()

        
        
    # Move Enemy
    enemy.x -= 5
    if enemy.x < 0:
        enemy.x = WIDTH
        enemy.y = random.randint(212, 568)
        enemy_character = randomise_enemy()
        enemy.img = enemy_character
        enemy.width = enemy_character.get_width()
        enemy.height = enemy_character.get_height()
        enemy.x -= 5
        score += 1
        score_t = font.render(f'Score: {score}', True, (0, 0, 0))

        
    
        
    # Move all Rects
    player.move()
    enemy.move()

    
    # Draw Screen

    screen.blit(background, (0, 0))
    player.draw()
    enemy.draw()
    screen.blit(score_t, (0, 0))

    
    # Update Timer
    timer += 0.010

    # Play Wave Sound
    if timer > 5:
        wave.play()
        timer = 0
        
    #  Update
    pygame.display.flip()
    
    
    
# Quit
pygame.quit()