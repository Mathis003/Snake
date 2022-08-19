from Configs import *

class Game:

    def __init__(self, screen, snake, score, FPS, apple):
        self.screen = screen
        self.snake = snake
        self.score = score
        self.apple = apple
        self.FPS = FPS
        self.clock = pygame.time.Clock()
        self.randomFoodOnce = True
        self.runningGame = True
        self.resetGameVariable = False

    def resetGame(self):
        self.score.addBestScore()
        self.screen.fill(BLACK)  # Fill the screen with black color
        self.snake.resetSnake()
        self.apple.resetApple()
        pygame.display.update()

    def Events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runningGame = False
                pygame.quit()
                quit()

            # Deal with the keyboard and the snake's direction
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and self.snake.head_pos[1] not in [HEIGHT, - SQUARE] and \
                        self.snake.dico_direction[self.snake.head_pos] != "LEFT":
                    self.snake.direction_play = "RIGHT"
                    self.snake.dico_direction[self.snake.head_pos] = "RIGHT"
                elif event.key == pygame.K_LEFT and self.snake.head_pos[1] not in [HEIGHT, - SQUARE] and \
                        self.snake.dico_direction[self.snake.head_pos] != "RIGHT":
                    self.snake.direction_play = "LEFT"
                    self.snake.dico_direction[self.snake.head_pos] = "LEFT"
                elif event.key == pygame.K_UP and self.snake.head_pos[0] not in [WIDTH, - SQUARE] and \
                        self.snake.dico_direction[self.snake.head_pos] != "DOWN":
                    self.snake.direction_play = "UP"
                    self.snake.dico_direction[self.snake.head_pos] = "UP"
                elif event.key == pygame.K_DOWN and self.snake.head_pos[0] not in [WIDTH, - SQUARE] and \
                        self.snake.dico_direction[self.snake.head_pos] != "UP":
                    self.snake.direction_play = "DOWN"
                    self.snake.dico_direction[self.snake.head_pos] = "DOWN"

    def run(self):
        while self.runningGame:

            self.clock.tick(self.FPS)

            # Events
            self.Events()

            # Snake movement
            self.snake.moveBody()
            if self.snake.checkCollision():
                self.resetGame()
                self.resetGameVariable = True

            if not self.resetGameVariable:
                self.snake.TeleportSnake()
                # Deal with the apple spawn and the 'eaten' mod
                if self.randomFoodOnce:
                    random_food_pos = self.apple.posRandomFood()
                    self.apple.position = random_food_pos
                    self.randomFoodOnce = False

                if self.snake.eatFood(self.apple.position):
                    self.randomFoodOnce = True

                # Update screen
                self.screen.fill(BLACK)  # Fill the screen with black color
                self.score.displayScore()
                self.apple.spawnFood()
                self.snake.drawSnake()
                pygame.display.update()

            self.resetGameVariable = False