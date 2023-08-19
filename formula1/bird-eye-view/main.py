import pygame
import time
import math
from utils import scale_image, blit_rotate_center


GRASS = scale_image(pygame.image.load('imgs/grass.jpg'), 2.5)
TRACK = scale_image(pygame.image.load('imgs/track.png'), 0.9)

TRACK_BORDER = scale_image(pygame.image.load('imgs/track-border.png'), 0.9)
FINISH = pygame.image.load('imgs/finish.png')

FORMULA_1 = scale_image(pygame.image.load('imgs/car.png'), 0.55)
GREEN_CAR = scale_image(pygame.image.load('imgs/green-car.png'), 0.55)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Formula 1 Grand Prix')


FPS = 60

class AbstractCar:

    def __init__(self, max_vel, rotation_vel):
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.img = self.IMG
        self.x, self.y = self.START_POS
        self.accelaration = 0.05
        
    def roatate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel
            
    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)
    
    def move_forward(self):
        self.vel = min(self.vel + self.accelaration, self.max_vel)
        self.move()
        
    def move(self):
        # calculate vertical and horizontal shift of care based on angle and velocity
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel
        
        self.y -= vertical
        self.x -= horizontal
    
    def reduce_speed(self):
        self.vel = max(self.vel - self.accelaration / 2, 0)
        self.move()
        
class PlayerCar(AbstractCar):
    IMG = FORMULA_1
    START_POS = (180, 200)
        
run = True
clock = pygame.time.Clock()
images = [(GRASS, (0, 0)), (TRACK, (0, 0))]
player_car = PlayerCar(5, 4)

def draw(win, images, player_car):
    for img, pos in images:
        win.blit(img, pos)
        
    player_car.draw(win)
    pygame.display.update()

# Main Loop

while run:
    clock.tick(FPS)
    
    draw(WIN, images, player_car)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    keys = pygame.key.get_pressed()
    moved = False
    if keys[pygame.K_LEFT]:
        player_car.roatate(left=True)
        
    if keys[pygame.K_RIGHT]:
        player_car.roatate(right=True)
        
    if keys[pygame.K_UP]:
        moved = True
        player_car.move_forward()
        
    if not moved:
        player_car.reduce_speed()
        
pygame.quit()