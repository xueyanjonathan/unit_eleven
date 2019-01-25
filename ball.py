# Jonathan Lin
# 01/25/2019
# Create the ball in the breakout game
import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight, radius):
        # initialize sprite super class
        super().__init__()
         
        # finish setting the class variables to the parameters
        self.color = color
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.radius = radius

        # Create a surface, get the rect coordinates
        self.image = pygame.image.load("knuckles.png")
        self.rect = self.image.get_rect()

        # Set the speed of the ball
        self.speedx = 5
        self.speedy = 6
        self.hit_sound = pygame.mixer.Sound("running.wav")

    def move(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # If the top of the ball hit the top of the window, or the bottom of the ball hit the bottom of the window,
        # the vertical velocity of the ball reverses.
        if self.rect.top <= 0 or self.rect.bottom >= self.windowHeight:
            self.speedy = -self.speedy
        # If the sides of the ball hit the sides of the window, reverse the ball's horizontal velocity.
        if self.rect.left <= 0 or self.rect.right >= self.windowWidth:
            self.speedx = -self.speedx

    def collision(self, spriteGroup):
        # If the ball hit the paddle, the ball's vertical velocity reverses
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.speedy = -self.speedy
            self.hit_sound.play()

    def collisionBrick(self, spriteGroup):
        # If the ball hit a brick, eliminate the brick from the sprite group and reverse the ball's vertical direction.
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.speedy = -self.speedy

