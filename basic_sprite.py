#Example sprite class
#Nathan Rowbottom
#Working example of how to load a sprite and do some stuff

import pygame

class BasicSprite(pygame.sprite.Sprite):
    
  #This class represents the Player. It inherits from the "Sprite" class in Pygame.   

  def __init__(self, data):
    # Call the super class constructor
    super().__init__()
    self.data = data

    #lets use the data to call different setup functions depending
    #setting instance variables to receive the values passed in the constructor call
    self.width = data.width
    self.height = data.height
   
    #load the image
    self.image = pygame.image.load(data.img).convert_alpha()
    #is the image the right size? I only check the width for speed's sake
    if (self.image.get_width() != width):
      #scale the image properly
      self.image = pygame.transform.scale(self.image, (width, height))
        
    # Set the background color and set it to be transparent
    #moved that to set_color_key() function

    # Fetch the rectangle object that has the dimensions of the image 
    self.rect = self.image.get_rect()

    def __init__(self, img):
      # Call the super class constructor
      super().__init__()

  #put all the game code in here
  def update(self):
    #added this line to allow me to put the update dunction in
    return True


  def draw(self, screen):
    screen.blit(self.image, self.rect)


  def set_color_key(self, color):
    self.color_key = color
    self.image.set_colorkey(color)