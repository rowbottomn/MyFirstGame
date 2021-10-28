#Explosion 
#Nathan Rowbottom
#I am using this to show how ot load images from a Spritesheet

from basic_sprite import BasicSprite

class Explosion(BasicSprite):

  #This class represents an explosion.

  def __init__(self, images, other):
        
    # Call the super class constructor
    super().__init__(images[0])
    self.images = images
    self.rect.x = other.rect.x + other.rect.width/2 - self.rect.width/2
    self.rect.y = other.rect.y
    self.duration = 40
    self.speed = int(self.duration/len(images))
    self.timer = 0
    
  #put all the game code in here
  def update(self):
    self.timer += 1
    frame = int(self.timer//self.speed)
    if frame >= len(self.images):
      self.kill()
      return
    else:
      self.rect.y += self.speed*0.5
      #print("{}".format(frame))
      self.image = self.images[frame]
    
    
