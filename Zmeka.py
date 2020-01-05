import pygame
import sys
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Zmeka")
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

SSx = 0
SSy = 0
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
                SSx += 11
                SSy = 0
            elif event.key == pygame.K_LEFT:
                SSx -= 11
                SSy = 0
            elif event.key == pygame.K_UP:
                SSx = 0
                SSy -= 11
            elif event.key == pygame.K_DOWN:
                SSx = 0
                SSy += 11
            elif event.key == pygame.K_ESCAPE:
                sys.exit()

    # --- Game logic should go here
    head[0] = head[0] + SSx
    head[1] = head[1] + SSy
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN,(head[0],head[1],10,10))
    draw_snake(screen)
    animation()
    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(12)

# Close the window and quit.
pygame.quit()
