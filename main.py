from Configs import *
from Snake import Snake
from Apple import Apple
from Score import Score
from Game import Game

pygame.font.init()
pygame.init()

# Create the classes
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
snake = Snake(screen, 28, (0, 0), [(0, 0)], "RIGHT")
apple = Apple(screen, snake, 28, (SQUARE * (random.randint(0, WIDTH // SQUARE - 1)), SQUARE * (random.randint(0, HEIGHT // SQUARE - 1))), RED)
score = Score(screen, snake)
FPS = 25

if __name__ == "__main__":
    game = Game(screen, snake, score, FPS, apple) # Create the game class
    game.run() # Run the game