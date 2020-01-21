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
size = (440, 445)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")


# Creating Snake
class Snake():
    # Adding pictures for changing picture by direction
    def __init__(self, image_pth):
        # x, y position head of snake
        self.head = [82, 82]
        # mass of x and y position of all body of snake
        self.body = [[82, 82], [62, 82], [42, 82]]
        # direction where snake goes
        self.direction = "Right"
        # sprite of snake
        self.image_pth = pygame.image.load(image_pth).convert()
        # mass for adding new part of body in the future
        self.segment = []
        self.Score = 0
        # variable for main loop
        self.done = False
        # x pos for food
        self.food_x = (random.randrange(0, 20) * 20) + 20
        # y pos for food
        self.food_y = (random.randrange(0, 20) * 20) + 20
        # wide for Blue line of WIN
        self.line_to_win = 1
        # detector for food, it won't spawn in snake
        self.detector = []

    def draw_head(self):
        pygame.draw.rect(screen, GREEN, (self.head[0], self.head[1], 16, 16))

    # Control of head and by the way body
    def move(self):
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

    # detecting head and body crush
    def hit_body(self):
        for hit in self.body:
            if hit[0] == self.head[0] and hit[1] == self.head[1]:
                print("You lose!")
                sys.exit()

    # detecting that food won't spawn in body
    def exclusion_stucking_food(self):
        for self.detector in self.body:
            if self.detector[0] == self.food_x + 2 and self.detector[1] == self.food_y + 2:
                self.food_x = (random.randrange(0, 20) * 20) + 20
                self.food_y = (random.randrange(0, 20) * 20) + 20

    # That is logic how snake goes on a field
    def logic_move(self):
        if self.direction == "Right":
            self.head[0] += 20
        if self.direction == "Left":
            self.head[0] -= 20
        if self.direction == "Up":
            self.head[1] -= 20
        if self.direction == "Down":
            self.head[1] += 20

    # That is logic where snake can't go
    def field_snake(self):
        if self.head[0] > 402:
            self.head[0] -= 20
        if self.head[0] < 22:
            self.head[0] += 20
        if self.head[1] > 402:
            self.head[1] -= 20
        if self.head[1] < 22:
            self.head[1] += 20

    # Changing sprites on snake depending on direction
    def sprites(self):
        if self.direction == "Right":
            screen.blit(head_right, (self.head[0], self.head[1]))
        if self.direction == "Left":
            screen.blit(head_left, (self.head[0], self.head[1]))
        if self.direction == "Up":
            screen.blit(head_up, (self.head[0], self.head[1]))
        if self.direction == "Down":
            screen.blit(head_down, (self.head[0], self.head[1]))

    # Every time when snake "eat" food: Change positions of food, Score + 1 and blue line up, +one body block
    def eating_food(self):
        if self.food_x < self.head[0] < self.food_x + 20 and self.food_y < self.head[1] < self.food_y + 20:
            self.food_x = (random.randrange(0, 20) * 20) + 20
            self.food_y = (random.randrange(0, 20) * 20) + 20
            # Score + 1
            self.Score += 1
            print(self.Score)
            # Random food everytime when snake get food
            self.body.append(self.body[0])
            self.line_to_win += 1

    def drawing_food(self):
        pygame.draw.rect(screen, RED, (self.food_x + 2, self.food_y + 2, 16, 16))

    # Logic that snake follow the head
    def animation(self):
        self.body.insert(0, list(self.head))
        self.body.pop()

    def draw_body(self):
        self.segment = []
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], 16, 16))


snake = Snake("pictures/Head/Head-right.png")
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
head_right = pygame.image.load('pictures/Head/Head-right.png').convert()
head_left = pygame.image.load('pictures/Head/Head-left.png').convert()
head_up = pygame.image.load('pictures/Head/Head-up.png').convert()
head_down = pygame.image.load('pictures/Head/Head-down.png').convert()

# -------- Main Program Loop -----------
while not snake.done:
    # --- Main event loop and control
    snake.move()
    # --- Game logic should go here
    snake.logic_move()
    snake.field_snake()
    snake.hit_body()
    snake.exclusion_stucking_food()
    # --- Screen-clearing code goes here
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
    snake.drawing_food()
    snake.eating_food()
    # "LINE TO WIN"
    pygame.draw.rect(screen, BLUE, (20, 425, snake.line_to_win, 15))
    # That is check when score goes 100+ points
    if snake.line_to_win > 100:
        print("You win!")
        sys.exit()
    snake.sprites()

    pygame.display.flip()

    clock.tick(10)

pygame.quit()
