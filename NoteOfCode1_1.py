# import all libraries which are uses
import pygame
import sys
import math
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
field1 = (105, 166, 52)
field2 = (105, 176, 52)

pygame.init()

# Set the width and height of the screen [width, height]
size = (455, 440)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

# Creating Ponits
NewScore = 0
xNS = 1


# Creating Snake
# Head
class Snake():
    def __init__(self, image_pth):
        self.head = [82, 82]
        self.body = [[82, 82], [62, 82], [42, 82]]
        self.direction = "Right"
        self.image_pth = pygame.image.load(image_pth).convert()

    def move():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and goes_side != "Left":
                goes_side = "Right"
            elif event.key == pygame.K_LEFT and goes_side != "Right":
                goes_side = "Left"
            elif event.key == pygame.K_UP and goes_side != "Down":
                goes_side = "Up"
            elif event.key == pygame.K_DOWN and goes_side != "Up":
                goes_side = "Down"

    def hit_body():
        for hit in body:
            if hit[0] == head[0] and hit[1] == head[1]:
                print("You lose!")
                sys.exit()

    def logic_move():
        if goes_side == "Right":
            head[0] += 20
        if goes_side == "Left":
            head[0] -= 20
        if goes_side == "Up":
            head[1] -= 20
        if goes_side == "Down":
            head[1] += 20

    def field_snake():
        if head[0] > 402:
            head[0] -= 20
        if head[0] < 22:
            head[0] += 20
        if head[1] > 402:
            head[1] -= 20
        if head[1] < 22:
            head[1] += 20

    def animation():
        body.insert(0, list(head))
        body.pop()

    def draw_body():
        for segment in body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], 16, 16))


snake = Snake("pictures/Head/Head-right.png")
head = [82, 82]
# Start direction
goes_side = "Right"
# body
body = [[82, 82], [62, 82], [42, 82]]
segment = []


# Creating logic Body of snake
def animation():
    body.insert(0, list(head))
    body.pop()


# DELETED this code i wrote in Dreawing code DELETED
# def draw_snake():
#    for segment in body:
#        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1],16,16))

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

head_right = pygame.image.load('pictures/Head/Head-right.png').convert()
head_left = pygame.image.load('pictures/Head/Head-left.png').convert()
head_up = pygame.image.load('pictures/Head/Head-up.png').convert()
head_down = pygame.image.load('pictures/Head/Head-down.png').convert()

# Creating Food
food0 = (random.randrange(0, 20) * 20) + 20
food1 = (random.randrange(0, 20) * 20) + 20
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # Control of snake

            if event.key == pygame.K_ESCAPE:
                sys.exit()
    # --- Game logic should go here
    # Where snake looks, there snake goes

    # ---- logic of Clash head and body
    snake.hit_body()
    for food_spawn in body:
        if food_spawn[0] == food0 + 2 and food_spawn[1] == food1 + 2:
            food0 = (random.randrange(0, 20) * 20) + 20
            food1 = (random.randrange(0, 20) * 20) + 20
    # --- Screen-clearing code goes here

    # Here, we clear the screen to Black. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    # Floop of field where snake goes
    # Actually i don't know how it's to explain but if you
    # interesting in this, look at the code down below =)(meme)
    row1 = [0, 0]
    for row in range(20):
        row1[0] += 20
        row1[1] = 20
        h = row1[0] / 2
        for column in range(20):
            pygame.draw.rect(screen, field2, (row1[0], row1[1], 20, 20))
            if math.fmod(row, 2) == 0:
                pygame.draw.rect(screen, field1, (row1[0], row1[1], 20, 20))
            if math.fmod(column, 2) == 1:
                pygame.draw.rect(screen, field1, (row1[0], row1[1], 20, 20))
            if math.fmod(row, 2) == 0 and math.fmod(column, 2) == 1:
                pygame.draw.rect(screen, field2, (row1[0], row1[1], 20, 20))
            row1[1] += 20
    # Body trucking head
    animation()
    # Drawing Head of snake

    pygame.draw.rect(screen, GREEN, (head[0], head[1], 16, 16))
    # Drawing body of snake
    for segment in body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], 16, 16))
    # Drawing food
    pygame.draw.rect(screen, RED, (food0 + 2, food1 + 2, 16, 16))
    # Condition of eating food
    if food0 < head[0] < food0 + 20 and food1 < head[1] < food1 + 20:
        # Score + 1
        NewScore += 1
        print(NewScore)
        # Random food everytime when snake get food
        food0 = (random.randrange(0, 20) * 20) + 20
        food1 = (random.randrange(0, 20) * 20) + 20
        body.append(body[0])
        xNS += 1
        i = random.randrange(0, 14)
        # Score line
    pygame.draw.rect(screen, BLUE, (20, 425, xNS, 15))
    # if xNS get 100 points write "You win!" and exit the game
    if xNS > 100:
        print("You win!")
        sys.exit()

    if goes_side == "Right":
        screen.blit(head_right, (head[0], head[1]))
    if goes_side == "Left":
        screen.blit(head_left, (head[0], head[1]))
    if goes_side == "Up":
        screen.blit(head_up, (head[0], head[1]))
    if goes_side == "Down":
        screen.blit(head_down, (head[0], head[1]))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)

# Close the window and quit.
pygame.quit()