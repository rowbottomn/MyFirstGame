#Example sprite class
#Nathan Rowbottom
#Working example of how to load a sprite and do some stuff

import pygame

class BasicSPrite(pygame.sprite.Sprite):
    
  #This class represents the Player. It inherits from the "Sprite" class in Pygame.   

  #Add instance variables here like maybe health or speed

  def __init__(self, img, width, height):
    # Call the super class constructor
    super().__init__()
    
    #setting instance variables to receive the values passed in the constructor call
    self.width = width
    self.height = height

    #load the image
    self.image = pygame.image.load(img).convert_alpha()
    #is the image the right size? I only check the width for speed's sake
    if (self.image.get_width() != width):
      #scale the image properly
      self.image = pygame.transform.scale(self.image, (width, height))
        
    # Set the background color and set it to be transparent
    #only need this if your image has a background
    #self.image.set_colorkey((255, 255 ,255))

    # Fetch the rectangle object that has the dimensions of the image 
    self.rect = self.image.get_rect()

  #put all the game code in here
  def update(self, pos, hit):
    #added this line to allow me to put the update dunction in
    return True


  def draw(self, screen):
    screen.blit(self.image, self.rect)
    