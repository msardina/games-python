# import useful packages
import pygame
import time
import os

# initialize pygame engine
SCREEN_WIDTH = 852
SCREEN_HEIGHT = 480
pygame.init()

# Concigure screen display
SCREEN = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
FPS = 27
pygame.display.set_caption('Mr.bold dude')

# TO REVIEW LATER
walkRight = [pygame.image.load(os.path.join('imgs', f'R{x}.png')) for x in range(1,10)]
walkLeft = [pygame.image.load(f'imgs/L{i}.png') for i in range(1, 10)]
bg = pygame.image.load(os.path.join('imgs', 'bg.jpg'))
idle = pygame.image.load(os.path.join('imgs', 'standing.png'))

class SpriteSheet():
    def __init__(self, file_name, cols, rows):
        self.sheet = pygame.image.load(file_name)
        self.cols = cols
        self.rows = rows
        self.rect = self.sheet.get_rect()
        self.cell_width = self.rect.width / self.cols
        self.cell_height = self.rect.height / self.rows
        self.number_cells = self.cols * self.rows
        self.cells = []

        for i in range(self.number_cells):
            x = (i % self.cols) * self.cell_width
            y = (i % self.rows) * self.cell_height

            self.cells.append((x, y, self.cell_width, self.cell_height))

class Player():
    def __init__(self, win, x, y, width, height, vel_x):
        self.win = win
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel_x = vel_x
        
        self.vel_y = 0
        self.is_jumping = False
        self.limit_y = y
        self.right = False
        self.left = False
        self.walk_count = 0


    def draw(self):
      
        if self.left:
            self.win.blit(walkLeft[self.walk_count // 3], (self.x, self.y))
        elif self.right:
            self.win.blit(walkRight[self.walk_count // 3], (self.x, self.y))
        else:
                self.win.blit(idle, (self.x, self.y))
            
        pygame.display.update()
        
    def act(self, keys):
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - self.width - self.vel_x:
            self.x += 5
            self.right = True
            self.left = False
            self.walk_count += 1
            if self.walk_count > 26:
                self.walk_count = 0
        if keys[pygame.K_LEFT] and self.x > self.vel_x:
            self.x -= 5
            self.left = True
            self.right = False
            self.walk_count += 1
            if self.walk_count > 26:
                self.walk_count = 0
            
        if keys[pygame.K_UP] and not self.is_jumping:
            self.is_jumping = True
            self.vel_y = -20

        if self.is_jumping:
            self.y += self.vel_y
            self.vel_y += 1

        if self.y > self.limit_y:
            self.is_jumping = False
            self.vel_y = 0
            self.y = self.limit_y
                


# Create player objects
prince = Player(SCREEN, 100, 415, 64, 64, 5)
prince2 = Player(SCREEN, 150, 415, 64, 64, 5)
prince3 = Player(SCREEN, 200, 415, 64, 64, 5)
prince4 = Player(SCREEN, 250, 415, 64, 64, 5)


game_running = True
clock = pygame.time.Clock()

# Main game loop
while game_running:
    clock.tick(FPS)

    list_of_events = pygame.event.get()
    
    # finish game if X was clicked
    for event in list_of_events:
        if event.type == pygame.QUIT:
            game_running = False

    keys = pygame.key.get_pressed()
    prince.act(keys)
    prince2.act(keys)
    prince3.act(keys)
    prince4.act(keys)

    # let's now draw the game
    SCREEN.blit(bg, (0, 0))
    prince.draw()
    prince2.draw()
    prince3.draw()
    prince4.draw()
    pygame.display.update()