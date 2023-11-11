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
ghost_img = pygame.image.load('assets/player.png')
road_img = pygame.image.load('assets/road.png')
yellow_candy_img = pygame.image.load('assets/yellow.png')
purple_candy_img = pygame.image.load('assets/purple.png')
blue_candy_img = pygame.image.load('assets/blue.png')
green_candy_img = pygame.image.load('assets/green.png')
car_img = pygame.image.load('assets/car.png')
sign_img = pygame.image.load('assets/sign.png')
pumpkin_img = pygame.image.load('assets/pumpkin.png')

# Sounds

#background_msc = pygame.mixer.Sound("sound/thriller.wav")
sfx_msc = pygame.mixer.Sound("sound/sfx-background.wav")
#background_msc.play(loops=-1, maxtime=5000)
sfx_msc.play(loops=-1)

# Vars

start = True
run = False
clock = pygame.time.Clock()
candy_timer = 0
score = 0

# Const

WIDTH = title_img.get_width()
HEIGHT = title_img.get_height()
FPS = 60
# Setup Screen

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Halloween Rampage || Halloween Special")

# Text/Fonts

font = pygame.font.SysFont(None, 50)
title_font = pygame.font.SysFont(None, 100)

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

class Player:
    
    def __init__(self, x, y, img):
        
        self.x = x
        self.y = y
        self.img = img
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        
    def move(self, keys):
        
        if keys[pygame.K_UP]:
            self.y -= 4
            
        if keys[pygame.K_DOWN]:
            self.y += 4
        
        if keys[pygame.K_RIGHT]:
            self.x += 4
            
        if keys[pygame.K_LEFT]:
            self.x -= 4
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def collide(self, rect):
        
        if pygame.Rect.colliderect(self.rect, rect):
            return True
        else:
            return False
class ScrollingSurface:
    
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
        self.y += 2
        if self.y > HEIGHT:
            self.y = HEIGHT * -1

class Candy:
    
    def __init__(self, x, y, img):
        
        self.x = x
        self.y = y
        self.img = img
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        
    def reset(self):
        self.y = 0
        self.x = random.randint(90, 550)
        
    def move(self):
        self.y += 2
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        if self.y > HEIGHT:
            self.reset()
    
    def collide(self, player):
        
        if pygame.Rect.colliderect(self.rect, player):
            self.reset()
            return True
            
class Obstacle:
    
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.width = img.get_width()
        self.height = img.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        
    def move(self):
        if self.img == car_img:
            self.y += 2
        else:
            self.y += 2
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def off_level(self):
        if self.y > HEIGHT:
            self.y = 0
            self.x = random.randint(90, 550)
    
# Objects

start_button = Button(WIDTH // 2 - 70, HEIGHT // 2, start_hover_btn, start_btn)
blank_button = Button(WIDTH // 2 - 70, HEIGHT // 2 + 100, blank_hover_btn, blank_btn)
blank_button_2 = Button(WIDTH // 2 - 70, HEIGHT // 2 + 200, blank_hover_btn, blank_btn)
buttons = [start_button, blank_button, blank_button_2]
player = Player(WIDTH // 2, 300, ghost_img)
road = ScrollingSurface(0, 0, road_img)
road_2 = ScrollingSurface(0, HEIGHT * -1, road_img)
candys = [Candy(WIDTH // 2, 0, yellow_candy_img), Candy(WIDTH // 2, 0, green_candy_img), Candy(WIDTH // 2, 0, purple_candy_img), Candy(WIDTH // 2, 0, blue_candy_img), Candy(random.randint(90, 550), 0, yellow_candy_img), Candy(WIDTH // 2, 0, green_candy_img), Candy(WIDTH // 2, 0, purple_candy_img), Candy(WIDTH // 2, 0, blue_candy_img)]
car = Obstacle(random.randint(90, 550), 0, car_img)
sign = Obstacle(random.randint(90, 550), -300, sign_img)
pumpkin = Obstacle(random.randint(90, 550), -500, pumpkin_img)


    
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

run = True

# Main Loop

while run:

    # Event Handler
    for event in pygame.event.get():
        
        # Check for X Button
        if event.type == pygame.QUIT:
            run = False

    # Candy score
    
    score_txt = font.render(f'{score}', True, (0, 0, 0))
    
    # Draw
    
    road.draw()
    road_2.draw()
    player.draw()
    car.draw()
    sign.draw()
    pumpkin.draw()
    screen.blit(score_txt, (WIDTH // 2, HEIGHT - 50))
    
    for candy in candys:
        candy.draw()
        candy.move()
        candy.collide(player.rect)
        candy.collide(car.rect)
        candy.collide(pumpkin.rect)
        candy.collide(sign.rect)
        if candy.collide(player.rect):
            score += 5


        
    # Move
    

    player.move(pygame.key.get_pressed())
    if player.collide(car.rect):
        run = False
    if player.collide(sign.rect):
        run = False
    if player.collide(pumpkin.rect):
        run = False
        
    road.move()
    road_2.move()
    car.move()
    car.off_level()
    sign.move()
    sign.off_level()
    pumpkin.move()
    pumpkin.off_level()
    
    # Update
    
    clock.tick(FPS)
    pygame.display.update()
    
pygame.quit()
quit()