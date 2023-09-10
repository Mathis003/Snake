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

    def resetGame(self):
        self.score.addBestScore()
        self.screen.fill(BLACK)
        self.snake.resetSnake()
        self.apple.resetApple_pos()
        pygame.display.update()

    def Events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runningGame = False
                self.score.addBestScore()
                pygame.quit()
                quit()

            # Deal with the keyboard and the snake's direction
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and self.snake.dico_direction[self.snake.head_pos] != "LEFT" and \
                        self.snake.head_pos[1] not in [HEIGHT, - SQUARE]:
                    self.snake.direction_play = "RIGHT"
                    self.snake.updateDicoDirection()
                elif event.key == pygame.K_LEFT and self.snake.dico_direction[self.snake.head_pos] != "RIGHT" and \
                        self.snake.head_pos[1] not in [HEIGHT, - SQUARE]:
                    self.snake.direction_play = "LEFT"
                    self.snake.updateDicoDirection()
                elif event.key == pygame.K_UP and self.snake.dico_direction[self.snake.head_pos] != "DOWN" and \
                        self.snake.head_pos[0] not in [WIDTH, - SQUARE]:
                    self.snake.direction_play = "UP"
                    self.snake.updateDicoDirection()
                elif event.key == pygame.K_DOWN and self.snake.dico_direction[self.snake.head_pos] != "UP" and \
                        self.snake.head_pos[0] not in [WIDTH, - SQUARE]:
                    self.snake.direction_play = "DOWN"
                    self.snake.updateDicoDirection()

    def run(self):

        self.snake.resetSnake()

        while self.runningGame:
            self.clock.tick(self.FPS)

            self.Events()

            # Snake movement
            self.snake.moveBody()

            if not self.snake.checkCollision():

                self.snake.TeleportSnake()

                # Deal with the apple spawn and the 'eaten' mod
                if self.randomFoodOnce:
                    random_food_pos = self.apple.posRandomFood()
                    self.apple.position = random_food_pos
                    self.randomFoodOnce = False

                if self.snake.eatFood(self.apple.position):
                    self.randomFoodOnce = True

                # Update screen
                self.screen.fill(BLACK)
                self.apple.spawnFood()
                self.snake.drawSnake()
                self.score.displayScore()
                pygame.display.update()
            else:
                self.resetGame()