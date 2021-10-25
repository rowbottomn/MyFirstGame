#Example sprite class
#Nathan Rowbottom
#A basic Player class

import pygame
from basic_sprite import BasicSprite
#from bullet import Bullet

class Player(BasicSprite):
    
  #This class represents the Player. It inherits from the "BasicSprite" class I made.   

  def __init__(self, img):
    # Call the super class constructor
    super().__init__(img)
    self.image = pygame.transform.flip( self.image, False, True)
    self.fire_timer = 40
    self.firing = False

  #put all the game code in here
  def update(self):
    self.fire_timer-=1
    #update the player based on input
      #process the keys
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
      self.rect.x += 5
      
    elif pressed[pygame.K_LEFT]:
      self.rect.x -= 5
    
    if pressed[pygame.K_SPACE]:
      if(self.fire_timer < 0):
        self.fire_timer = 30
        self.fire()
    
    #prevent the player from leaving the screen
    if (self.rect.x < 0):
      self.rect.x = 0
    elif (self.rect.x > self.WIDTH-self.rect.width):
      self.rect.x = self.WIDTH-self.rect.width

  #set the bulletgroup
  def setBullets(self,bullets):
    self.bullets = bullets

  def fire(self):
    self.firing = True
    
  
  


 