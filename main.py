import pygame
import sys

import src.config.constants as CONSTANTS

from src.background import Background
from src.fruit import Fruit
from src.snake import Snake
from src.collision import Collision
from src.score import Score


def main():
    pygame.init()
    screen = pygame.display.set_mode((CONSTANTS.WIDTH, CONSTANTS.HEIGHT))
    pygame.display.set_caption("Snake Game")

    background = Background(screen)
    fruit = Fruit(screen)
    snake = Snake(screen)
    collision = Collision()
    score = Score(screen)

    while True:
        background.draw()
        fruit.draw()
        snake.draw()
        score.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        if snake.direction != "DOWN":
                            snake.changeDir("UP")

                    case pygame.K_DOWN:
                        if snake.direction != "UP":
                            snake.changeDir("DOWN")

                    case pygame.K_RIGHT:
                        if snake.direction != "LEFT":
                            snake.changeDir("RIGHT")

                    case pygame.K_LEFT:
                        if snake.direction != "RIGHT":
                            snake.changeDir("LEFT")

                    case pygame.K_p:
                        snake.changeState("STOP")

        if collision.snakeHeadAndFruit(snake, fruit):
            snake.addTail()
            fruit.spawn()
            score.increase()

        if snake.state != "STOP":
            snake.move()

        if collision.snakeHeadAndSnakeTails(snake) or collision.snakeHeadAndWalls(snake):
            snake.die()
            score.reset()
            fruit.spawn()

        pygame.time.delay(120)
        pygame.display.update()


main()
