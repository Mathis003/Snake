from Game import *
from Snake import Snake
from Apple import Apple
from Score import Score

pygame.font.init()
pygame.init()

if __name__ == "__main__":

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")
    FPS = 25
    SIZE_ELEM = 28

    # Create the classes
    snake = Snake(screen, SIZE_ELEM)
    apple = Apple(screen, snake, SIZE_ELEM, RED)
    score = Score(screen, snake)

    game = Game(screen, snake, score, FPS, apple) # Create the game class
    game.run() # Run the game