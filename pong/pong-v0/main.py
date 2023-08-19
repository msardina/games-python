import pygame
from constant import SCREEN_HEIGHT, SCREEN_WIDTH, WHITE
from ball import Ball
from paddle import Paddle
from inputs import handle_input
from pygame.locals import *
from pygame import mixer
import time

print("Pong v 0.1")
#intro
print("Hello gamer, we are the pong committe.We made this committe FOR YOU. Please play our game to support me making games from the 80's .")

#Were the Game starts
TICK_RATE = 30
TOTAL_POINTS = 5

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Ping Pong with python!!!! by marcos (:")

clock = pygame.time.Clock()

# done means game finished
quit_game = False

ball = Ball()  # ball object created

paddle_left = Paddle()  # paddle object
paddle_right = Paddle()
paddle_right.rect.x = SCREEN_WIDTH - paddle_right.rect.width  # put paddle 2 in right side
score_left = 0
score_right = 0
game_round = 1

while not quit_game:
    clock.tick(TICK_RATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
    handle_input(paddle_right, paddle_left)

    screen.fill((0, 0, 0))  # draw backdrop

    # score_left
    font_score_left = pygame.font.SysFont(None, 100)
    img_score_left = font_score_left.render(str(score_left), True, WHITE)
    screen.blit(img_score_left, (30, 20)) \
        # score_right
    font_score_right = pygame.font.SysFont(None, 100)
    img_score_right = font_score_right.render(str(score_right), True, WHITE)
    screen.blit(img_score_right, (550, 20))

    ball.update(paddle_left, paddle_right)
    ball.draw(screen)  # draw the ball

    # has the ball gone out of bounds? If so, finish the game

    if ball.out_right or ball.out_left:
        if score_left < TOTAL_POINTS and score_right < TOTAL_POINTS:
            font = pygame.font.SysFont(None, 104)
            img = font.render("Round " + str(game_round) + " over", True, WHITE)
            screen.blit(img, (100, 200))
            time.sleep(1)
            game_round = game_round + 1

    # Draw paddles
    paddle_left.draw(screen)
    paddle_right.draw(screen)

    # flip screen and draw everything
    pygame.display.flip()

    # when ball is out of bounds
    if ball.out_right or ball.out_left:
        time.sleep(2)
        # add 1 to score_left
        if ball.out_right:
            score_left = score_left + 1
        # add 1 to score_right
        if ball.out_left:
            score_right = score_right + 1
        # setup evrything
        ball.setup()
        paddle_left.setup()
        paddle_right.setup()

    # game is over someone won!!
    if score_left == TOTAL_POINTS or score_right == TOTAL_POINTS:
        time.sleep(1)
        font_you_win = pygame.font.SysFont(None, 104)
        if score_left == TOTAL_POINTS:
            msg = 'player 1 wins'
            print('player 1 wins')
        else:
            msg = 'player 2 wins'
            print("player 2 wins")

        screen.fill((0, 0, 0))
        img_you_win = font_you_win.render(msg, True, WHITE)
        screen.blit(img_you_win, (100, 200))
        time.sleep(2)
        pygame.display.flip()
        time.sleep(2)
        quit_game = True

    # when left players score is == 5 then player left wins

pygame.quit()
