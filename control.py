class Control():
    def __init__(self):
        self.done = False
        self.flag_side = "Right"
    def control(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.flag_side = "Right"
                elif event.key == pygame.K_LEFT:
                    self.flag_side = "Left"
                elif event.key == pygame.K_UP:
                    self.flag_side = "Up"
                elif event.key == pygame.K_DOWN:
                    self.flag_side = "Down"
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
