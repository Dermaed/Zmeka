import pygame
import sys
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (551, 551)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Zmeka")
# Шрифт
font = pygame.font.Font(None, 40)
# Счётчик еды
score = 0
def eating():
    body.append(head)
def animation():
    body.insert(0,list(head))
    body.pop()
def draw_snake(screen):
    for segment in body:
        pygame.draw.rect(screen, GREEN,pygame.Rect(segment[0], segment[1], 10, 10))

done = False
# Loop until the user clicks the close button.
head = [45, 45]
body = [[45,45],[34,45],[23,45]]

SSx = 11
SSy = 0
flag_side = "Right"

x = random.randrange(0, 551, 11)
y = random.randrange(0, 551, 11)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and flag_side != "Left":
                flag_side = "Right"
                SSx += 11
                SSy = 0
            elif event.key == pygame.K_LEFT and flag_side != "Right":
                flag_side = "Left"
                SSx -= 11
                SSy = 0
            elif event.key == pygame.K_UP and flag_side != "Down":
                flag_side = "Up"
                SSx = 0
                SSy -= 11
            elif event.key == pygame.K_DOWN and flag_side != "Up":
                flag_side = "Down"
                SSx = 0
                SSy += 11
            elif event.key == pygame.K_ESCAPE:
                sys.exit()

    # --- Game logic should go here

    text = font.render("Score: " + str(score), True, WHITE)

    if SSx > 11:
        SSx = 11
    if SSx < -11:
        SSx = -11
    head[0] = head[0] + SSx
    if SSy > 11:
        SSy = 11
    if SSy < -11:
        SSy = -11
    head[1] = head[1] + SSy

    if head[0] > 541:
        head[0] = 1
    if head[0] < 1:
        head[0] = 541
    if head[1] > 541:
        head[1] = 34
    if head[1] < 34:
        head[1] = 541

    if head[0] == x+1 and head[1] == y+1:
        score +=1
        x = random.randrange(0, 541, 11)
        y = random.randrange(33, 541, 11)
        head[0] += 11
        head[1] += 11
        eating()
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN,(head[0],head[1],10,10))
    pygame.draw.rect(screen, RED, (x+1, y+1, 10, 10))
    draw_snake(screen)
    animation()
    # --- Drawing code should go here
    screen.blit(text, [0,0])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(12)

# Close the window and quit.
pygame.quit()
