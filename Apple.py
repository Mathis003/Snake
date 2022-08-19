from Configs import *

class Apple:

    def __init__(self, screen, snake, size, position, color):
        self.screen = screen
        self.snake = snake
        self.size = size
        self.position = position
        self.color = color

    def resetApple(self):
        self.position = self.posRandomFood()

    def posRandomFood(self):
        while True:
            i = random.randint(0, WIDTH // SQUARE - 1)
            j = random.randint(0, HEIGHT // SQUARE - 1)
            pos = (i * SQUARE, j * SQUARE)
            if not self.checkAppleOnSnake(pos):
                return pos

    def checkAppleOnSnake(self, pos):
        if pos in self.snake.body_pos:
            return True
        return False

    def spawnFood(self):
        pygame.draw.rect(self.screen, RED, [self.position[0] + 1, self.position[1] + 1, self.size, self.size])