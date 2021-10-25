#Example sprite class
#Nathan Rowbottom
#Working example of how to load a sprite and do some stuff

import pygame

class BasicSprite(pygame.sprite.Sprite):
  #This class represents the Player. It inherits from the "Sprite" class in Pygame. 
  
  #used to store the screen width and height

  def __init__(self, img):
    # Call the super class constructor
    
    super().__init__()
    #set the width and height of the screen
    self.WIDTH, self.HEIGHT = pygame.display.get_surface().get_size()

    self.image = img
    self.rect = img.get_rect()

    self.width = self.rect.width
    self.height = self.rect.height

    #we should probably move the coords over to center the image
    

  def setPosition(self, pos):
    self.rect.x  = pos[0] - self.width/2
    self.rect.y = pos[1] - self.height/2   

  #put all the game code in here
  def update(self):
    #added this line to allow me to put the update dunction in
    return True

  #given the screen, draw yourself
  def draw(self, screen):
    screen.blit(self.image, self.rect)

  #auto tries to get teh color key  
  def set_color_key(self):
    try:
      self.image.set_colorkey(self.image.color_at((0,0)))
    except pygame.error as e:
      print(e)
      return