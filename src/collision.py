import math

import src.config.constants as CONSTANTS


class Collision:
    def snakeHeadAndFruit(self, snake, fruit):
        return self.checkCollision({
            "x": snake.head["x"],
            "y": snake.head["y"],
        }, {
            "x": fruit.posX,
            "y": fruit.posY,
        })

    def snakeHeadAndWalls(self, snake):
        return snake.head["x"] > CONSTANTS.WIDTH - CONSTANTS.PIXELS or snake.head["x"] < 0 or snake.head["y"] > CONSTANTS.HEIGHT - CONSTANTS.PIXELS or snake.head["y"] < 0

    def snakeHeadAndSnakeTails(self, snake):
        for tail in snake.tails:
            if tail.isNew:
                continue

            if self.checkCollision({
                "x": snake.head["x"],
                "y": snake.head["y"],
            }, {
                "x": tail.x,
                "y": tail.y,
            }):
                return True

        return False

    def checkCollision(self, firstElement, secondElement):
        distance = math.sqrt(math.pow(
            (firstElement["x"] - secondElement["x"]), 2) + math.pow((firstElement["y"] - secondElement["y"]), 2))

        return distance < CONSTANTS.PIXELS
