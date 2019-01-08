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

        # Create a surface, get the rect coordinates, fill the surface with a white color (or whatever color the
        # background of your breakout game will be.
        self.image = pygame.Surface((self.radius, self.radius))
        self.rect = self.image.get_rect()
        self.image.fill(self.color)

        # Add a circle to represent the ball to the surface just created.

        # Set the speed of the ball
        self.speedx = 3
        self.speedy = 5

    def move(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top <= 0 or self.rect.bottom >= self.windowHeight:
            self.speedy = -self.speedy
        if self.rect.left <= 0 or self.rect.right >= self.windowWidth:
            self.speedx = -self.speedx

    def collision(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.speedy = -self.speedy

    def collisionBrick(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.speedy = -self.speedy


