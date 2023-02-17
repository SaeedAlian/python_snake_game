import pygame

import src.config.constants as CONSTANTS


class Score:
    def __init__(self, surface):
        self.surface = surface
        self.points = 0
        self.font = pygame.font.SysFont('monospace', 18, bold=False)

    def increase(self):
        self.points += 1

    def reset(self):
        self.points = 0

    def draw(self):
        lbl = self.font.render(
            'Score: ' + str(self.points), 1, CONSTANTS.TEXT_COLOR)
        self.surface.blit(lbl, (5, 5))
