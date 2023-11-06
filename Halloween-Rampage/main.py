# Init

import pygame
import random
from pygame import mixer
pygame.init()
mixer.init()

# Images

title_img = pygame.image.load('assets/title scene.png')
start_btn = pygame.image.load("assets/play button.png")
start_hover_btn = pygame.image.load("assets/play button hover.png")

# Sounds

background_msc = pygame.mixer.Sound("sound/thriller.wav")
sfx_msc = pygame.mixer.Sound("sound/sfx-background.wav")
background_msc.play(-1)
sfx_msc.play(-1)

# Vars

run = True

# Const

WIDTH = title_img.get_width()
HEIGHT = title_img.get_height()

# Setup Screen

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Halloween Rampage || Halloween Special")

# Classes

class Button:
    
    def __init__(self, x, y, hover, normal):
        self.clicked = False
        self.x = x
        self.y = y
        self.img = normal
        self.state = 'normal'
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.normal = normal
        self.hover = hover
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        
        pos = pygame.mouse.get_pos()
        
        # Change State
        if self.rect.collidepoint(pos):
            self.state = 'hover'
        else:
            self.state = 'normal'

        # Change Img using State
        if self.state == 'hover':
            self.img = self.hover
        else:
            self.img = self.normal
            
        # Change size of rect
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        

        screen.blit(self.img, (self.x, self.y))
        
    def click(self):
        
        if self.state == 'hover':
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print('click')

            
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False



        
# Objects

start_button = Button(WIDTH // 2 - 70, HEIGHT // 2, start_hover_btn, start_btn)

# Main Loop

while run:

    # Event Handler
    for event in pygame.event.get():
        
        # Check for X Button
        if event.type == pygame.QUIT:
            run = False

    # Draw

    screen.blit(title_img, (0, 0))
    start_button.draw()
    #print(start_button.clicked)
    if start_button.clicked == True:
        run = False

        
    # Move
    
    # Update
    
    pygame.display.update()
    
pygame.quit()
quit()