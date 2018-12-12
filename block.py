import pygame


class Block:

    def __init__(self, screen, width, height, color):
        self.screen = screen
        self.width = width
        self.height = height
        self.color = color

        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.image.fill(self.color)
