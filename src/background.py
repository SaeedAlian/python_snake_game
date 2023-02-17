import pygame

import src.config.constants as CONSTANTS


class Background:
    def __init__(self, surface):
        self.surface = surface

    def draw(self):
        self.surface.fill(CONSTANTS.BG_PRIMARY)

        for row in range(CONSTANTS.SQUARES):
            for column in range(CONSTANTS.SQUARES):
                if (row % 2 == 0 and column % 2 == 0) or (row % 2 != 0 and column % 2 != 0):
                    pygame.draw.rect(
                        self.surface,
                        CONSTANTS.BG_SECONDARY,
                        (
                            column * CONSTANTS.PIXELS,
                            row * CONSTANTS.PIXELS,
                            CONSTANTS.PIXELS,
                            CONSTANTS.PIXELS
                        )
                    )
