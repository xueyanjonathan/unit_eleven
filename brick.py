# Jonathan Lin
# 01/25/2019
# Create the bricks in the breakout game
import pygame


class Brick(pygame.sprite.Sprite):

    def __init__(self, width, height, color):
        # initialize sprite super class
        super().__init__()

        # finish setting the class variables to the parameters
        self.width = width
        self.height = height
        self.color = color

        # Put in the image for the brick
        self.image = pygame.image.load("kappa.png")

        # Get the rect coordinates
        self.rect = self.image.get_rect()
