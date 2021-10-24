#Enemy class
#Nathan Rowbottom
#Just an example of an basic enemy

import pygame
import random

from basic_sprite import BasicSprite

class Bullet(BasicSprite):

  #used to store the screen width and height
  WIDTH = 0
  HEIGHT = 0

  #This class represents the Player. It inherits from the "Sprite" class in Pygame.   

  def __init__(self, img, width, height):
    global WIDTH, HEIGHT
    # Call the super class constructor
    super().__init__(img, width, height)
    WIDTH, HEIGHT = pygame.display.get_surface().get_size()
    self.rect.x = random.randint(0, WIDTH) - width/2
    self.rect.y = random.randint(-500, -100) - height/2
    self.speed = 5
    
    #should have the rect formed
    

  #put all the game code in here
  def update(self):
    global WIDTH, HEIGHT
    self.rect.y += self.speed

    if (self.rect.y > HEIGHT + self.width/2):
      self.rect.y = random.randint(-500, -100)
      self.rect.x = random.randint(0, WIDTH)