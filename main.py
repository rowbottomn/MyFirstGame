import pygame
import random
#Let's import the Player class
from basic_sprite import BasicSprite
#from basic_sprite import BasicSprite
from enemy import Enemy
from player import Player
import utilities

p = utilities.p

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0 , 0 , 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)

pygame.init()
 
# Set the width and height of the screen [width, height]
WIDTH = 700
HEIGHT = 400
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Dodge Ball!")

#we should probably load all the images once and then ass them along
def load_img (url, width, height):
  image = pygame.image.load(url).convert_alpha()
  if (image.get_width() != width):
    #scale the image properly
    image = pygame.transform.scale(image, (width, height))


#contains all the sprites in the game.
all_sprites = pygame.sprite.Group() 

#contains all the enemies in the game
enemies_group = pygame.sprite.Group()

#contains the player
player_group = pygame.sprite.GroupSingle()

#contains bullets
#bullets = 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Game variables

SPEED = 5
numCircles = 10 
numEnemies = 10
#circle variables

enemies = []
circlesX = []#WIDTH/2
circlesY = []#0

circlesSp = []#5
circlesSize = []#25

#player variables

player_size = 50

player_img = load_img("star_gold.png", player_size, player_size)
#player = Player("star_gold.png", player_size, player_size)
player = Player(player_img)
player.setPosition([WIDTH/2,HEIGHT - 50]);
player.add(player_group)
player.add(all_sprites)

#intialize arrays for enemies
for i in range(numEnemies):
  #make the enemy 
  enemy = Enemy('ships.png', 40, 40)
  #add the enemy to the all sprites grout
  #enemies.append(enemy)
  enemy.add(all_sprites)
  #add the enemey to the all emnemies group 
  enemy.add(enemies_group)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        done = True

    #clear the screen
    screen.fill(WHITE)

    #update the sprite list 
    all_sprites.update()

    #get all the collisions with enemies
    enemy_collisions = pygame.sprite.spritecollide(player, enemies_group, True)

    for enemy in enemy_collisions:
      enemy.kill()

    #draw all the sprites
    #all_sprites.draw(screen)

    #below does the same thing for all the ships
    #for i in range(numCircles):

     # enemies[i].update()
        
      #Draw Stuff (circles)
     # enemies[i].draw(screen)
      #pygame.draw.circle(screen, MAGENTA, (circlesX[i], circlesY[i]), circlesSize[i])

    player_group.draw(screen)
    #player.draw(screen)
    # --- Render the screen.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(40)

    p("{}, {}".format(player.rect.x, player.rect.y))
 
# Close the window and quit.
pygame.quit()
