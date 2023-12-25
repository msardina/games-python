# init
import pygame
import random
import time
from pygame import mixer
pygame.init()
mixer.init()

# constants
WIDTH = 1200
HEIGHT = 800
FPS = 60

# vars
run = True
clock = pygame.time.Clock()

# imgs
alien_img = pygame.image.load('assets/alien.png')
player_img = pygame.image.load('assets/spaceman.png')

# sounds

backround_msc = pygame.mixer.Sound('sound/background.wav')
backround_msc.play(-1)

# setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Warrior I - Macia Productions')

# class

class Player:
    
    def __init__(self, x, y, img=None):
        self.x = x
        self.y = y
        self.img = img
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        
    def move(self, keys, speed):
        if keys[pygame.K_UP]:
            self.y -= speed
        if keys[pygame.K_DOWN]:
            self.y += speed
        if keys[pygame.K_RIGHT]:
            self.x += speed
        if keys[pygame.K_LEFT]:
            self.x -= speed
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def collision(self, obstacles):
        
        for obstacle in obstacles:
            collide = pygame.Rect.colliderect(self.rect, obstacle.rect)
            collision_data = [obstacle, collide]
            return collision_data
        
class Obstacle:
    
    def __init__(self, x, y, img=None):
        self.x = x
        self.y = y
        self.img = img
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        
    def move(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
# objects

player = Player(100, HEIGHT // 2, player_img)
alien = Obstacle(WIDTH // 2, HEIGHT // 2, alien_img)
obstacles = [alien]

# main loop

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # draw screen
    screen.fill((0, 0, 20))
    player.draw()
    alien.draw()
    
    # move screen
    player.move(pygame.key.get_pressed(), 4)
    alien.move()
    
    # collision
    if player.collision(obstacles)[1] == True:
        run = False
        
    # update screen
    clock.tick(FPS)
    pygame.display.update()
    
# quit game
pygame.quit()
quit()

