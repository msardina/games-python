
import pygame
import random
from Ships import Player, Enemy, Point
from constants import *
pygame.font.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_NAME)

print(GAME_NAME)



def main():
    """This is the main function of the game
    """
    
    playing = True  # game is still playing/running
    lost_count = 0  # 
    level = 0
    lives = 10
    player = Player(300, 650)   # create player object of class Player
    point = Point(random.randint(0, WIDTH), -500)
    enemies = []    # use to store all the Enemy objects
    wave_length = 40 # n o of enemies attaching in a single wave
    enemy_vel = 1   # velocity of enemies

    def redraw_window():
        SCREEN.blit(BGS, (0, 0))
        #draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

        SCREEN.blit(lives_label, (10, 10))
        SCREEN.blit(level_label, (WIDTH - level_label.get_width() -10, 10))

        player.draw(SCREEN)
        
        if not point == None:
            point.draw(SCREEN)
            point.move(1)
        for enemy in enemies:
            enemy.draw(SCREEN)

        if lives <= 0:
            lost_text = lost_font.render("Game over", 1, (255, 255, 255))
            SCREEN.blit(lost_text, (WIDTH // 2 - lost_text.get_width() // 2, HEIGHT // 2))



        pygame.display.update()

    # pygame clock to control speed of game
    clock = pygame.time.Clock()

    #point = Point(random.randint(0, WIDTH - 100), HEIGHT - 1500)
    # define font types
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 70)
    
    
    # main game loop starts here
    while playing:
        clock.tick(FPS) # set FPS to get right speed independent of machine

            
        # when all enemies are killed, start a new level
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            point = Point(random.randint(0, WIDTH), -500)
            # make a new wave by filling the list enemies with new Enemy objects (random loc + color)
            for i in range(wave_length):
                x = random.randrange(50, WIDTH - 100)
                y = random.randrange(-1500, -100)
                color = random.choice(["red", "green", "blue"])
                enemy = Enemy(x, y, color) # create an enemy object and add it to the list
                enemies.append(enemy)

        # check if user has closed window; if so, terminate the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

        # collect all keys that have been pressed
        keys = pygame.key.get_pressed()

        # make player act depending on which keys were pressed
        player.act(keys)

        # make enemys move and update no of lives
        for enemy in enemies.copy():    # process each enemy in the list enemies
            # move the enemy
            enemy_killed = False
            enemy.move(enemy_vel)   
            if enemy.y > HEIGHT:    # enemy has gone to the bottom, 1 live lesss
                enemy_killed = True
                lives = lives - 1
            
            if pygame.sprite.collide_rect(player, enemy):
                lives -= 1
                enemy_killed = True
            
            # enemy was hit and killed
            if not player.laser == []:  # is there any player's laser around?
                new_lasers = []
                for laser in player.laser:
                    if pygame.sprite.collide_rect(laser, enemy):
                        enemy_killed = True
                    else:
                        new_lasers.append(laser)
                    
                player.laser = new_lasers
            # ship has been hit by enemy laster
            if not enemy.laser is []:
                new_lasers = []
                for laser in enemy.laser:
                    if pygame.sprite.collide_rect(laser, player):
                        lives -= 1
                        new_lasers.append(laser)
                enemy.laser = new_lasers
                        
            if enemy_killed == True:
                enemies.remove(enemy)

        # check if Player hit point star
        if not point is None:
            if pygame.sprite.collide_rect(point, player):
                point = None
                lives += 3

        # did I lose?
        if lives <= 0:
            lives = 0
            lost_count += 1
            if lost_count > FPS * 3:
                playing = False


        redraw_window()


# call main program
main()
