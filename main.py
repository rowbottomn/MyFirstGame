
import pygame
import random
 
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
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Game variables

#circle variables
circleX = WIDTH/2
circleY = 0

circleSp = 5
circleSize = 25

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    #clear the screen
    screen.fill(WHITE)

    #Update stuff
    circleY += circleSp #move the circle down the screen
 
    #check stuff  
    #if off the screen  
    if circleY > HEIGHT + circleSize:
      circleY = -circleSize#move to the top
      circleX = random.randint(0, WIDTH)#random x location

    #Draw Stuff
    pygame.draw.circle(screen, MAGENTA, (circleX, circleY), circleSize)

    # --- Render the screen.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()