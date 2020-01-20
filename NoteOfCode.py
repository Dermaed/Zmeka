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

# Creating Snake
# Head
class Snake():
    def __init__(self, image_pth):
        self.head = [82, 82]
        self.body = [[82, 82], [62, 82], [42, 82]]
        self.direction = "Right"
        self.image_pth = pygame.image.load(image_pth).convert()
        self.line_to_win = 1
        self.Score = 0
        self.done = False

    def draw_head(self):
        pygame.draw.rect(screen, GREEN, (self.head[0], self.head[1], 16, 16))

    def move(self):  #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and self.direction != "Left":
                    self.direction = "Right"
                elif event.key == pygame.K_LEFT and self.direction != "Right":
                    self.direction = "Left"
                elif event.key == pygame.K_UP and self.direction != "Down":
                    self.direction = "Up"
                elif event.key == pygame.K_DOWN and self.direction != "Up":
                    self.direction = "Down"
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()

    def hit_body(self):  #
        for hit in self.body:
            if hit[0] == self.head[0] and hit[1] == self.head[1]:
                print("You lose!")
                sys.exit()

    def logic_move(self):  #
        if self.direction == "Right":
            self.head[0] += 20
        if self.direction == "Left":
            self.head[0] -= 20
        if self.direction == "Up":
            self.head[1] -= 20
        if self.direction == "Down":
            self.head[1] += 20

    def field_snake(self):  #
        if self.head[0] > 402:
            self.head[0] -= 20
        if self.head[0] < 22:
            self.head[0] += 20
        if self.head[1] > 402:
            self.head[1] -= 20
        if self.head[1] < 22:
            self.head[1] += 20

    def sprites(self):
        if self.direction == "Right":
            screen.blit(head_right, (self.head[0], self.head[1]))
        if self.direction == "Left":
            screen.blit(head_left, (self.head[0], self.head[1]))
        if self.direction == "Up":
            screen.blit(head_up, (self.head[0], self.head[1]))
        if self.direction == "Down":
            screen.blit(head_down, (self.head[0], self.head[1]))

    def eating_food(self, food_x, food_y):
        if food_x < self.head[0] < food_x and food_y < self.head[1] < food_y + 20:
            # Score + 1
            self.Score += 1
            print(self.Score)
            # Random food everytime when snake get food
            food_x = (random.randrange(0, 20) * 20) + 20
            food_y = (random.randrange(0, 20) * 20) + 20
            self.body.append(self.body[0])
            self.line_to_win += 1

            # Score line



    def animation(self):  #
        self.body.insert(0, list(self.head))
        self.body.pop()

    def draw_body(self):  #
        segment = []
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], 16, 16))


class Food():
    def __init__(self, food_x, food_y):
        self.food_x = (random.randrange(0, 20) * 20) + 20
        self.food_y = (random.randrange(0, 20) * 20) + 20

    def excluding_snake_food(self, body):
        for food_spawn in body:
            if food_spawn[0] == self.food_x + 2 and food_spawn[1] == self.food_y + 2:
                self.food_x = (random.randrange(0, 20) * 20) + 20
                self.food_y = (random.randrange(0, 20) * 20) + 20

    def drawing_food(self):
        pygame.draw.rect(screen, RED, (self.food_x + 2, self.food_y + 2, 16, 16))

    def score_to_win(self, l_to_win):
        pygame.draw.rect(screen, BLUE, (20, 425,l_to_win , 15))
        # if xNS get 100 points write "You win!" and exit the game
        if l_to_win > 100:
            print("You win!")
            sys.exit()

snake = Snake("pictures/Head/Head-right.png")
food = Food((random.randrange(0, 20) * 20) + 20, (random.randrange(0, 20) * 20) + 20)
# head = [82, 82]
# Start direction
# goes_side = "Right"
# body
# body = [[82, 82], [62, 82], [42, 82]]
# segment = []


# Creating logic Body of snake
# def animation():
#   body.insert(0, list(head))
# body.pop()


# DELETED this code i wrote in Dreawing code DELETED
# def draw_snake():
#    for segment in body:
#        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1],16,16))

# Loop until the user clicks the close button.

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

head_right = pygame.image.load('pictures/Head/Head-right.png').convert()
head_left = pygame.image.load('pictures/Head/Head-left.png').convert()
head_up = pygame.image.load('pictures/Head/Head-up.png').convert()
head_down = pygame.image.load('pictures/Head/Head-down.png').convert()

# Creating Food
# food0 = (random.randrange(0, 20) * 20) + 20
# food1 = (random.randrange(0, 20) * 20) + 20
# -------- Main Program Loop -----------
while not snake.done:
    # --- Main event loop
    # Control of snake
    snake.move()

    # --- Game logic should go here
    # Where snake looks, there snake goes
    snake.logic_move()
    snake.field_snake()
    # ---- logic of Clash head and body
    snake.hit_body()
    food.excluding_snake_food(snake.body)
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
    snake.animation()
    # Drawing Head of snake
    snake.draw_head()
    # Drawing body of snake
    snake.draw_body()
    # Drawing food
    food.drawing_food()
    # Condition of eating food
    snake.eating_food(food.food_x, food.food_y)
    food.score_to_win(snake.line_to_win)

    snake.sprites()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)

# Close the window and quit.
pygame.quit()
