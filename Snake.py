from Configs import *

class Snake:

    def __init__(self, screen, size):
        self.screen = screen
        self.size = size
        self.length = 1 # The head doesn't count

        # Update directly by 'resetSnake()'
        self.head_pos = None
        self.body_pos = None
        self.direction_play = None # Direction of the head snake
        self.dico_direction = None # Dictionary with key : position of a square and value : direction of the snake at this position
        self.dico_rect = None # Dictionary with key : position of a square and value : rectangle of the square

    def resetSnake(self):
        self.length = 1
        self.head_pos = (0, 0)
        self.body_pos = [(0, 0)]
        self.direction_play = "RIGHT"
        self.dico_direction = {(0, 0): "RIGHT"}
        self.dico_rect = {(0, 0): pygame.Rect(0 + 1, 0 + 1, self.size, self.size)}

    def moveSquare(self, pos, direction):
        pos = list(pos)
        if direction == "UP":
            pos[1] -= SPEED
        elif direction == "DOWN":
            pos[1] += SPEED
        elif direction == "LEFT":
            pos[0] -= SPEED
        elif direction == "RIGHT":
            pos[0] += SPEED
        return tuple(pos)

    def moveBody(self):
        for i in range(self.length):
            if i == 0:
                self.head_pos = self.moveSquare(self.body_pos[0], self.dico_direction[self.body_pos[0]])
                self.body_pos[0] = self.head_pos
                self.updateDicoDirection()
            else:
                self.body_pos[i] = self.moveSquare(self.body_pos[i], self.dico_direction[self.body_pos[i]])

            self.updateDicoRect(self.body_pos[i])

    def addBody(self, new_body_pos):
        self.body_pos.append(new_body_pos)
        self.length += 1
        self.dico_direction[new_body_pos] = self.dico_direction[self.body_pos[-2]]
        self.dico_rect[new_body_pos] = pygame.Rect(new_body_pos[0] + 1, new_body_pos[1] + 1, self.size, self.size)

    def checkCollision(self):
        if self.length >= 5:
            for i in range(1, self.length):
                if self.dico_rect[self.head_pos].colliderect(self.dico_rect[self.body_pos[i]]):
                    return True
        return False

    def posNewBody(self, direction, body_pos):
        if direction == "UP":
            new_body_pos = (body_pos[0], body_pos[1] + SQUARE)
        elif direction == "DOWN":
            new_body_pos = (body_pos[0], body_pos[1] - SQUARE)
        elif direction == "LEFT":
            new_body_pos = (body_pos[0] + SQUARE, body_pos[1])
        elif direction == "RIGHT":
            new_body_pos = (body_pos[0] - SQUARE, body_pos[1])

        return new_body_pos

    def updateDicoDirection(self):
        self.dico_direction[self.head_pos] = self.direction_play

    def updateDicoRect(self, pos):
        self.dico_rect[pos] = pygame.Rect(pos[0] + 1, pos[1] + 1, self.size, self.size)

    def updateEatenMod(self):
        direction_last_body = self.dico_direction[self.body_pos[-1]]
        new_body_pos = self.posNewBody(direction_last_body, self.body_pos[-1])
        self.addBody(new_body_pos)

    def eatFood(self, food_pos):
        if self.head_pos == food_pos:
            self.updateEatenMod()
            return True
        return False

    def drawSquare(self, pos, color):
        pygame.draw.rect(self.screen, color, [pos[0] + 1, pos[1] + 1, self.size, self.size])

    def drawSnake(self):
        for pos in self.body_pos:
            self.drawSquare(pos, GREEN)

    def teleportation(self, pos, direction_pos_before):
        if pos[0] == - SQUARE and direction_pos_before == "LEFT":
            pos = (WIDTH, pos[1])
        elif pos[0] == WIDTH and direction_pos_before == "RIGHT":
            pos = (- SQUARE, pos[1])
        elif pos[1] == - SQUARE and direction_pos_before == "UP":
            pos = (pos[0], HEIGHT)
        elif pos[1] == HEIGHT and direction_pos_before == "DOWN":
            pos = (pos[0], - SQUARE)
        return pos

    def TeleportSnake(self):
        if self.length != 1:
            for i in range(self.length):
                direction_partSnake = self.dico_direction[self.body_pos[i]]
                self.body_pos[i] = self.teleportation(self.body_pos[i], direction_partSnake)
                if i == 0:
                    self.head_pos = self.body_pos[0]
                if self.body_pos[i] not in self.dico_direction:
                    self.dico_direction[self.body_pos[i]] = direction_partSnake
                self.updateDicoDirection()
                self.updateDicoRect(self.body_pos[i])
        else:
            direction_pos_before = self.dico_direction[self.body_pos[0]]
            self.body_pos[0] = self.teleportation(self.body_pos[0], direction_pos_before)
            self.head_pos = self.body_pos[0]
            self.updateDicoDirection()
            self.updateDicoRect(self.body_pos[0])
