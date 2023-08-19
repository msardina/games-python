import pygame
from pygame import mixer


# Init
pygame.init()
mixer.init()
# Constants
WIDTH = 1200
HEIGHT = 800

# Variables
run = True

# Set up Screen

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('When Mr. Max watches a Bouncing Ball')

# Music

bounce = pygame.mixer.Sound('sound/Basketball Bounce.wav')
background = pygame.mixer.Sound('sound/background.wav')
background.play(-1)

# Imgs

court = pygame.image.load('assets/court.svg')

# Classes

class Ball:
    def __init__(self, x, y, radius, screen):
        self.x = x
        self.y = y
        self.radius = radius
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        self.speed = 0
        
    def draw(self):
        pygame.draw.circle(self.screen, (255, 165, 0), (self.x, self.y), self.radius, 0)
        
    def move(self):
        self.y += self.speed
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
        

class Floor:
    def __init__(self, x, y, width, height, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        pygame.draw.rect(self.screen, (190, 100, 0), self.rect)
        
# Create Objects
balls = []
#ball = Ball(WIDTH / 2, HEIGHT / 2, 50, screen)
floor = Floor(0, HEIGHT - 70, WIDTH, 70, screen)

while run:
    for event in pygame.event.get():
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            balls.append(Ball(pos[0], pos[1], 50, screen))
            
            
            
        if event.type == pygame.QUIT:
            run = False
            break
    # Draw Screen
    screen.fill((135, 206, 235))
    floor.draw()
    
    for ball in balls:

        # Move Screen
        ball.move()
        ball.speed += 0.010

        # Collisions

        collide = pygame.Rect.colliderect(ball.rect, floor.rect)

        if collide:
            ball.speed = -3
            bounce.play()

        ball.draw()



    
    # Update Screen
    pygame.display.flip()