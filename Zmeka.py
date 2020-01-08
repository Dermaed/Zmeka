import pygame
import sys
import random
import math
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
field1 = (105, 166, 52)
field2 = (105, 176, 52)

pygame.init()

# Set the width and height of the screen [width, height]
size = (740,740)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Zmeka")

# Creating Snake
snake = [22,22]


done = False
# Loop until the user clicks the close button.

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake[0] += 20
            elif event.key == pygame.K_LEFT:
                snake[0] -= 20
            elif event.key == pygame.K_UP:
                snake[1] -= 20
            elif event.key == pygame.K_DOWN:
                snake[1] += 20
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    # --- Game logic should go here
    if snake[0] > 702:
        snake[0] -= 20
    if snake[0] < 22:
        snake[0] += 20
    if snake[1] > 702:
        snake[1] -= 20
    if snake[1] < 22:
        snake[1] += 20
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    row1 = [0,0]
    floop = []
    for row in range(35):
        row1[0] += 20
        row1[1] = 20
        h = row1[0]/2
        for column in range(35):
            pygame.draw.rect(screen, field2,(row1[0],row1[1],20,20))
            if math.fmod(row, 2) == 0:
                pygame.draw.rect(screen, field1,(row1[0],row1[1],20,20))
            if math.fmod(column, 2) == 1:
                pygame.draw.rect(screen, field1,(row1[0],row1[1],20,20))
            if math.fmod(row, 2) == 0 and math.fmod(column, 2) == 1:
                pygame.draw.rect(screen, field2,(row1[0],row1[1],20,20))
            floop.append([row])
            row1[1] += 20

    pygame.draw.rect(screen, GREEN, (snake[0], snake[1], 16, 16))
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(12)

# Close the window and quit.
pygame.quit()
