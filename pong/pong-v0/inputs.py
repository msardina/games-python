import pygame
from pygame.locals import *


def handle_input(paddle1, paddle2):
    pygame.event.pump()
    keys = pygame.key.get_pressed()

    if keys[K_UP]:
        paddle1.move_up()
    elif keys[K_DOWN]:
        paddle1.move_down()

    if keys[K_w]:
        paddle2.move_up()
    elif keys[K_s]:
        paddle2.move_down()
