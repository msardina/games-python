from constants import *
import random

counter = 0

class Laser:
    def __init__(self, x, y, vel_x, vel_y,  img):
        self.x = x
        self.y = y
        self.img = img
        self.rect = pygame.Rect(self.x, self.y, self.get_width(), self.get_height())
        self.vel_y = vel_y
        self.vel_x = vel_x
        
    def get_width(self):
        return self.img.get_width()
    def get_height(self):
        return self.img.get_height()

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
        
    def move(self):
        self.y -= self.vel_y
        self.x += self.vel_x
        self.rect = pygame.Rect(self.x, self.y, self.get_width(), self.get_height())
        
    def off_screen(self, height):
        return self.y <= height and self.y >= 0

class Ship(pygame.sprite.Sprite):
    def __init__(self, x_initial, y_initial, vel_laser=0, health=100):
        self.x = x_initial
        self.y = y_initial
        self.health = health
        
        self.ship_img = None
        self.laser_img = None
        self.laser = []
        self.cool_down_counter = 0
        self.point_img = None
        self.laser_counter = 10
        self.rect = None

    def draw(self, window):
        """Draw the ship and its current lasers"""
        
        # draw ship img
        window.blit(self.ship_img, (self.x, self.y))
        if self.laser_counter > 0:
            self.laser_counter = self.laser_counter - 1
            #print(self.laser_counter)
        # Draw lasers of ship
        new_lasers = [] # lasers that are inside screen
        if not self.laser == []:
            for laser in self.laser:
                laser.move()
                if laser.y < HEIGHT and laser.y > 0:    # laser in screen?
                    laser.draw(window)
                    new_lasers.append(laser)
        # new lasers of ship
        self.laser = new_lasers
            
    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, x, y, health=100):
        # Initialize Class Ship(Player Dad)
        super().__init__(x, y, health)
        
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.vel = 5
        self.rect = pygame.Rect(self.x, self.y, self.get_width(), self.get_height())
    def act(self, keys):
        # Move player ship
        if keys[pygame.K_LEFT] and self.x - self.vel > 0:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x + self.vel + self.get_width() < WIDTH:
            self.x += self.vel
        if keys[pygame.K_UP] and self.y - self.vel > 0:
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y + self.vel + self.get_height() < HEIGHT:
            self.y += self.vel
            
        # updates hitbox coodinates
        self.rect = pygame.Rect(self.x, self.y, self.get_width(), self.get_height())

        # shoot a new laser
        if keys[pygame.K_SPACE]:
            if self.laser_counter == 0: # Are we ready to shoot?
                self.laser.append(Laser(self.x, self.y, 0, 10, self.laser_img))
                self.laser.append(Laser(self.x, self.y, 10, 10, self.laser_img))
                self.laser.append(Laser(self.x, self.y, -10, 10, self.laser_img))
                self.laser_counter = 20
                     

class Enemy(Ship):
    COLOR_MAP = {
        "red": (RED_SPACE_SHIP, RED_LASER),
        "green": (GREEN_SPACE_SHIP, GREEN_LASER),
        "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        pygame.mask.from_surface(self.ship_img)
        self.rect = pygame.Rect(self.x, self.y, self.get_width(), self.get_height())


    def move(self, vel):
        self.y += vel
        self.rect = pygame.Rect(self.x, self.y, self.get_width(), self.get_height())
        if self.y > 100:
            speed_of_enemyLaser = random.randint(-25, -5)
            if random.randint(0, 75) < 50:
                self.laser.append(Laser(self.x, self.y, 0, speed_of_enemyLaser, self.laser_img))

class Point(Ship):
    def __init__(self, x, y):
        super(). __init__(x, y)
        self.ship_img =  POINT
        
        pygame.mask.from_surface(self.ship_img)
        self.rect = pygame.Rect(self.x, self.y, self.get_width(), self.get_height())
        
    def move(self, vel):
        self.y += vel
        self.rect = pygame.Rect(self.x, self.y, self.get_width(), self.get_height())
        if self.y > HEIGHT:
            self.rect = None
            

        