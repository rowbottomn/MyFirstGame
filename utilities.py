import math
import pygame

DEBUG = True

def p(msg):
  global DEBUG
  if (DEBUG):
    print(msg)

#circular hit detection used early on, not really needed due ot pygaqme spritegroup functions
def distance(x1, y1, x2, y2):
  return math.sqrt((x2-x1)**2+(y2-y1)**2)

#we should probably load all the images once and then pass them along
def load_img (url, width, height):
  image = pygame.image.load(url).convert_alpha()
  if (image.get_width() != width):
    #scale the image properly
    image = pygame.transform.scale(image, (width, height))
  return image

#we should probably load all the images once and then pass them along
def load_imgs(url, width, height, offsetX, offsetY):
  image = pygame.image.load(url).convert_alpha()

  if (image.get_width() != width):
    #scale the image properly
    image = pygame.transform.scale(image, (width, height))
  return image