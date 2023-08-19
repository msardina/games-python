import pygame

# Load images

# Classes
class Entity():
    def __init__(self, screen, x, y, width, height, image_file):
        self.rect = pygame.Rect(x, y, width, height)
        self.dx = 0
        self.dy = 0
        self.color = (250, 200, 152)
        self.screen = screen
        self.image = pygame.image.load(image_file)

    def draw(self):
        #pygame.draw.rect(slf.screen, self.color, self.rect)
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

class Enemy(Entity):
    def move_ai(self, aim):
        # Enemy Movement
        if self.rect.x > aim.rect.x:
            self.dx = -3
        if self.rect.x < aim.rect.x:
            self.dx = 3
        if self.rect.y > aim.rect.y:
            self.dy = -3
        if self.rect.y < aim.rect.y:
            self.dy = 3
            
class Snowman(Entity):
    pass
