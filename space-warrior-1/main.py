# init
import pygame
import random
import time
from pygame import transform
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
level_img = pygame.transform.scale(pygame.image.load('assets/level.png'), (10000, 1300))

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
        self.dx = 0
        self.dy = 0
        
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        
    def move(self, keys, speed):
        if keys[pygame.K_UP]:
            self.dy -= 0.75
        if keys[pygame.K_DOWN]:
            self.dy += 0.75
        if keys[pygame.K_RIGHT]:
            if player.x < WIDTH - 400:
                self.dx += 0.75
        if keys[pygame.K_LEFT]:
            if player.x > 100:
                self.dx -= 0.75
            
        self.x += self.dx
        self.y += self.dy
        self.dx  = self.dx * 0.9
        self.dy = self.dy * 0.9
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

class ScrollingSurface:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
# objects

player = Player(100, HEIGHT // 2, player_img)
alien = Obstacle(WIDTH // 2, HEIGHT // 2, alien_img)
obstacles = [alien]
level = ScrollingSurface(0, 0, level_img)

# main loop

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # draw screen
    level.draw()
    player.draw()
    alien.draw()
    
    # move screen
    player.move(pygame.key.get_pressed(), 4)
    alien.move()
    
    if level.x < -8500:
        level.move(0, 0)
    elif player.x > WIDTH - 400:
        level.move(-10, 0)     
    elif player.x < 200:
        level.move(-3, 0)
    else:
        level.move(-5, 0)

    
    # collision
    if player.collision(obstacles)[1] == True:
        run = False
        
    # update screen
    clock.tick(FPS)
    pygame.display.update()
    
# quit game
pygame.quit()
quit()

