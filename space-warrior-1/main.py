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
loss = False
lives = 3
boss_fight = False
oxygen = 100
game_over = False
speed_of_screen = 5

# imgs
alien_img = pygame.image.load('assets/alien.png')
player_img = pygame.image.load('assets/spaceman.png')
level_img = pygame.transform.scale(pygame.image.load('assets/level.png'), (10000, 1300))
one_life_img = pygame.image.load('assets/1 lives.png')
two_life_img = pygame.image.load('assets/2 lives.png')
three_life_img = pygame.image.load('assets/3 lives.png')
air_img = pygame.image.load('assets/air.png')
game_over_screen = pygame.image.load('assets/game over.png')
star_img = pygame.image.load('assets/star.png')
black_hole_img = pygame.image.load('assets/black hole.png')

# sounds

backround_msc = pygame.mixer.Sound('sound/background.wav')
collect_sfx = pygame.mixer.Sound('sound/collect.wav')
lose_sfx = pygame.mixer.Sound('sound/lose.wav')
#no_air = pygame.mixer.Sound('sound/no air.wav')
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
            if player.y > 40:
                self.dy -= 0.75
        if keys[pygame.K_DOWN]:
            if player.y < (HEIGHT - player.height) - 40:
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
            print(obstacle)
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
        pygame.draw.rect(screen, (0, 0, 0), self.rect)
    def move(self, speed_of_screen):
        self.x -= speed_of_screen
        
        if self.x < self.width * -1:
            self.x = (WIDTH * 2) + random.randint(-50, 50)
            self.y = random.randint(0, HEIGHT)
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
class Lives:
    
    def __init__(self, x, y, imgs):
        self.x = x
        self.y = y
        self.imgs = imgs
        
    def draw(self, lives, dead):
        if not dead:
            lives = lives - 1
        screen.blit(self.imgs[lives], (self.x, self.y))
class Bar:
    
    def __init__(self, x, y, power, height, start_width):
        self.x = x
        self.y = y
        self.power = power
        self.height = height
        self.width = self.power
        self.start_width = start_width
        self.color = (0, 255, 255)
        
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
        self.power -= 0.45
        self.width = self.power
    
    def increase_power(self):
        if self.power < 200:
            self.power += 0.30
            self.width = self.power
            
            
class Oxygen:
    
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
        self.x -= 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def collected(self, player_rect):
        collide = pygame.Rect.colliderect(self.rect, player_rect)
        
        if collide:
            self.x = WIDTH * 2
            self.y = random.randint(0, HEIGHT)
            return True
# objects

player = Player(100, HEIGHT // 2, player_img)
alien = Obstacle(WIDTH // 2, HEIGHT // 2, alien_img)
alien2 = Obstacle(1000, random.randint(0, HEIGHT), alien_img)
evil_star = Obstacle(WIDTH - 50, random.randint(0, HEIGHT), star_img)
black_hole = Obstacle(WIDTH + 100, random.randint(0, HEIGHT), black_hole_img)
obstacles = [alien, alien2]
level = ScrollingSurface(0, 0, level_img)
hearts = Lives(10, 10, [one_life_img, two_life_img, three_life_img])
oxygen_bar = Bar(300, 30, 200, 30, 200)
air = Oxygen(WIDTH, random.randint(0, HEIGHT), air_img)

# main loop

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # draw screen
    level.draw()
    player.draw()
    if len(obstacles) > 0:
        for obstacle in obstacles:
            obstacle.draw()
    hearts.draw(lives, loss)

    if boss_fight == False:
        air.draw()
        oxygen_bar.draw()
    
    # move screen
    player.move(pygame.key.get_pressed(), 4)
    alien.move(speed_of_screen)
    alien2.move(speed_of_screen)
    black_hole.move(speed_of_screen)
    evil_star.move(speed_of_screen)
    if boss_fight == False:
        air.move()
    
    if air.x < air.width * -1:
        air.x = WIDTH * 2
        air.y = random.randint(0, HEIGHT)
        
    if level.x < -8500:
        boss_fight = True
        level.move(0, 0)
    elif player.x > WIDTH - 400:
        level.move(-10, 0)
        speed_of_screen = 10
    elif player.x < 200:
        level.move(-3, 0)
        speed_of_screen = 3
    else:
        level.move(-5, 0)
        speed_of_screen = 5

    # clear screen boss fight
    
    if boss_fight:
        obstacles = []
        
    # lose oxygen
    
    if boss_fight == False:
        oxygen_bar.decrease_power()
    else:
        oxygen_bar.power = 200
        oxygen_bar.draw()
        
    # collision
    print(len(obstacles))
    if len(obstacles) > 0:
        if player.collision(obstacles)[0] == alien.rect and player.collision(obstacles)[1] == True:
            print('colide')
            lives -= 1
            player.x = 100
            player.y = HEIGHT // 2
            if lives == 0:
                loss = True

    air.collected(player.rect)
    
    if air.collected(player.rect):
        oxygen_bar.power = 200
        collect_sfx.play()
        
    if oxygen_bar.power < 0:
        loss = True
        
    # end game
    
    if loss == True:
        run = False
        
        
    # update screen
    clock.tick(FPS)
    pygame.display.update()

if loss == True:
    game_over = True
    lose_sfx.play()
    
while game_over:
    backround_msc.stop()

    # Draw
    screen.fill('black')
    screen.blit(game_over_screen, (0, 0))
    
    # Update
    
    pygame.display.update()
    
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
# quit game
pygame.quit()
quit()