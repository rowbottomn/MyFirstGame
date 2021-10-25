#Enemy class
#Nathan Rowbottom
#Just an example of an basic enemy

import pygame
import random
import utilities

from basic_sprite import BasicSprite

class Enemy(BasicSprite):


  #This class represents the Player. It inherits from the "Sprite" class in Pygame.   

  def __init__(self, img):
    
    # Call the super class constructor
    super().__init__(img)

    self.rect.x = random.randint(0, self.WIDTH) - self.width/2
    self.rect.y = random.randint(-500, -100) - self.height/2
    self.speed = 5
    
    #should have the rect formed
    

  #put all the game code in here
  def update(self):
    
    self.rect.y += self.speed

    if (self.rect.y > self.HEIGHT + self.width/2):
      self.rect.y = random.randint(-500, -100)
      self.rect.x = random.randint(0, self.WIDTH)
    #utilities.p("enemy update")

  

