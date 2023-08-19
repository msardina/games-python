import pygame
import os

FPS = 100
WIDTH, HEIGHT = 750, 750

GAME_NAME = "2012 - 1975"


# load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
#Player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# lasers
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
# player laser
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))
#BG
BG = pygame.image.load(os.path.join("assets", "background-black.png"))
BGS = pygame.transform.scale(BG, (WIDTH, HEIGHT))

POINT = pygame.image.load(os.path.join("assets", "point.png"))
