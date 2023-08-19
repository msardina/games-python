import pygame
SCREEN_WIDTH = 852
SCREEN_HEIGHT = 480
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = 27
pygame.display.set_caption('moving red cube')

class Player():
    def __init__(self, win, x, y, width, height):
        self.win = win
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(self.win, (250, 250, 250), (self.x, self.y), (self.width, self.height))




player1 =   Player(SCREEN, 0, 0, 64, 64)
play_game = True
while play_game:
    list_of_events = pygame.event.get()
    for event in list_of_events:
        if event.type == pygame.QUIT:
            play_game = False
    player1.draw()