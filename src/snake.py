import pygame

import src.config.constants as CONSTANTS

middleBoardCoordinate = (CONSTANTS.SQUARES / 2 - 1) * CONSTANTS.PIXELS


class Snake:
    def __init__(self, surface):
        self.surface = surface
        self.direction = "RIGHT"
        self.state = "MOVING"
        self.head = {
            "x": middleBoardCoordinate,
            "y": middleBoardCoordinate
        }

    def move(self):
        if self.state == "STOP":
            return

        match self.direction:
            case "UP":
                self.head["y"] -= CONSTANTS.PIXELS

            case "DOWN":
                self.head["y"] += CONSTANTS.PIXELS

            case "RIGHT":
                self.head["x"] += CONSTANTS.PIXELS

            case "LEFT":
                self.head["x"] -= CONSTANTS.PIXELS

    def changeDir(self, direction):
        self.direction = direction

        if (self.state == "STOP"):
            self.changeState("MOVING")

    def changeState(self, state):
        self.state = state

    def draw(self):
        self.drawRect(self.head['x'], self.head['y'])
        self.drawTriangle(self.head['x'], self.head['y'], self.direction)

    def drawRect(self, x, y):
        pygame.draw.rect(self.surface, CONSTANTS.SNAKE_COLOR, (
            x, y, CONSTANTS.PIXELS, CONSTANTS.PIXELS
        ))

    def drawTriangle(self, x, y, direction):
        column = x / CONSTANTS.PIXELS
        row = y / CONSTANTS.PIXELS

        color = CONSTANTS.BG_SECONDARY if (row % 2 == 0 and column % 2 == 0) or (
            row % 2 != 0 and column % 2 != 0) else CONSTANTS.BG_PRIMARY

        middleVertexCoordinates = {
            "x": x + 0.5 * CONSTANTS.PIXELS,
            "y": y + 0.5 * CONSTANTS.PIXELS
        }

        match direction:
            case "UP":
                firstVertexCoordinates = {
                    "x": x,
                    "y": y
                }

                secondVertexCoordinates = {
                    "x": x + CONSTANTS.PIXELS,
                    "y": y
                }

            case "DOWN":
                firstVertexCoordinates = {
                    "x": x,
                    "y": y + CONSTANTS.PIXELS
                }

                secondVertexCoordinates = {
                    "x": x + CONSTANTS.PIXELS,
                    "y": y + CONSTANTS.PIXELS
                }

            case "LEFT":
                firstVertexCoordinates = {
                    "x": x,
                    "y": y
                }

                secondVertexCoordinates = {
                    "x": x,
                    "y": y + CONSTANTS.PIXELS
                }

            case "RIGHT":
                firstVertexCoordinates = {
                    "x": x + CONSTANTS.PIXELS,
                    "y": y
                }

                secondVertexCoordinates = {
                    "x": x + CONSTANTS.PIXELS,
                    "y": y + CONSTANTS.PIXELS
                }

        pygame.draw.polygon(
            self.surface, color,
            [
                [firstVertexCoordinates["x"], firstVertexCoordinates["y"]],
                [middleVertexCoordinates["x"], middleVertexCoordinates["y"]],
                [secondVertexCoordinates["x"], secondVertexCoordinates["y"]]
            ]
        )
