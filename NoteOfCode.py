import pygame
import sys
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
field1 = (22, 64, 54)
field2 = (85, 96, 32)


pygame.init()

# Set the width and height of the screen [width, height]
size = (460, 460)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")
x = 10
y = 10

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_RIGHT:
#            elif event.key == pygame.K_LEFT:
#            elif event.key == pygame.K_UP:
#            elif event.key == pygame.K_DOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    row1 = [0,0]
    floop = []
    for row in range(40):
        row1[0] += 10
        row1[1] = 10
        h = row1[0]/2
        for column in range(40):
            pygame.draw.rect(screen, field2,(row1[0],row1[1],10,10))
            if math.fmod(row, 2) == 0:
                pygame.draw.rect(screen, field1,(row1[0],row1[1],10,10))
            if math.fmod(column, 2) == 1:
                pygame.draw.rect(screen, field1,(row1[0],row1[1],10,10))
            if math.fmod(row, 2) == 0 and math.fmod(column, 2) == 1:
                pygame.draw.rect(screen, field2,(row1[0],row1[1],10,10))
            floop.append([row])
            row1[1] += 10

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
