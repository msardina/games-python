# Imports

import pygame
import random
import time
from pygame import mixer

# Initialise

pygame.init()
mixer.init()

# Images

cars = pygame.image.load('imgs/cars.png')
old_cars = pygame.image.load('imgs/old-car-selection.png')
new_cars = pygame.image.load('imgs/new-car-selection2.png')


old_ferrari = pygame.image.load('imgs/old ferrari.png')
old_williams = pygame.image.load('imgs/old williams.png')
old_mclaren = pygame.image.load('imgs/old mclaren.png')
new_williams = pygame.image.load('imgs/new williams.png')
new_ferrari = pygame.image.load('imgs/new ferrari.png')
new_mclaren = pygame.image.load('imgs/new mclaren.png')


# Music

background_music = pygame.mixer.Sound('sounds/background.wav')
engine_sound = pygame.mixer.Sound('sounds/engine.wav')
background_music.play(-1)



# Fonts

regular_font = pygame.font.Font(None, 50)
medium_font = pygame.font.Font(None, 100)
title_font = pygame.font.Font(None, 150)


# Text

title = title_font.render('PITSTOP III', False, (0, 0, 0), None)
year_text = regular_font.render('What Mode will you play?', False, (0, 0, 0), None)
year2_text = regular_font.render('Press 1 for classic|| Press 2 for new', False, (0, 0, 0), None)
choose_car_text = medium_font.render('Choose Your Car', False, (0, 0, 0), None)


# Vars

run = False
start = True
age = False
car_select = False
car = old_mclaren
# Const

WIDTH, HEIGHT = 800, 970

# Setup Screen

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pitstop III || The Peak of Motor Sport')

# Classes

class Car:
    
    def __init__(self, x, y, img, screen):
        self.x = x
        self.y = y
        self.img = img
        self.width = img.get_width()
        self.height = img.get_height()
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        
    def move(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def keys(self, keys_pressed):
        
        #if keys_pressed[pygame.K_UP]:
        #   self.y -= 0.50
            
        #if keys_pressed[pygame.K_DOWN]:
        #    self.y += 0.50
        
        if keys_pressed[pygame.K_RIGHT]:
            self.x += 0.50
            
        if keys_pressed[pygame.K_LEFT]:
            self.x -= 0.50

        
        
# Start Loop

while start:
    
    for event in pygame.event.get():
        
        # Check for the X button
        if event.type == pygame.QUIT:
            pygame.quit()
        
            
    #### Draw ####
    
    # Draw Road
    
    screen.fill('grey')
    pygame.draw.rect(screen, (0, 100, 50), (0, 0, 200, HEIGHT))
    pygame.draw.rect(screen, (0, 100, 50), (WIDTH - 200, 0, 200, HEIGHT))
    
    # Cars & Title
    
    screen.blit(cars, ((WIDTH // 2) - 100, HEIGHT // 2))
    screen.blit(title, (125, 100))
    pygame.draw.line(screen, (0, 0, 0), (125, 200), (WIDTH - 110, 200), 5)
    

    # Start Key
    
    key = pygame.key.get_pressed()
    
    if key[pygame.K_RETURN]:
        start = False
        age = True
    
    
    # Update
    
    pygame.display.update()
    


# Age Check

screen.fill('black')


while age:
    
    for event in pygame.event.get():
        
        # Check for the X button
        if event.type == pygame.QUIT:
            pygame.quit()
        
            
    #### Draw ####
    
    # Draw Road
    
    screen.fill('grey')
    pygame.draw.rect(screen, (0, 100, 50), (0, 0, 200, HEIGHT))
    pygame.draw.rect(screen, (0, 100, 50), (WIDTH - 200, 0, 200, HEIGHT))
    
    # Text
    
    screen.blit(year_text, (0, (HEIGHT // 2) - 200))
    screen.blit(year2_text, (0, ((HEIGHT // 2) - 200) + 50))
    
    # Cars
    
    screen.blit(cars, ((WIDTH // 2) - 100, HEIGHT // 2))
    
    # Keys
    

    
    key = pygame.key.get_pressed()
    
    # 1990 - Old
    
    if key[pygame.K_1]:
        mode = 'classic mode'
        age = False
        car_select = True
        
    # 2023 - new
    
    if key[pygame.K_2]:
        mode = 'new mode'
        age = False
        car_select = True
        
    # Update
    
    pygame.display.update()
    

# Car Select

screen.fill('black')

time.sleep(0.50)

while car_select:
    
    for event in pygame.event.get():
        
        # Check for the X button
        if event.type == pygame.QUIT:
            pygame.quit()
        
            
    #### Draw ####
    
    # Draw Road
    
    screen.fill('grey')
    pygame.draw.rect(screen, (0, 100, 50), (0, 0, 200, HEIGHT))
    pygame.draw.rect(screen, (0, 100, 50), (WIDTH - 200, 0, 200, HEIGHT))
    
    # Draw Text
    
    screen.blit(choose_car_text, (0, 0))
    
    # Keys
    

    
    key = pygame.key.get_pressed()
    
    if mode == 'classic mode':
        
        screen.blit(old_cars, (50, (HEIGHT // 2) - 100))
        
        if key[pygame.K_1]:
            car = old_ferrari
            car_select = False
        
        if key[pygame.K_2]:
            mode = old_williams
            car_select = False
            
        if key[pygame.K_3]:
            mode = old_mclaren
            car_select = False
            
            
    if mode == 'new mode':
        
        screen.blit(new_cars, (50, (HEIGHT // 2) - 100))
        
        if key[pygame.K_1]:
            car = new_ferrari
            car_select = False
        
        if key[pygame.K_2]:
            car = new_williams
            car_select = False
            
        if key[pygame.K_3]:
            car = new_mclaren
            car_select = False
            
    # Update
    
    pygame.display.update()
    
    
screen.fill('black') 

run = True




# Objects

player = Car(WIDTH // 2, HEIGHT - 100, car, screen)

# Sounds
engine_sound.play(-1)
background_music.stop()

# Game Loop


while run:
    
    for event in pygame.event.get():
        
        # Check for the X button
        if event.type == pygame.QUIT:
            run = False
        
            
    #### Draw ####
    
    # Draw Road
    
    screen.fill('grey')
    pygame.draw.rect(screen, (0, 100, 50), (0, 0, 100, HEIGHT))
    pygame.draw.rect(screen, (0, 100, 50), (WIDTH - 100, 0, 100, HEIGHT))
    
    # Draw Car
    
    player.draw()
    
    # Move
    
    player.move()
    player.keys(pygame.key.get_pressed())
    
    # Update
    
    pygame.display.update()
    
    
# Quit the Game

pygame.quit()