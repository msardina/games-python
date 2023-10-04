# Imports
import random
import pygame
from pygame import mixer

# Init

mixer.init()
pygame.font.init()

# Text Management

font = pygame.font.SysFont(None, 50)
title_font = pygame.font.SysFont(None, 100)


# Images

background_img = pygame.image.load("assets/background.png")
start_screen = pygame.image.load("assets/start-screen.png")
robot_img = pygame.image.load("assets/robo.png")
robot_img_death = pygame.image.load("assets/robo-broken.png")
bolt_img = pygame.image.load("assets/power.png")

# Constants

WIDTH, HEIGHT = background_img.get_width(), background_img.get_height()
FPS = 60

# Variables

clock = pygame.time.Clock()
run = False
start = True
power_timer = 0
sound_timer = 0
score = 0

# Music

background_music = pygame.mixer.Sound("sounds/background.wav")
robot_sound_1 = pygame.mixer.Sound("sounds/buzz whir.wav")
robot_sound_2 = pygame.mixer.Sound("sounds/QSNTNC1.wav")
robot_sound_3 = pygame.mixer.Sound("sounds/computer beeps1.wav")
robot_sound_4 = pygame.mixer.Sound("sounds/computer beeps2.wav")
collect = pygame.mixer.Sound("sounds/coin.wav")
lose_sound = pygame.mixer.Sound("sounds/lose.wav")

#background_music.play(-1)

# Text Prep

score_text = font.render("Score: {score}", True, (0, 0, 0))
game_over_text = title_font.render("Game Over", True, (0, 0, 0))

# Setup Screen

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robo-Top || The AI Masterpiece")


# Classes

class Robot:
    
    def __init__(self, x, y, img, img_death):
        self.x = x
        self.y = y
        self.img = img
        self.img_good = img
        self.img_bad = img_death
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.state = "good"
    
    def img_state(self):
        if self.state == "good":
            self.img = self.img_good
        else:
            self.img = self.img_bad
            
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        
    def move(self, keys):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        if keys[pygame.K_LEFT] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]and self.x > 70:
            self.x -= 3
            
        if keys[pygame.K_RIGHT] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN] and self.x < 831:
            self.x += 3
            
        if keys[pygame.K_UP] and not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and self.y > 0:
            self.y -= 3
            
        if keys[pygame.K_DOWN] and not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and self.y < HEIGHT - 130:
            self.y += 3
            

class Power:
    
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
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def reset(self):
        self.x = random.randint(70, 831)
        self.y = random.randint(0, HEIGHT - 130)

class Energy:
    
    def __init__(self, x, y, power, height, start_width):
        self.x = x
        self.y = y
        self.power = power
        self.height = height
        self.width = self.power
        self.start_width = start_width
        
    def draw(self):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.start_width, self.height))
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width, self.height))

        
    def decrease_power(self):
        self.power -= 0.30
        self.width = self.power
        
    
        
        
# Objects

player = Robot(WIDTH / 2, HEIGHT / 2, robot_img, robot_img_death)
power = Power(0, 0, bolt_img)
energy = Energy((WIDTH - 220), HEIGHT - 30, 200, 20, 200)
power.reset()

# Defs

def start_screen_def():
    start = True
    run = False
    while start:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                
        # Enter
        
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            start = False
            run = True
            
        # Draw
        
        screen.blit(start_screen, (0, 0))
        
        # Update
        
        pygame.display.update()


# Start Loop

start_screen_def()

# Game Loop

run = True

while run:
    
    for event in pygame.event.get():
        
        # X Button
        if event.type == pygame.QUIT:
            run = False

    # Text

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    
    # Collisions
    
    if pygame.Rect.colliderect(player.rect, power.rect):
        power.reset()
        power_timer = 0
        score += 1
        energy.power = 200
        collect.play()
        
    # Power Reset Check
    
    power_timer += 0.10
    if power_timer > 20:
        power_timer = 0
        power.reset()
        
    #  Robot sound timer
    
    sound_timer += 0.10
    if sound_timer > 10:
        robot_sound_num = random.randint(0, 3)
        if robot_sound_num == 0:
            robot_sound_1.play()
        elif robot_sound_num == 1:
            robot_sound_2.play()
        elif robot_sound_num == 2:
            robot_sound_3.play()
        elif robot_sound_num == 3:
            robot_sound_4.play()
            
        sound_timer = 0


        
    # Move
    
    player.move(pygame.key.get_pressed())
    power.move()
    energy.decrease_power()
    
    # Draw Screen
    
    screen.blit(background_img, (0, 0))
    player.draw()
    power.draw()
    screen.blit(score_text, (0, 0))
    energy.draw()
    
    # Check player state
    
    player.img_state()
    
    # If death change player death
    if energy.power < 0:
        player.state = "Bad"
        game_over_text = title_font.render("Game Over", True, (0, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - 170, HEIGHT // 2 - 100))
        lose_sound.play()
        
    # Clock Tick
    clock.tick(FPS)
    
    
    # Update
    
    pygame.display.update()
    
    
pygame.quit()
quit()