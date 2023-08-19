import pygame
from pygame import mixer
import time
import random
pygame.font.init()

# Constants
WIDTH, HEIGHT = 1280, 720
BORDER_THICKNESS = 25
BOUNCING_RATE = -1
SHRINK_RATE = 0.8

# Variables
ball_size = 20
lenght_paddle = 150
score = 0
text_font = pygame.font.Font('freesansbold.ttf', 50)
game_over = text_font.render('Game Over', True, (255, 255, 255))
game_over_rect = game_over.get_rect()
game_over_rect.center = (WIDTH // 2, HEIGHT // 2)
double_ball = 1
two_balls = False

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong V1.0 - (C) MSfoundation productions ')
clock = pygame.time.Clock()
running = True

class Wall():
    def __init__(self, screen, color, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.screen = screen
        self.color = color
        self.width = width
        self.height = height
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
class Paddle():
    def __init__(self, x, y, width, height, color, screen):
        self.rect = pygame.Rect(x, y, width, height)
        self.height = height
        self.width = width
        self.color = color
        self.screen = screen
        self.state = 'idle'

    def draw(self, height):
        self.rect.height = height
        pygame.draw.rect(self.screen, self.color, self.rect)

    def move(self):
        if self.state == 'up' and self.rect.y > BORDER_THICKNESS:
            self.rect.y -= 10
        if self.state == 'down' and self.rect.y < HEIGHT - (lenght_paddle + BORDER_THICKNESS):
            self.rect.y += 10

    def change_state(self, state):
        self.state = state

    def moving_down(self):
        return self.state == 'down'
    def moving_up(self):
        return self.state == 'up'

class Ball():
    def __init__(self, screen, color, x, y, width, height, dx=0, dy=0):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.screen = screen
        self.dx = dx
        self.dy = dy
                
    def draw(self, width, height):
        self.rect = pygame.Rect(self.rect.x, self.rect.y, width, height)
        pygame.draw.rect(self.screen, self.color, self.rect)
    

        
    def move(self):
        self.rect.x += self.dx
        if self.rect.x < 0 or self.rect.x > WIDTH:
            self.rect.x -= self.dx
        self.rect.y += self.dy
        if self.rect.y < 0 or self.rect.y > HEIGHT:
            self.rect.y -= self.dy
            
            
        
        

# Create Objects
player1 = Paddle(20, (HEIGHT / 2) - (lenght_paddle / 2),
                 BORDER_THICKNESS, lenght_paddle, (255, 255, 255), screen)

wall_top = Wall(screen, (255, 255, 255), 0, 0, WIDTH, 25)
wall_right = Wall(screen, (255, 255, 255), WIDTH - 25, 0, 25, HEIGHT)
wall_bottom = Wall(screen, (255, 255, 255), 0, HEIGHT - 25, WIDTH, 25)
balls = [Ball(screen, (255, 255, 255), WIDTH / 2, HEIGHT / 2, ball_size, ball_size, dx=3, dy=3)]
# Main loop
while running:
    # Events
    for event in pygame.event.get():
        # X pressed?
        if event.type == pygame.QUIT:
            running = False

        # Check if a Key is pressed
        if event.type == pygame.KEYDOWN:
            # Up key pressed?
            if event.key == pygame.K_UP:
                player1.change_state('up')
            # Down key pressed?
            if event.key == pygame.K_DOWN:
                player1.change_state('down')

        # No key pressed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN and player1.moving_down():
                player1.change_state('idle')
            if event.key == pygame.K_UP and player1.moving_up():
                player1.change_state('idle')

    
    ##### MOVEMENT #####
    player1.move()
    for ball in balls:
        ball.move()

    ###### NOW WE DRAW THE SCENE ##
    screen.fill('black')
    player1.draw(lenght_paddle)
    
    # Is the ball out
    if ball.rect.x == 1:
        print('LOSE!')
        screen.blit(game_over, game_over_rect)
        time.sleep(4)
        running = False
    
    #Draw Balls
    
    for ball in balls:
        ball.draw(ball_size, ball_size)
            ##### Check Collision ########
        if pygame.Rect.colliderect(ball.rect, wall_bottom.rect) or pygame.Rect.colliderect(ball.rect, wall_top.rect):
            ball.dy = ball.dy * BOUNCING_RATE
            score += 1
            mixer.music.load('boing.wav')
            mixer.music.play()
        if pygame.Rect.colliderect(ball.rect, wall_right.rect):
            ball.dx = ball.dx * BOUNCING_RATE
            score += 1
            mixer.music.load('boing.wav')
            mixer.music.play()
        if pygame.Rect.colliderect(ball.rect, player1.rect):
            ball.dx = ball.dx * BOUNCING_RATE
            player1.rect.y += lost_length / 2
            lenght_paddle = lenght_paddle * SHRINK_RATE
            score += 1
            mixer.music.load('boing.wav')
            mixer.music.play()
        if random.randint(10, 10) == 10 and (ball.rect.x < (WIDTH / 2) + 10 and ball.rect.x > (WIDTH / 2) - 10) and len(balls) < 5:
            print('New Ball!')
            balls.append(Ball(screen, (255, 255, 255), balls[0].rect.x, random.randint(50, HEIGHT-50), ball_size, ball_size, dx=-3, dy=3))
        lost_length = lenght_paddle - (lenght_paddle * SHRINK_RATE)

    
    # Draw walls
    wall_top.draw()
    wall_right.draw()
    wall_bottom.draw()

    #n = ball.rect.y - ((ball.dy/ball.dx) * ball.rect.x)
    #y_col = (HEIGHT - 25)
    #x_col = (y_col - n) * (ball.dx/ball.dy)
    #pygame.draw.circle(screen, 'red', (x_col, y_col), 10)
    


    # Update
    pygame.display.flip()

    clock.tick(60)  # limit FPS to 60
print(f'score: {score}')
pygame.quit()
