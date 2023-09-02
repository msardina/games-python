# Import

import pygame
import random
from pygame import mixer


# Init

pygame.init()
mixer.init()


# Images

background_img = pygame.image.load('assets/background.png')
bird_img = pygame.image.load('assets/flappy bird.png')
pipe_b_img = pygame.image.load('assets/pipe_bottom.png')
pipe_u_img = pygame.image.load('assets/pipe_up.png')

# Music


# Vars

run = True

# Const

WIDTH = background_img.get_width()
HEIGHT = background_img.get_height()

# Setup Screen

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Duck || Marcos Sardina Productions')

# Classes

class Bird:
    
    def __init__(self, x, y, max_y, img, screen):
        self.x = x
        self.y = y
        self.vel = 0
        self.img = img
        self.screen = screen
        self.width = img.get_width()
        self.height = img.get_height()
        self.max_y = max_y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        
    def move(self):
        self.vel += 0.50
        self.y += self.vel
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def keys(self, keys):
        if keys[pygame.K_UP]:
            self.vel = -10
    
    def check_death(self):
        
        if self.y > self.max_y:
            return True
        else:
            return False

class Pipe:
    
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
        self.x -= 10
        if self.x < 0:
            self.x = WIDTH
            
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def collide_check(self, other_rect):
        
        if pygame.Rect.colliderect(self.rect, other_rect):
            
            return True
        else:
            return False
        
# Objects

player = Bird(100, HEIGHT // 2, HEIGHT, bird_img, screen, )
pipe_b = Pipe(WIDTH, HEIGHT - pipe_b_img.get_height(), pipe_b_img.get_width(), pipe_b_img.get_height(), pipe_b_img, screen)
pipe_u = Pipe(WIDTH, 0, pipe_u_img.get_width(), pipe_u_img.get_height(), pipe_u_img, screen)

# Game Loop

while run:
    
    
    for event in pygame.event.get():
        
        # X button check
        if event.type == pygame.QUIT:
            run = False
    

        
    # Keys
    keys = pygame.key.get_pressed()
    
    player.keys(keys)
    
    # Draw
    
    screen.blit(background_img, (0, 0))
    player.draw()
    pipe_b.draw()
    pipe_u.draw()
    
    # Move
    
    player.move()
    pipe_b.move()
    pipe_u.move()
    
    # Check for the player going out of screen
    
    if player.check_death():
        run = False
    
    # Collisions
    
    if pipe_b.collide_check(player.rect):
        run = False
    
    if pipe_u.collide_check(player.rect):
        run = False
    # Update
    pygame.display.update()
    
# Quit Game
pygame.quit()