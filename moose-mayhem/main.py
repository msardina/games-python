import pygame
import math
from pygame import mixer
pygame.init()
mixer.init()



#music

music = pygame.mixer.Sound('sound/background_sfx.wav')
music.play(-1)

#assets
background = pygame.transform.scale(pygame.image.load('assets/background.png'), (900, 900))

#vars
start = True

#const
WIDTH, HEIGHT = background.get_width(), background.get_height()

#setup the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Moose Mayhem!')

#font
font = pygame.font.SysFont(None, 50)
title_font = pygame.font.SysFont(None, 100)

#game loop

title = title_font.render(f'Moose Mayhem', True, (0, 0, 0))
play = font.render(f'Press Enter to Play', True, (0, 0, 0))


while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
    #draw
    screen.blit(background, (0, 0))
    screen.blit(title, (WIDTH // 2 - (title.get_width() / 2), 100))
    screen.blit(play, (0, HEIGHT - 50))
    
    #move
    
    #exit
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RETURN]:
        start = False
        
    #update
    pygame.display.update()
    
#quit the game
pygame.quit()
quit()