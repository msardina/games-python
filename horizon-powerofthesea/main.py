import pygame
import random
import time
from pygame import mixer
pygame.init()
mixer.init()

#imgs
start_screen_img = pygame.image.load('assets/title-screen.png')

#vars
clock = pygame.time.Clock()

#const
WIDTH, HEIGHT = start_screen_img.get_width(), start_screen_img.get_height()
FPS = 60

#font
title_font = pygame.font.SysFont(None, 100)
font = pygame.font.SysFont(None, 50)



#setup the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Horizon I || Power of the Sea')

def start_screen():

    start = True
    play = font.render(f'Press Enter to Play', True, (0, 0, 0))

    while start:
        #event loop
        for event in pygame.event.get():
            
            #check if X/QUIT pressed
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #draw
        screen.blit(start_screen_img, (0, 0))
        screen.blit(play, (0, HEIGHT - play.get_height()))
        
        #move
        
        #check if play pressed
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RETURN]:
            start = False
            
        #update
        clock.tick(FPS)
        pygame.display.update()


def game():
    run = True
    
    while run:
        
        #event loop
        for event in pygame.event.get():
            
            #check if X/QUIT pressed
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #draw
        screen.fill('sky blue')
        
        #move
        
        #key
        
        #update
        clock.tick(FPS)
        pygame.display.update()
        
    
#run program
if __name__ == '__main__':
    start_screen()
    game()