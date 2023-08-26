import pygame
import random
from pygame import mixer

# Initialise

pygame.init()
mixer.init()

# Variables

run = True
timer = 0

# Constant
WIDTH, HEIGHT = 1200, 800
GRAVITY = 0.25

# Imgs

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('NASA Space Ship')

# Music

# Classes

class Player:
    def __init__(self, x, y, width, height, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)
        
    def move(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
class Floor:
    def __init__(self, x, y, width, height, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        pygame.draw.rect(self.screen, (0, 255, 0), self.rect)
        
    def move(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
# Objects
player = Player(WIDTH // 2, HEIGHT // 2, 50, 100, screen)
floor = Floor(0, HEIGHT - 50, WIDTH, 50, screen)
# Main Game Loop

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        
    # Move Screen
    player.move()
    player.y += GRAVITY
    
    # Draw Screen
    screen.fill('light blue')
    floor.draw()
    player.draw()
    
    # Collisions
    
    collide = pygame.Rect.colliderect(floor.rect, player.rect)
    
    if collide:
        player.y = floor.y - 100

    # Gravity
    
    # Keys
    
    keys = pygame.key.get_pressed()
    

    if keys[pygame.K_RIGHT]:
        player.x += 1
    if keys[pygame.K_LEFT]:
        player.x -= 1
    if keys[pygame.K_UP]:
        player.y -= 0.50
        
            


    # Set Text
    
    # Update Screen
    pygame.display.flip()
    
pygame.quit()