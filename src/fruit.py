import pygame
import random
import os

import src.config.constants as CONSTANTS


fruitImgPath = os.path.join("assets", 'apple.png')


class Fruit:
    def __init__(self, surface):
        self.img = pygame.image.load(fruitImgPath)
        self.img = pygame.transform.scale(
            self.img, (CONSTANTS.PIXELS, CONSTANTS.PIXELS))

        self.surface = surface
        self.spawn()

    def spawn(self):
        self.posX = random.randrange(0, CONSTANTS.WIDTH, CONSTANTS.PIXELS)
        self.posY = random.randrange(0, CONSTANTS.HEIGHT, CONSTANTS.PIXELS)

    def draw(self):
        self.surface.blit(self.img, (self.posX, self.posY))
