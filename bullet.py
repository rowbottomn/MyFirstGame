#Bullet class!
#Nathan Rowbottom
#Just an example of an a bullet class

import pygame

from basic_sprite import BasicSprite

class Bullet(BasicSprite):

  #This class represents the Bullet. It inherits from the "Sprite" class in Pygame.   

  def __init__(self, img, player):
    global WIDTH, HEIGHT
    # Call the super class constructor
    super().__init__(img)
    WIDTH, HEIGHT = pygame.display.get_surface().get_size()

    self.rect.x = player.rect.x + player.rect.width/2 - self.rect.width/2
    self.rect.y = player.rect.y - self.rect.height/2
    self.speed = 15   

  #put all the game code in here
  def update(self):
    global WIDTH, HEIGHT
    #move the bullet
    self.rect.y -= self.speed
    #if its off the screen then remove it
    if (self.rect.y > HEIGHT):
      self.kill()
