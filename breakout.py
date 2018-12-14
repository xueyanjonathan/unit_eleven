import pygame, sys
import brick
import paddle
from pygame.locals import *


def main():

    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH =  (APPLICATION_WIDTH - (BRICKS_PER_ROW -1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 8
    PADDLE_WIDTH = 60
    PADDLE_HEIGHT = 10
    RADIUS_OF_BALL = 10
    NUM_TURNS = 3

    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    colors = [CYAN, GREEN, YELLOW, ORANGE, RED]

    # Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
    # the screen (BRICK_Y_OFFSET)
    pygame.init()
    mainSurface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 32, 0)
    mainSurface.fill(WHITE)
    pygame.display.set_caption("Break Out")

    x = 0
    y = BRICK_Y_OFFSET
    bricks = 10
    for groups in range(5):
        color = colors.pop()
        for rows in range(2):
            for number in range(bricks):
                pile = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, color)
                pile.rect.x = x
                pile.rect.y = y
                mainSurface.blit(pile.image, pile.rect)
                x = x + BRICK_WIDTH + BRICK_SEP
            x = 0
            y = y + BRICK_HEIGHT + BRICK_SEP
    pygame.display.update()

    # Step 2: Create a paddle
    board = paddle.Paddle(mainSurface, BLACK, PADDLE_WIDTH, PADDLE_HEIGHT)
    pygame.display.update()
    board.rect.x = pygame.mouse.get_pos()
    board.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    mainSurface.blit(board.image, board.rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()

main()
