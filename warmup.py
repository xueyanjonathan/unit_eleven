import pygame, sys
from pygame.locals import *
import block


pygame.init()
main_window = pygame.display.set_mode((500, 500), 32, 0)
pygame.display.set_caption("Animation")

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
WIDTH = 25
HEIGHT = 25

my_block = block.Block(main_window, WIDTH, HEIGHT, BLUE)
my_block.rect.x = 10
my_block.rect.y = 10
main_window.blit(my_block.image, my_block.rect)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()

    main_window.fill(WHITE)
    my_block.rect.left += 3
    my_block.rect.top += 3
    main_window.blit(my_block.image, my_block.rect)
    pygame.display.update()

