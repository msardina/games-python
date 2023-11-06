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
pipe_b_img = pygame.image.load('assets/pipe_bottom_long.png')
pipe_u_img = pygame.image.load('assets/pipe_bottom_long.png')

# Music

flap = pygame.mixer.Sound('music/flap.mp3')
# Vars

run = True
clock = pygame.time.Clock()

# Const

WIDTH = background_img.get_width()
HEIGHT = background_img.get_height()
FPS = 60

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
        self.release = True
        
        
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        
    def move(self):
        self.vel += 0.50
        self.y += self.vel
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def keys(self, keys):
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            if self.release:
                flap.play()
                self.vel = -10
            self.release = False
            
        else:
            self.release = True
            
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
            self.y = random.randint(HEIGHT - self.img.get_height(), HEIGHT - 200)
            
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def collide_check(self, other_rect):
        
        if pygame.Rect.colliderect(self.rect, other_rect):
            
            return True
        else:
            return False
        
# Objects

player = Bird(100, WIDTH // 2, HEIGHT,  bird_img, screen)
pipe_b = Pipe(WIDTH, WIDTH // 2, pipe_b_img.get_width(), pipe_b_img.get_height(), pipe_b_img, screen)
#pipe_u = Pipe(WIDTH, pipe_b.y + (pipe_u_img.get_height() - 200), pipe_u_img.get_width(), pipe_u_img.get_height(), pipe_u_img, screen)

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
    #pipe_u.draw()
    
    # Move
    
    player.move()
    pipe_b.move()
    #pipe_u.move()
    #pipe_u.y = 0 + pipe_b.y + (pipe_u_img.get_height() - 200)
    # Check for the player going out of screen
    
    if player.check_death():
        run = False
    
    # Collisions
    
    if pipe_b.collide_check(player.rect):
        run = False
    
    #if pipe_u.collide_check(player.rect):
    #    run = False
        
    # Update
    clock.tick(FPS )
    pygame.display.update()
    
# Quit Game
pygame.quit()