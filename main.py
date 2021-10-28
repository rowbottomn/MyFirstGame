
import pygame
import random
#Let's import the Player class

from enemy import Enemy
from player import Player
from bullet import Bullet
from spritesheet import SpriteSheet
from explosion import Explosion

import utilities

#making local references to the utility functions
p = utilities.p
load_img = utilities.load_img
load_imgs = utilities.load_imgs

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
 

#contains all the sprites in the game.
all_sprites = pygame.sprite.Group() 

#contains all the enemies in the game
enemies_group = pygame.sprite.Group()

#contains the player
player_group = pygame.sprite.GroupSingle()

#contains bullets
bullets = pygame.sprite.Group()
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

#player variables
player_size = 50

#to make it easier to understand I am going to load the images first and then pass them in corrected to the appropriate size.
player_img = load_img("assets/images/ships.png", player_size, player_size)

player = Player(player_img)
player.setPosition([WIDTH/2, HEIGHT - 50]);
player.add(player_group)
player.add(all_sprites)

#intialize arrays for enemies
enemy_img = load_img("assets/images/enemy.png", 40, 40)
bullet_img = load_img("assets/images/star_gold.png", 15, 15)

#using an array to load all the enemies   
for i in range(numEnemies):
  #make the enemy 
  enemy = Enemy(enemy_img)
  #add the enemy to the all sprites grout
  #enemies.append(enemy)
  enemy.add(all_sprites)
  #add the enemey to the all emnemies group 
  enemy.add(enemies_group)

#load up the explosion images
explosion_images = SpriteSheet('assets/images/explosions.png', (60, 60), (4, 4)).images

blast = pygame.mixer.Sound('assets/sounds/blast.wav')
#sound = audio.play_file('assets/sounds/blast.wav')

p('set up cpompleted')
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

    if (player.firing):
      bullet = Bullet(bullet_img, player);
      bullet.add(bullets)
      bullet.add(all_sprites)
      player.firing = False;

    #get all the collisions with enemies
    enemy_collisions = pygame.sprite.groupcollide(enemies_group,bullets, False, True, None)
    
    for enemy in enemy_collisions:
      explosion = Explosion(explosion_images, enemy)
      explosion.add(all_sprites)
      blast.play()

      enemy.kill()

    #draw all the sprites
    all_sprites.draw(screen)

    #below does the same thing for all the ships
    #for i in range(numCircles):

     # enemies[i].update()
        
      #Draw Stuff (circles)
     # enemies[i].draw(screen)
      #pygame.draw.circle(screen, MAGENTA, (circlesX[i], circlesY[i]), circlesSize[i])

    #player_group.draw(screen)
    #player.draw(screen)
    # --- Render the screen.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

    #p("{}, {}".format(player.rect.x, player.rect.y))
 
# Close the window and quit.
pygame.quit()

