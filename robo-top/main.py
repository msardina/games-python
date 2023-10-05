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
death_timer = 0
score = 0

# Music

background_music = pygame.mixer.Sound("sounds/background.wav")
robot_sound_1 = pygame.mixer.Sound("sounds/buzz whir.wav")
robot_sound_2 = pygame.mixer.Sound("sounds/QSNTNC1.wav")
robot_sound_3 = pygame.mixer.Sound("sounds/computer beeps1.wav")
robot_sound_4 = pygame.mixer.Sound("sounds/computer beeps2.wav")
robo_top_intro = pygame.mixer.Sound("sounds/robo-top-intro.wav")
collect = pygame.mixer.Sound("sounds/coin.wav")
lose_sound = pygame.mixer.Sound("sounds/lose.wav")
robo_top_intro.play()

#background_music.play(-1)

# Text Prep

score_text = font.render("Score: {score}", True, (0, 0, 0))
game_over_text = title_font.render("Game Over", True, (0, 0, 0))
power_text = font.render("Power:", True, (0, 0, 0))
turbo_text = font.render("Turbo:", True, (0, 0, 0))

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
        self.speed = 3
        
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
            self.x -= self.speed
            
        if keys[pygame.K_RIGHT] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN] and self.x < 831:
            self.x += self.speed
            
        if keys[pygame.K_UP] and not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and self.y > 0:
            self.y -= self.speed
            
        if keys[pygame.K_DOWN] and not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and self.y < HEIGHT - 130:
            self.y += self.speed
        
    def speed_check(self, turbo_on):
        
        if turbo_on:
            self.speed = 8
            
        else:
            self.speed = 3
            

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

class Bar:
    
    def __init__(self, x, y, power, height, start_width, turbo):
        self.x = x
        self.y = y
        self.power = power
        self.height = height
        self.width = self.power
        self.start_width = start_width
        self.color = (0, 255, 255)
        self.turbo = turbo
        
    def draw(self):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, 200, self.height))
        
        # Green
        if self.power > 150:
            self.color = (0, 255, 0)
            
        # Orange
        elif self.power > 50:
            self.color = (255, 165, 0)
            
        # Red
        else:
            self.color = (255, 0, 0)
            
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        
    def decrease_power(self):
        self.power -= 0.30
        self.width = self.power
    
    def increase_power(self):
        if self.power < 200:
            self.power += 0.30
            self.width = self.power
        
    def check_turbo(self, keys):
        if self.turbo == True:
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                if self.power > 1:
                    self.power -= 1
                    return True
            else:
                return False
# Objects

player = Robot(WIDTH / 2, HEIGHT / 2, robot_img, robot_img_death)
power = Power(0, 0, bolt_img)
energy = Bar((WIDTH - 220), HEIGHT - 30, 200, 20, 200, False)
turbo = Bar(100, HEIGHT - 30, 0, 20, 0, True)
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
        # Draw

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
    turbo.increase_power()
    
    # Draw Screen
    
    screen.blit(background_img, (0, 0))
    screen.blit(power_text, ((WIDTH - 350), HEIGHT - 40,))
    screen.blit(turbo_text, (0, HEIGHT - 40))
    player.draw()
    power.draw()
    screen.blit(score_text, (0, 0))
    energy.draw()
    turbo.draw()
    turbo.check_turbo(pygame.key.get_pressed())
    
    if turbo.check_turbo(pygame.key.get_pressed()) == True:
        player.speed_check(True)
    else:
        player.speed_check(False)
    
    # Check player state
    
    player.img_state()
    
    # If death change player death
    if energy.power <= 0:
        player.state = "Bad"
        game_over_text = title_font.render("Game Over", True, (0, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - 170, HEIGHT // 2 - 100))
        lose_sound.play()
        
        death_timer += 0.10
        
        if death_timer > 20:
            start_screen_def()
        
    # Clock Tick
    clock.tick(FPS)
    
    
    # Update
    
    pygame.display.update()
    
    
pygame.quit()
quit()