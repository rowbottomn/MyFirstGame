import pygame
import random
#Let's import the Player class
from sprite_example import Player
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

#contains all the sprites in the game.
all_sprites_list = pygame.sprite.Group() 

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Game variables

SPEED = 5
numCircles = 10 
#circle variables
circlesX = []#WIDTH/2
circlesY = []#0

circlesSp = []#5
circlesSize = []#25

#player variables
playerX = WIDTH/2
playerY = HEIGHT - 50;
player_size = 50

player = Player(RED, player_size, player_size)

#intialize arrays for circles
for i in range(numCircles):
  circlesX.append(random.randint(0, WIDTH))
  circlesY.append(random.randint(-500, -100))
  circlesSp.append(SPEED)
  circlesSize.append(random.randint(15, 30))

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        done = True


    #clear the screen
    screen.fill(WHITE)

#update the player based on input
      #process the keys
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
      playerX += 5
    elif pressed[pygame.K_LEFT]:
      playerX -= 5

    #update the player sprite and shift it over center it
    player.rect.x = playerX - player.width/2
    player.rect.y = playerY - player.height/2

    #update the sprite list
    all_sprites_list.update()

    for i in range(numCircles):
      #Update stuff
      circlesY[i] += circlesSp[i] #move the circle down the screen
  
      #check stuff  
      #if off the screen  
      if circlesY[i] > HEIGHT + circlesSize[i]:
        circlesY[i] = -circlesSize[i]#move to the top
        circlesSp[i] = random.randint(SPEED-3, SPEED+3)
        circlesX[i] = random.randint(0, WIDTH)#random x location
      if (utilities.distance(playerX, playerY, circlesX[i],circlesY[i] )<= player_size+circlesSize[i]):
        #p("hit"+str(i))
        hello = 0
        
      #Draw Stuff (circles)
      
      pygame.draw.circle(screen, MAGENTA, (circlesX[i], circlesY[i]), circlesSize[i])

    pygame.draw.circle(screen, YELLOW, (playerX, playerY), player_size*0.2)
    #draw all the sprites
    #all_sprites_list.draw(screen)
    player.draw(screen)
    # --- Render the screen.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(40)

    p("{}, {}".format(player.rect.x, player.rect.y))
 
# Close the window and quit.
pygame.quit()