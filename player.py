#Example sprite class
#Nathan Rowbottom
#Working example of how to load a sprite and do some stuff

import pygame
from basic_sprite import BasicSprite
from bullet import Bullet

class Player(BasicSprite):
    
  #This class represents the Player. It inherits from the "Sprite" class in Pygame.   


  def __init__(self, img, width, height):
    # Call the super class constructor
    super().__init__(img, width, height)
   
  def __init__(self, img):
    # Call the super class constructor
    super().__init__(img)


  #put all the game code in here
  def update(self):
    #update the player based on input
      #process the keys
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
      self.rect.x += 5
      
    elif pressed[pygame.K_LEFT]:
      self.rect.x -= 5
    
    if pressed[pygame.SPACE]:
      fire()
      
  def setPosition(self, pos):
    self.rect.x = pos[0] - self.width/2
    self.rect.y = pos[1] - self.height/2

  def fire():
    return Bullet()

  


 