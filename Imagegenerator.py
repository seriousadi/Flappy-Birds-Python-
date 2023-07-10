import os
import pygame

current_directory = os.path.dirname(__file__)


class ImageHandler():
    def __init__(self, screen):
        self.Background = pygame.image.load(
            os.path.join(current_directory, "Resources/background.png")
        ).convert_alpha()
        self.birdflying = pygame.image.load(
            os.path.join(current_directory, "Resources/Birdflying.png")
        ).convert_alpha()
        self.birdup = pygame.image.load(
            os.path.join(current_directory, "Resources/BirdUp.png")
        ).convert_alpha()

        self.pipe = pygame.image.load(
            os.path.join(current_directory, "Resources/pipe.png")
        ).convert_alpha()
        self.pipe2 = pygame.transform.flip(self.pipe,flip_y=True,flip_x=False)
        # getting the screen to render images and things
        self.window = screen

        # initial coordinates of bird
        self.y = 240
        self.x = self.window.get_size()[0] / 2 - 80

    def render_background(self, x):
        self.window.blit(self.Background, (x, 50))
        self.window.blit(self.Background, (x + 504, 50))

    def render_pipes(self, x1, y1, x2, y2, x3, y3):
        self.pipes(x1,y1)
        self.pipes(x2,y2)
        self.pipes(x3,y3)
    def pipes(self,x,y):
        self.window.blit(self.pipe, (x, y))
        self.window.blit(self.pipe2, (x, y - 520))
    def render_birdflying(self, y):
        self.window.blit(self.birdflying, (self.x, y))

    def render_birdup(self, y):
        self.window.blit(self.birdup, (self.x, y))