from Configs import *

class Score:

    def __init__(self, screen, snake):
        self.screen = screen
        self.snake = snake

    def readBestScore(self):
        with open("BestScore.txt", "r") as file:
            best_score = file.read()
            return best_score

    def displayScore(self):
        font = pygame.font.SysFont("comicsansms", 30)
        best_score = self.readBestScore()
        textScore, textBestScore = font.render("Score: " + str(self.snake.body_pos.__len__() - 1), True, WHITE), font.render("Best Score: " + best_score, True, WHITE)
        # Display the score/best score on the screen
        self.screen.blit(textScore, [10, 0])
        self.screen.blit(textBestScore, [WIDTH - textBestScore.get_width() - 10, 0])

    def addBestScore(self):
        bestScore = self.readBestScore()
        if int(bestScore) < self.snake.body_pos.__len__() - 1:
            with open("BestScore.txt", "w") as file:
                file.write(str(self.snake.body_pos.__len__() - 1))