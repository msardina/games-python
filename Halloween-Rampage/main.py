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
blank_btn = pygame.image.load('assets/blank button.png')
blank_hover_btn = pygame.image.load('assets/blank button hover.png')

# Sounds

#background_msc = pygame.mixer.Sound("sound/thriller.wav")
sfx_msc = pygame.mixer.Sound("sound/sfx-background.wav")
#background_msc.play(loops=-1, maxtime=5000)
sfx_msc.play(loops=-1)

# Vars

start = True
run = False

# Const

WIDTH = title_img.get_width()
HEIGHT = title_img.get_height()

# Setup Screen

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Halloween Rampage || Halloween Special")

# Classes

class Button:
    
    def __init__(self, x, y, hover_img, normal_img):
        self.clicked = False
        self.x = x
        self.y = y
        self.img = normal_img
        self.hovering = False
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.normal_img = normal_img
        self.hover_img = hover_img
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def update(self):
        
        pos = pygame.mouse.get_pos()
        
        # Change State
        if self.rect.collidepoint(pos):
            self.hovering = True
        else:
            self.hovering = False

        # Change Img using State
        self.img = self.hover_img if self.hovering else self.normal_img
            
        # Redo rect of button
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # if hovering, check if press
        if self.hovering:            
            # left button clicked
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        screen.blit(self.img, (self.x, self.y))
    
    def is_clicked(self):
        return self.clicked


        
# Objects

start_button = Button(WIDTH // 2 - 70, HEIGHT // 2, start_hover_btn, start_btn)
blank_button = Button(WIDTH // 2 - 70, HEIGHT // 2 + 100, blank_hover_btn, blank_btn)
blank_button_2 = Button(WIDTH // 2 - 70, HEIGHT // 2 + 200, blank_hover_btn, blank_btn)
buttons = [start_button, blank_button, blank_button_2]

# Start Loop

while start:

    # Event Handler
    for event in pygame.event.get():
        
        # Check for X Button
        if event.type == pygame.QUIT:
            pygame.quit()

    # Draw

    screen.blit(title_img, (0, 0))
    
    for button in buttons:  
        button.update()
    
    if start_button.is_clicked():
        start = False
        run = True

    # Update
    
    pygame.display.update()

# Fill black
screen.fill('black')

# Main Loop

while run:

    # Event Handler
    for event in pygame.event.get():
        
        # Check for X Button
        if event.type == pygame.QUIT:
            run = False

    # Draw

        
    # Move
    
    # Update
    
    pygame.display.update()
    
pygame.quit()
quit()