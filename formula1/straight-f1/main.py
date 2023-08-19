# Importations

import pygame
import random
import time
from pygame import mixer


# Initialize
pygame.init()

# Variables
run = True
angle = 0
speed = -5
speed_gui = 0
dodged = 0
lap = 1
overtaken = 0
survived_time = 0
font = pygame.font.SysFont(None, 50)

# Constantes
WIDTH, HEIGHT = 1200, 800

# Images
background = pygame.image.load('imgs/road.svg')
cockpit = pygame.image.load('imgs/cockpit.svg')

# Music
mixer.music.load('engine.wav')
mixer.music.play(-1)
# Classes

class Player():
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.dx = 0
        self.dy = 0
        self.img =  pygame.image.load('imgs/car.png')
        self.img = pygame.transform.rotozoom(self.img, 0, 0.75)
        self.rect = pygame.Rect(x, y, 54, 130)
        
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        #pygame.draw.rect(self.screen, (255, 255, 255), self.rect)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.rect = pygame.Rect(self.x, self.y, 54, 130)
        
class Wheel():
    def __init__(self, x, y, screen):
        self.screen = screen

        self.img = pygame.image.load('imgs/ferrari wheel.png')
        self.center = (x, y)


        
    def draw(self, rotation):
        img = pygame.transform.rotate(self.img, rotation)
        rect = img.get_rect()
        rect.center = self.center
        self.screen.blit(img, rect)
        
class Enemy():
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.screen = screen
        self.img = pygame.image.load('imgs/enemy car2.png')
        self.img = pygame.transform.rotozoom(self.img, 0, 0.75)
        self.rect = pygame.Rect(x, y, 54, 131)

        
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        #pygame.draw.rect(self.screen, (255, 255, 255), self.rect)
        
    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.rect = pygame.Rect(self.x, self.y, 54, 131)
        
# Set Up Screen

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Formula 1 Grand Prix')

# Objects
player = Player(WIDTH // 2, HEIGHT - 400, screen)
wheel = Wheel(WIDTH / 2 + 50, HEIGHT - 100, screen)
enemy_car = Enemy(WIDTH // 2, 0, screen)
# Main loop

while run:
    
    screen.fill('Black')
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        
    # Key Presses
    keys = pygame.key.get_pressed()
    
    
    if keys[pygame.K_UP] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        if speed_gui < 350:
                if speed_gui == 0:
                    speed_gui += 100
                    mixer.music.play(-1)
                else:
                    speed_gui += 5
                    
    else:
        if speed_gui > 100:
            speed_gui -= 2
    if keys[pygame.K_RIGHT]:
        player.dx = 5
        angle = -45
        
    elif keys[pygame.K_LEFT]:
        player.dx = -5
        angle = 45

        
    else:
        player.dx = 0
        angle = 0

    if not enemy_car.y > HEIGHT - cockpit.get_height():
        enemy_car.dy = 10
    else:
        overtaken += 1
        enemy_car.y = 0
        enemy_car.x = random.randint(400, WIDTH - 250)
        
        


        
    # Move Player
    player.move()
    enemy_car.move()
    
    # Draw Screen
    screen.blit(background, (0, 0))
    screen.blit(cockpit, (0, HEIGHT - 200))
    player.draw()
    wheel.draw(angle)
    enemy_car.draw()
    

    # Set all Measurments
    speed_text = font.render(f'Speed: {speed_gui}', True, (255, 255, 255))
    lap_text = font.render(f'Lap: {lap}', True, (255, 255, 255))
    overtaken_text = font.render(f'Passed: {overtaken}', True, (255, 255, 255))
    game_over = font.render(f'Game Over! You Crashed!', True, (255, 255, 255))
    survived = font.render(f'Time Survived: {survived_time}', True, (255, 255, 255))
    
    if overtaken:
        overtaken += 1
        
    # Draw Text
    screen.blit(speed_text, (WIDTH / 2 + 290, HEIGHT - 190))
    screen.blit(lap_text, (WIDTH / 2 + 290, HEIGHT - 150))
    screen.blit(overtaken_text, (WIDTH / 2 + 290, HEIGHT - 110))
    
    # Update
    
    pygame.display.flip()
    
    
    # Check Collisions
    collide = pygame.Rect.colliderect(enemy_car.rect, player.rect)
    
    # Return Boolean ^
    
    if collide:
        mixer.music.load('crash.wav')
        mixer.music.play(0)
        time.sleep(3)
        run = False

screen.blit(game_over, (WIDTH / 2 , HEIGHT / 2))

pygame.quit()