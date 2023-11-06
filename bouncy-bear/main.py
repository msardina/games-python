# Initialise game

import pygame
from pygame import mixer
mixer.init()

# Variables

run = True

# Constants

WIDTH, HEIGHT = 1200, 800

# Setup Screen

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncy Bear")

# Images

trampoline_img = pygame.image.load("assets/trampoline.png")

# Music

background_music = pygame.mixer.Sound("music/background.wav")
background_music.play()

# Classes

class Tramp:
    
    def __init__(self, x, y, img, screen):
        self.x = x
        self.y = y
        self.img = img
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
    
    def move(self, mouse_pos):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.x = mouse_pos[0] - self.width // 2

class Bear:
    
    def __init__(self, x, y, img, screen):
        self.x = x
        self.y = y
        self.img = img
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
    
    def move(self, mouse_pos):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
# Objects

player = Tramp(WIDTH // 2, HEIGHT - 150, trampoline_img, screen)

# Hide Mouse


# Game Loop

while run:
    
    for event in pygame.event.get():
        
        # X Button
        if event.type == pygame.QUIT:
            run = False
    
    # Move
    
    player.move(pygame.mouse.get_pos())
    
    # Draw
    
    screen.fill("light blue")
    
    # Draw floor
    
    pygame.draw.rect(screen, (0, 100, 0), (0, HEIGHT - 200, WIDTH, 200))

    # Draw Sun
    
    pygame.draw.circle(screen, (255, 255, 0), (0, 0), 100)
    
    player.draw()
    

    # Update
    
    pygame.display.update()