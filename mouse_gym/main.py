
from cmath import sqrt
import pygame
import random
import math

# Define colors
WHITE = (255, 255, 255)
GREEN = (150, 255, 150)
RED = (255, 0, 0)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
BLUE = (50, 153, 213)
FULLGREEN = (0, 225 , 0)

# lists
colors = [WHITE, GREEN, RED, YELLOW, FULLGREEN, YELLOW, BLACK]

# vars
rx = 0
ry = 0
circle_on_screen = False
radius = 50
time_now = 0
time_start = 0
point = 0
old_points = 0
ball_pos = (rx, ry)
color = random.randint(0, len(colors)) # ball color first time



# Initialize the game
pygame.init()

# Create the window
SIZE = (960, 720)
WIDTH, HEIGHT = SIZE
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Mouse Gym")

FPS = 60
clock = pygame.time.Clock()

# defs

def calc_dis(pos1, pos2):
    a = abs(pos1[0] - pos2[0])**2
    b = abs(pos1[1] - pos2[1])**2

    return math.sqrt(a + b)


running = True
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if calc_dis(ball_pos, mouse_pos) < radius:
                # move circle randomly
                point += 1
                print(f'Your score: {point} Size of ball {radius}')
                rx = random.randint(radius, SIZE[0] - radius)
                ry = random.randint(radius, SIZE[1] - radius)
                ball_pos = (rx, ry)
                color = random.randint(0, len(colors))
            else:
                point -= 1
                radius += 1
                print(f'Your score: {point} Size of ball {radius}')

    SCREEN.fill(BLUE)
    
    time_now = pygame.time.get_ticks()
    if circle_on_screen:
        pygame.draw.circle(SCREEN, colors[color], (rx, ry), radius)
        if time_now - time_start > 2000:
            circle_on_screen = False
            time_start = pygame.time.get_ticks()
    else:
        if time_now - time_start > 1000:    # more than 2sec without circle
            rx = random.randint(radius, SIZE[0] - radius)
            ry = random.randint(radius, SIZE[1] - radius)
            ball_pos = (rx, ry)
            circle_on_screen = True
            time_start = pygame.time.get_ticks()
            
    if point == old_points + 10:
        radius -= 10
        point +=1
        old_points = point
        
    ###########################################
    # guarantee that the framerate is a steady FPS fps (unless things slow down.)
    clock.tick(FPS)

    # Go ahead and update the screen with what we've drawn.
    # pygame.display.flip() # will update everything
    # https://www.pygame.org/docs/ref/display.html#pygame.display.update
    pygame.display.update()

pygame.quit()
