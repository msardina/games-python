import pygame

from constant import *

class Ball:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.radius = 10

        self.SPEED = 5
        self.vx = self.SPEED
        self.vy = self.SPEED

        self.out_left = False
        self.out_right = False
    
    def setup(self):
      self.x = SCREEN_WIDTH // 2
      self.y = SCREEN_HEIGHT // 2
      self.SPEED = 5
      self.vx = self.SPEED
      self.vy = self.SPEED
      self.out_left = False
      self.out_right = False

    def get_rect(self):
      return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def draw(self, screen):
      pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)

    def update(self, paddle_l, paddle_r):

      # Move the ball
      self.x += self.vx
      self.y += self.vy

      # if the ball touches border,  then we will bounce.
      if self.y > SCREEN_HEIGHT - self.radius * 2:    # bottom of screen
          self.vy *= -1
      if self.x > SCREEN_WIDTH - self.radius * 2:  # right side of screen
          self.vx *= -1
          self.out_right = True
      if self.x < self.radius * 2:  # left side of screen
          self.vx *= -1
          self.out_left = True
      if self.y < self.radius * 2:  # top side of screen
          self.vy *= -1

      # collide with both paddles
      if self.get_rect().colliderect(paddle_r.rect):  # collide with right paddle
          self.vx *= -1
          self.vx = self.vx - 1
          if self.vy > 0:  # increase the speed
            self.vy = self.vy + 1
            
          else:
            self.vy = self.vy - 1


      if self.get_rect().colliderect(paddle_l.rect):  # collide with left paddle
          self.vx *= -1
          self.vx = self.vx + 1
          if self.vy > 0:
            self.vy = self.vy + 1
           
          else:
            self.vy = self.vy - 1
