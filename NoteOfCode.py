import pygame
import sys
import math
import random


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
field1 = (105, 166, 52)
field2 = (105, 176, 52)

pygame.init()

# Set the width and height of the screen [width, height]
size = (740,740)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

font = pygame.font.Font(None, 40)
# Счётчик голов
Score = 0

# Creating Snake
snake = [82,82]
goes_side = "Right"
body = [[82,82],[62,82],[42,82]]

def animation():
    body.insert(0,list(snake))
    body.pop()
def draw_snake():
    for segment in body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1],16,16))

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Creating Food
food0 = (random.randrange(0,35)*20)+20
food1 = (random.randrange(0,35)*20)+20
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and goes_side != "Left":
                goes_side = "Right"
                #snake[0] += 20
            elif event.key == pygame.K_LEFT and goes_side != "Right":
                goes_side = "Left"
                #snake[0] -= 20
            elif event.key == pygame.K_UP and goes_side != "Down":
                goes_side = "Up"
                #snake[1] -= 20
            elif event.key == pygame.K_DOWN and goes_side != "Up":
                goes_side = "Down"
                #snake[1] += 20
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    # --- Game logic should go here
    if goes_side == "Right":
        snake[0] += 20
    if goes_side == "Left":
        snake[0] -= 20
    if goes_side == "Up":
        snake[1] -= 20
    if goes_side == "Down":
        snake[1] += 20

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
#    text = font.render(str(Score), True, BLUE)
    screen.fill(BLACK)
#    screen.blit(text, 0, 0)

    # --- Drawing code should go here
    row1 = [0,0]
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
            row1[1] += 20
    animation()
    pygame.draw.rect(screen, GREEN, (snake[0], snake[1], 16, 16))
    draw_snake()
    pygame.draw.rect(screen, RED, (food0+2, food1+2, 16, 16))
    if food0 < snake[0] < food0+20 and food1 < snake[1] < food1+20:
        Score += 1
        print(Score)
        food0 = (random.randrange(0,35)*20)+20
        food1 = (random.randrange(0,35)*20)+20
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)

# Close the window and quit.
pygame.quit()
