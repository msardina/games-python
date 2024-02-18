import pygame
import math
import time
from pygame import mixer
pygame.init()
mixer.init()

#imgs
title_screen_img = pygame.image.load('assets/title-screen.png')
background_img = pygame.image.load('assets/background.png')
fox_1 = pygame.image.load('assets/fox1.png')
fox_2 = pygame.image.load('assets/fox2.png')
cactus_img = pygame.image.load('assets/cactus.png')

#vars
start = True
run = False

#const
WIDTH, HEIGHT = title_screen_img.get_width(), title_screen_img.get_height()
GRAVITY = 0.50
FPS = 60

##setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('FOX FRENZY BETA')

#music
retro_music = pygame.mixer.Sound('sound/retro.wav')
retro_music.play(-1)

#font
font = pygame.font.SysFont(None, 50)
title_font = pygame.font.SysFont(None, 100)

#clock
clock = pygame.time.Clock()

#classes

class Player:
    def __init__(self, x, y, imgs):
        self.x = x
        self.y = y
        self.dy = 0
        self.width = imgs[0].get_width()
        self.height = imgs[0].get_height()
        self.imgs = imgs
        self.frame = 0
        self.elapsed = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        self.elapsed += 0.10
        
        if self.elapsed > 1:
            if self.frame == 0:
                self.frame = 1
            else:
                self.frame = 0
            self.elapsed = 0
            
        screen.blit(self.imgs[self.frame], (self.x, self.y))
        
    def move(self, keys):
        self.y += self.dy
        

                
        if self.y < ((HEIGHT - self.height) - 100):
            self.dy += GRAVITY
        if self.y > ((HEIGHT - self.height) - 100):
            self.y = ((HEIGHT - self.height) - 100)
            
        if self.y == ((HEIGHT - self.height) - 100):
            if keys[pygame.K_UP]:
                self.dy = -13
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
class Cactus:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        
    def move(self):
        self.x -= 10
        if self.x < 0 - self.width:
            self.x = WIDTH
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


            
#title screen
play = font.render(f'Press Enter to Play', True, (0, 0, 0))

while start:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    #draw screen
    screen.blit(title_screen_img, (0, 0))
    screen.blit(play, (0, HEIGHT - 50))
    
    #exit
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RETURN]:
        start = False
        run = True
        
    #update
    pygame.display.update()

#objects
player = Player(50, HEIGHT - 700, [fox_1, fox_2])
cactus = Cactus(WIDTH, HEIGHT - 250, cactus_img)

# game loop
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    #draw screen
    screen.blit(background_img, (0, 0))
    player.draw()
    cactus.draw()
    
    #move screen
    player.move(pygame.key.get_pressed())
    cactus.move()
    
    #update
    clock.tick(FPS)
    pygame.display.update()
    
#quit the game
pygame.quit()
quit()