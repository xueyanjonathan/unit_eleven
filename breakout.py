# Jonathan Lin
# 01/25/2019
# Create a Breakout game with images and sounds
import pygame
import sys
import brick
import paddle
import ball
from pygame.locals import *


def main():

    # Constants that will be used in the program
    APPLICATION_WIDTH = 500
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH = (APPLICATION_WIDTH - (BRICKS_PER_ROW -1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 10
    PADDLE_WIDTH = 60
    PADDLE_HEIGHT = 10
    RADIUS_OF_BALL = 10
    NUM_TURNS = 3
    BLACK = (0, 0, 0)

    # Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
    # the screen (BRICK_Y_OFFSET)
    pygame.init()
    # Create a window for the game
    mainSurface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 32, 0)
    pygame.display.set_caption("Break Out")
    bricksGroup = pygame.sprite.Group()
    paddleGroup = pygame.sprite.Group()

    # Create a pile of bricks
    x = 0
    y = BRICK_Y_OFFSET
    bricks = 10
    for rows in range(10):
        for number in range(bricks):
            pile = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, color)
            pile.rect.x = x
            pile.rect.y = y
            bricksGroup.add(pile)
            # Add the row to the window(surface)
            mainSurface.blit(pile.image, pile.rect)
            x = x + BRICK_WIDTH + BRICK_SEP
        # Start over at x = 0, but move up by the brick height + brick separation to draw two new rows
        x = 0
        y = y + BRICK_HEIGHT + BRICK_SEP
    pygame.display.update()

    # Step 2: Create a paddle
    board = paddle.Paddle(mainSurface, BLACK, PADDLE_WIDTH, PADDLE_HEIGHT)
    # The paddle starts at the middle of the screen and has a 30 pixel distance away from the bottom.
    board.rect.x = APPLICATION_WIDTH / 2
    board.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    # Add the paddle to the main surface
    mainSurface.blit(board.image, board.rect)
    paddleGroup.add(board)
    pygame.display.update()

    # Step 3: Create a ball
    circle = ball.Ball(BLACK, APPLICATION_WIDTH, APPLICATION_HEIGHT, RADIUS_OF_BALL)
    # The ball starts at the middle of the window
    circle.rect.x = APPLICATION_WIDTH / 2
    circle.rect.y = APPLICATION_HEIGHT / 2
    pygame.display.update()

    background = pygame.image.load("cat.png")
    background_rect = background.get_rect()
    background_rect.x = 0
    background_rect.y = 0
    while True:
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()
        # Fill the window with the image every time the ball or the paddle moves
        mainSurface.blit(background, background_rect)
        # Add all the bricks on the window every time the ball or the paddle moves
        for cubes in bricksGroup:
            mainSurface.blit(cubes.image, cubes.rect)
        board.move()
        mainSurface.blit(board.image, board.rect)
        circle.move()
        circle.collision(paddleGroup)
        circle.collisionBrick(bricksGroup)
        # There are three turns in total to play breakout.
        # If the turn becomes 0(the ball hits the ball for three times), the player loses and the game stops and quits.
        if circle.rect.bottom >= APPLICATION_HEIGHT:
            # Every time the ball hits the bottom, the number of turns(3) will minus 1.
            NUM_TURNS = NUM_TURNS - 1
            # Reset the position of the ball.
            circle.rect.x = APPLICATION_WIDTH / 2
            circle.rect.y = APPLICATION_HEIGHT / 2
            # If the ball hits the bottom, the lose sound will be played.
            lose_sound = pygame.mixer.Sound("dk_dawae.wav")
            lose_sound.play()
            # The game waits for a second.
            pygame.time.wait(1000)
            # The ball will move with its original speed from the reset position.
            circle.speedx = 5
            circle.speedy = 6
            # If the user loses, the game waits for 1.5 seconds and quits afterwards.
            if NUM_TURNS == 0:
                pygame.time.wait(1500)
                pygame.quit()
                sys.exit()
        # If all bricks are eliminated(have collided with the ball), the game waits for 3 seconds.
        # It will play the winning sound, and quit.
        if len(bricksGroup) == 0:
            win_sound = pygame.mixer.Sound("clicking.wav")
            win_sound.play()
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()
        mainSurface.blit(circle.image, circle.rect)
        pygame.display.update()


main()
