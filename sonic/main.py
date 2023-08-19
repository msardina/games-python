import pygame
import sys
import math
import random

pygame.init
pygame.display.set_caption("The adventures of Tom Greenyberry")
clock = pygame.time.Clock()

WIDTH = 1200
HEIGHT = 800
GRAVITY = 1

# Define various colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the screen
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


# Create classes
class Sprite():
    def __init__(self, x, y, width, height, screen):
        # Center of sprite
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(int(self.x - self.width / 2.0), int(self.y - self.height / 2.0), self.width, self.height)

        # speed of sprite
        self.dx = 0
        self.dy = 0

        self.color = BLUE
        self.friction = 1

        self.screen = screen

    def goto(self, x, y):
        """Move sprite to a fixed location (x,y)
        """
        self.x = x
        self.y = y
        self.rect = pygame.Rect(int(self.x - self.width / 2.0), int(self.y - self.height / 2.0), self.width, self.height)

    def render(self):
        """Draw the Sprite
        """
        
        # draw the sprite
        pygame.draw.rect(self.screen, self.color, self.rect)

    def is_aabb_collision(self, other):
        #  do I collide with other?
        return self.rect.colliderect(other)

        # Axis Aligned Bounding Box
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)

class Player(Sprite):
    def __init__(self, x, y, width, height, screen):
        Sprite.__init__(self, x, y, width, height, screen) # initialize a sprite
        self.color = GREEN

    def move(self):
        self.goto(self.x + self.dx, self.y + self.dy)
        self.dx = self.dx * self.friction
        
        self.dy += GRAVITY
        if self.dx >= 1 and self.dx < 8:
            self.dx += 1
        if self.dx <= -1 and self.dx > -8:
            self.dx -= 1
            
    def jump(self):
        self.dy -= 24

    def left(self):
        self.dx = -1
        self.friction = 1

    def right(self):
        self.dx = 1
        self.friction = 1
        
    def collide(self, other : Sprite):
        if self.rect.colliderect(other):
            if self.y < other.y and self.x > other.x - other.width // 2 and self.x < other.x + other.width // 2: # Collide with top of other
                self.dy = 0 # Set vel y to 0
                self.goto(self.x, other.y - self.height // 2 - other.height // 2) # Make player.y be ontop of block
            elif self.y > other.y and self.x > other.x - other.width // 2 and self.x < other.x + other.width // 2: # Collide with bottom of other
                self.dy = 0
                self.goto(self.x, other.y + other.height // 2 + self.height // 2)
            elif self.x < other.x:
                self.dx = 0
                self.goto(other.x - other.width // 2 - self.width // 2, self.y)
            elif self.x > other.x:
                self.dx = 0
                self.goto(other.x + other.width // 2 + self.width // 2, self.y)
            return True
        else:
            return False  
        
# Create font

# Create Sounds

# Create game objects
player = Player(600, 0, 20, 40, SCREEN)
blocks = []
blocks.append(Sprite(600, 200, 400, 20, SCREEN)) 
blocks.append(Sprite(20, 600, 1000, 20, SCREEN))
blocks.append(Sprite(1180, 600, 1000, 20, SCREEN))
blocks.append(Sprite(600, 500, 500, 20, SCREEN))
blocks.append(Sprite(880, 450, 200, 20, SCREEN))

# Main game loop

while True:
    # go over all events that have happened in the frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # quit application
            sys.exit()
            
        # Keyboard Events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                player.jump()
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.friction = 0.8
            if event.key == pygame.K_LEFT:
                player.friction = 0.8

                

    # Move hte player
    player.move()

    # Border check the player
    if player.y > 800:
      player.goto(600, 0)
      player.dy = 0
      player.dx = 0

    # Check for player collisions with blocks
    for block in blocks:
        if player.collide(block):            
            # player.dx = player.dx*player.friction
            continue


    # Render (draw)
    # Fill the background
    SCREEN.fill(BLACK)

    # render objects
    player.render()
    for block in blocks:
        block.render()
    # flip the display
    pygame.display.flip()

    # Set the FPS
    clock.tick(30)
