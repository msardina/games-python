import pygame
from pygame import mixer
import time

from entities import Snowman, Enemy


# Constants
WIDTH, HEIGHT = 1900, 1000

# Variabless
running = True
#text_font = pygame.font.SysFont('Arial', 30)
# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snowmans Land')
clock = pygame.time.Clock()

# Background music
mixer.music.load('background.wav')
mixer.music.play(-1)


# Defenitions
def draw_text(text, font, text_col, x, y, screen):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))



# Objects
player = Snowman(screen, WIDTH / 2, HEIGHT / 2, 70, 70, 'snowman.png')
sun = Enemy(screen, 0, 0, 70, 70, 'sun.png')

# Main loop
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            # Player Movement
            if key[pygame.K_RIGHT]:
                player.dx = 5
            if key[pygame.K_LEFT]:
                player.dx = -5
            if key[pygame.K_UP]:
                player.dy = -5
            if key[pygame.K_DOWN]:
                player.dy = 5
            if not key[pygame.K_RIGHT] and not key[pygame.K_LEFT]:
                player.dx = 0
            if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
                player.dx = 0
            if not key[pygame.K_UP] and not key[pygame.K_DOWN]:
                player.dy = 0

    # Collisions
    collision = pygame.Rect.colliderect(player.rect, sun.rect)
    if collision:
        running = False
    # Move
    player.move()
    sun.move_ai(player)
    sun.move()
    
    # Draw scene
    screen.fill('light blue')
    player.draw()
    sun.draw()
    # Update
    pygame.display.flip()
    
    clock.tick(60)
mixer.music.load('lose.wav')
mixer.music.play(0)
#draw_text('You lose', (0, 0, 0), WIDTH / 2, HEIGHT / 2)
time.sleep(3)
pygame.quit()