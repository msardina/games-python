import pygame
from constant import SCREEN_HEIGHT
PADDLE_HEIGHT = 99
PADDLE_WIDTH = 20
WHITE = (255, 255, 255)

class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(10, SCREEN_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.SPEED = 10
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)



    def move_up(self):
        if self.rect.y > 0:
            self.rect.y -= self.SPEED

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - PADDLE_HEIGHT:
            self.rect.y += self.SPEED

    def setup(self):
        self.rect.y = SCREEN_HEIGHT // 2
        