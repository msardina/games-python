# Importations

import pygame
import random
from pygame import mixer

# Initialise Packages

pygame.init()
mixer.init()

# Images
background = pygame.image.load('assets/background.png')
level = pygame.image.load('assets/level.png')
frog = pygame.image.load('assets/frog.png')
lilly_pad_img = pygame.image.load('assets/lily-pad.png')

# Music
background_music = pygame.mixer.Sound('sound/background.wav')
connect = pygame.mixer.Sound('sound/connect.wav')
background_music.play(-1)

# Variables

run = False
start = True
timer = 0
collide_frog_lilly1 = False
collide_frog_lilly2 = False
first_click = False
lilly_created = False
# Constantes

WIDTH, HEIGHT = background.get_width(), background.get_height()

# Setup Screen

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Frog Pond')

# Classes

class Player:
    def __init__(self, x, y, width, height, img, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = img
        self.speed = 0
    def move(self):
        self.y += self.speed
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        #pygame.draw.rect(self.screen , (0, 255, 255), self.rect)
        screen.blit(self.img, (self.x, self.y))

class LillyPad:
    def __init__(self, x, y, width, height, img, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = img
        
    def move(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        #pygame.draw.rect(self.screen , (0, 255, 255), self.rect)
        screen.blit(self.img, (self.x, self.y))
        
# Objects

player = Player(0, HEIGHT - 100, frog.get_width(), frog.get_height(), frog, screen)
lilly_pad = LillyPad(random.randint(100, 500), 0, lilly_pad_img.get_width(), lilly_pad_img.get_width(), lilly_pad_img, screen)


# Start Loop

while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
    
    # Keys
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RETURN]:
        connect.play()
        start = False
        break
    
    # Draw
    
    screen.blit(background, (0, 0))
    
    # Move
    
    # Update
    
    pygame.display.flip()

run = True

# Reset Screen
screen.fill('black')

lilly_pad2 = lilly_pad
# Game Loop

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            player.x = mouse_pos[0]
            player.y = mouse_pos[1]
            first_click = True

        
            

            
    # Move Lilly Pad
    lilly_pad.y += 2
    lilly_pad2.y += 2
    
    if lilly_pad.y > HEIGHT:
        lilly_pad.y = 0
        lilly_pad.x = random.randint(100, 500)
        
    if lilly_pad2.y > HEIGHT:
        lilly_pad2.y = 0
        lilly_pad2.x = random.randint(100, 500)
    
    # Move Frog on lilly pad
    collide_frog_lilly1 = pygame.Rect.colliderect(player.rect, lilly_pad.rect)
    collide_frog_lilly2 = pygame.Rect.colliderect(player.rect, lilly_pad2.rect)
    
    if collide_frog_lilly1:
        player.speed = 2
        print(collide_frog_lilly1)

    elif collide_frog_lilly2:
        player.speed = 2
        print(collide_frog_lilly2)



    # Draw

    screen.blit(level, (0, 0))
    lilly_pad.draw()
    lilly_pad2.draw()
    player.draw()

    # Move
    lilly_pad.move()
    lilly_pad2.move()
    player.move()
    
    # Update Timer
    
    if timer < 1:
        timer += 0.010
        
    if timer >= 1:
        if lilly_created == False:
            lilly_pad2 = LillyPad(random.randint(100, 500), 0, lilly_pad_img.get_width(), lilly_pad_img.get_width(), lilly_pad_img, screen)
            lilly_created = True
        timer = 0
        
    # Update
    
    pygame.display.flip()
        
pygame.quit()
