import pygame
import time
import random
from pygame import mixer
from pygame import font

# Initialise Packages
mixer.init()
font.init()
pygame.init()




# Images

titi = pygame.image.load('assets/Titi.svg')
pongo = pygame.image.load('assets/Pongo.svg')
kunga = pygame.image.load('assets/Kunga.svg')
hipo = pygame.image.load('assets/Hipo.svg')
gufi = pygame.image.load('assets/Gufi.svg')
background = pygame.image.load('assets/l1.svg')
carrot = pygame.image.load('assets/carrot.svg')
copo = pygame.image.load('assets/copo.svg')
start_screen = pygame.image.load('assets/Start Screen.svg')
char_select_background = pygame.image.load('assets/character select.svg')

# Vars
run = True
timer = 0
score = 0
p1_score = 0
start_screen_button = True
p2_score = 0
player_1_chacter = copo
player_2_chacter = titi

    
    
# Text Management

font = pygame.font.SysFont(None, 50)
title_font = pygame.font.SysFont(None, 100)


# Constants
WIDTH, HEIGHT = background.get_width(), background.get_height()

# Setup Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('World of Titi - Msardina Productions')

# Music
eat_sound = pygame.mixer.Sound('sound/Chomp.wav')
background_music = pygame.mixer.Sound('sound/background.wav')
title_sound = pygame.mixer.Sound('sound/title_sound.wav')
connect = pygame.mixer.Sound('sound/Connect.wav')
title_sound.play()
background_music.play(-1)

# Classes
class Entity:
    def __init__(self, x, y, width, height, img, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = img
        
    def move(self, keys, player_chosen):
        if player_chosen == True:
            if keys[pygame.K_UP]:
                self.y += -3
            elif keys[pygame.K_DOWN]:
                self.y += 3
                
            if keys[pygame.K_RIGHT]:
                self.x += 3
            elif keys[pygame.K_LEFT]:
                self.x += -3
        elif player_chosen == False:
            if keys[pygame.K_w]:
                self.y += -3
            elif keys[pygame.K_s]:
                self.y += 3
                
            if keys[pygame.K_d]:
                self.x += 3
            elif keys[pygame.K_a]:
                self.x += -3

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        
        #pygame.draw.rect(self.screen , (0, 255, 255), self.rect)
        screen.blit(self.img, (self.x, self.y))

class Carrota:
    def __init__(self, x, y, width, height, img, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = img
        
    def move(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        #pygame.draw.rect(self.screen , (0, 255, 255), self.rect)
        screen.blit(self.img, (self.x, self.y))

    def get_rect(self):
        return self.rect
    
    def reset(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)

# Pick Player Chars

# Player 1
charcter_num = random.randint(1, 6)
print(charcter_num)

if charcter_num == 1:
    player_1_chacter = titi
if charcter_num == 2:
    player_1_chacter = copo
if charcter_num == 3:
    player_1_chacter = pongo
if charcter_num == 4:
    player_1_chacter = gufi
if charcter_num == 5:
    player_1_chacter = hipo
if charcter_num == 6:
    player_1_chacter = kunga

# Player 2
charcter_num = random.randint(1, 6)
print(charcter_num)

if charcter_num == 1:
    player_2_chacter = titi
if charcter_num == 2:
    player_2_chacter = copo
if charcter_num == 3:
    player_2_chacter = pongo
if charcter_num == 4:
    player_2_chacter = gufi
if charcter_num == 5:
    player_2_chacter = hipo
if charcter_num == 6:
    player_2_chacter = kunga

# Create Objects
player1 = Entity(WIDTH // 2, HEIGHT // 2, player_1_chacter.get_width(), player_1_chacter.get_height(), player_1_chacter, screen)
player2 = Entity(WIDTH // 2, HEIGHT // 2, player_2_chacter.get_width(), player_2_chacter.get_height(), player_2_chacter, screen)
carrota = Carrota(random.randint(0, WIDTH), random.randint(0, HEIGHT), carrot.get_width(), carrot.get_height(), carrot, screen)

# Start presentation
title = title_font.render(f'Los Juguetes', True, (0, 0, 0))
play = font.render(f'Press Enter to Play', True, (0, 0, 0))
screen.blit(start_screen, (0, 0))
screen.blit(title, (450, 100))
screen.blit(play, (0, HEIGHT - 50))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        connect.play()
        break


# Char select
time.sleep(1)
screen.fill('black')
choose_text_p1 = title_font.render(f'Choose Your Character', True, (0, 0, 0))
screen.blit(char_select_background, (-67, 0))
screen.blit(choose_text_p1, ((WIDTH // 2) - 100, HEIGHT // 2))
pygame.display.flip()
p1_char = 1
p2_char = 2

# next is the main game loop
while run:
    # X Button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    # Key Presses
    keys = pygame.key.get_pressed()

    player1.move(keys, True)
    player2.move(keys, False)
    

    # Collisions
    collide = pygame.Rect.colliderect(carrota.get_rect(), player1) or pygame.Rect.colliderect(carrota.get_rect(), player2)
    collide_p1 = pygame.Rect.colliderect(carrota.get_rect(), player1)
    collide_p2 = pygame.Rect.colliderect(carrota.get_rect(), player2)
    if collide:
        eat_sound.play()
        carrota.reset()
        if collide_p1:
            p1_score += 1

        if collide_p2:
            p2_score += 1
        
    # Move Carrota
    if timer >= 2:
        carrota.reset()
        timer = 0
        
    # Update Timer
    timer += 0.01
    
    # Move Screen Objects
    carrota.move()
    
    # Text Measurements
    
    p1_score_t = font.render(f'Player 1 Score: {p1_score}', True, (0, 255, 255))
    p2_score_t = font.render(f'Player 2 Score: {p2_score}', True, (255, 0, 0))
    
    # Draw Screen
    screen.blit(background, (0, 0))
    player1.draw()
    player2.draw()
    carrota.draw()
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 300, 100))
    screen.blit(p1_score_t, (0, 0))
    screen.blit(p2_score_t, (0, 50))
    
    
    # Update
    pygame.display.flip()
    
pygame.quit()