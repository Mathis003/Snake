from src.Configs import *

class Score:

    def __init__(self, screen, snake):
        self.screen = screen
        self.snake = snake

    def readBestScore(self):
        try:
            with open("BestScore.txt", "r") as file:
                best_score = file.read()
                return best_score
        except:
            return "0"
    
    def writeBestScore(self, best_score):
        with open("BestScore.txt", "w") as file:
            file.write(str(best_score))
    
    def addBestScore(self):
        bestScore = self.readBestScore()
        new_score = self.snake.length - 1
        if int(bestScore) < new_score:
           self.writeBestScore(new_score)

    def displayScore(self):
        font = pygame.font.SysFont("comicsansms", 30)
        best_score = self.readBestScore()
        current_score = self.snake.length - 1
        textScore, textBestScore = font.render("Score: " + str(current_score), True, WHITE), font.render("Best Score: " + best_score, True, WHITE)
        self.screen.blit(textScore, [10, 0])
        self.screen.blit(textBestScore, [WIDTH - textBestScore.get_width() - 10, 0])