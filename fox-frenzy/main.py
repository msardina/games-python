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
fox_3 = pygame.image.load('assets/fox3.png')
cactus_img = pygame.image.load('assets/cactus.png')
floor_img = pygame.image.load('assets/floor.png')

#const
WIDTH, HEIGHT = title_screen_img.get_width(), title_screen_img.get_height()
GRAVITY = 0.50
FPS = 80

##setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('FOX FRENZY V 1.0')

#music
retro_music = pygame.mixer.Sound('sound/retro.wav')
jump = pygame.mixer.Sound('sound/jump.wav')
die = pygame.mixer.Sound('sound/die.wav')
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
        self.width = imgs[0].get_width() // 3
        self.height = imgs[0].get_height()
        self.imgs = imgs
        self.frame = 0
        self.elapsed = 0
        self.rect = pygame.Rect(self.x + self.width, self.y + self.height, self.width, self.height)

        
    def draw(self, death):
        
        if death == False:
            self.elapsed += 0.10
            
            if self.elapsed > 1:
                if self.frame == 0:
                    self.frame = 1
                else:
                    self.frame = 0
                self.elapsed = 0
        else:
            self.frame = 2
            
        screen.blit(self.imgs[self.frame], (self.x, self.y))
        #pygame.draw.rect(screen, (0, 0, 0), self.rect)
        
    def move(self, keys):
        self.y += self.dy
                
        if self.y < ((HEIGHT - self.height) - 100):
            self.dy += GRAVITY
        if self.y > ((HEIGHT - self.height) - 100):
            self.y = ((HEIGHT - self.height) - 100)
            
        if self.y == ((HEIGHT - self.height) - 100):
            if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                self.dy = -13
                jump.play()
                
        self.rect = pygame.Rect(self.x + self.width, self.y, self.width, self.height)
        
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
        self.x -= 10
        if self.x < 0 - self.width:
            self.x = WIDTH
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

#title screen
play = font.render(f'Press Enter to Play', True, (0, 0, 0))
game_over = title_font.render(f'Game Over!', True, (0, 0, 0))

def start_screen():

    start = True
    
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


def game():
    

    #objects
    player = Player(50, HEIGHT - 200, [fox_1, fox_2, fox_3])
    cactus = Cactus(WIDTH, HEIGHT - 250, cactus_img)
    floor1 = ScrollingSurface(0, HEIGHT - floor_img.get_height(), floor_img)
    floor2 = ScrollingSurface(WIDTH, HEIGHT - floor_img.get_height(), floor_img)
    
    #vars
    run = True
    score = 0
    dead = False
    
    # game loop
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        #collisions
        if pygame.Rect.colliderect(player.rect, cactus.rect):
            dead = True

            
        #score
        score += 1
        score_txt = title_font.render(f'{score}', True, (0, 0, 0))

        #draw screen
        screen.fill((0,206,209))
        screen.blit(background_img, (0, 0))
        floor1.draw()
        floor2.draw()
        cactus.draw()
        player.draw(dead)
        screen.blit(score_txt, (0, 0))

        
        #move screen
        player.move(pygame.key.get_pressed())
        floor1.move()
        floor2.move()
        cactus.move()

        #play gameover sound and display text
        
        if dead:
            screen.blit(game_over, (WIDTH // 2 - (game_over.get_width() // 2), 100))
            player.move(pygame.key.get_pressed())
            pygame.display.update()
            die.play()
            time.sleep(3)
            run = False
            
        #update
        clock.tick(FPS)
        pygame.display.update()

#game
game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            
    start_screen()
    game()

        
    
#quit the game
pygame.quit()
quit()