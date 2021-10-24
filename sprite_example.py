#Example sprite class
#Nathan Rowbottom
#Working example of how to load a sprite and do some stuff

import pygame

WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
    
    #This class represents the Player. It inherits from the "Sprite" class in Pygame.
    
    #Color will be more important if you wanted a two player game; a Mario/Luigi type thing
    def __init__(self, color, width, height):
        # Call the super class constructor
        super().__init__()
        
        self.width = width
        self.height = height

# Pass in the color, and x and y position, width and height.
        if (False):#using this to debug a rectangle versus the picture
        
            #Set the image size
            self.image = pygame.Surface([width, height])
            self.color = color
            self.image.fill(WHITE)
            # Draw the player as a rectangle!
            pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        else:
            image = pygame.image.load("star_gold.png").convert_alpha()
            #scale the image
            self.image = pygame.transform.scale(image, (width, height))
            
        # Set the background color and set it to be transparent
        #only need this if your image has a background
        self.image.set_colorkey((255, 0 ,0))

        # Fetch the rectangle object that has the dimensions of the image 

        self.rect = self.image.get_rect()
        
    def draw(self, screen):
      screen.blit(self.image, self.rect)
      
  
      