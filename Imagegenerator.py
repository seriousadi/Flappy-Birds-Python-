import os
import pygame
import time
current_directory = os.path.dirname(__file__)


class ImageHandler:
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
        self.pipe2 = pygame.transform.flip(self.pipe, flip_y=True, flip_x=False)

        # getting the screen to render images and things
        self.window = screen

        # initial coordinates of bird
        self.y = 240
        self.x = self.window.get_size()[0] / 2 - 80
        self.bird_up_collision = self.window.blit(self.birdup, (0, 0))

        self.pipe_collision = self.window.blit(self.pipe, (0, 0))
        self.pipe2_collision = self.window.blit(self.pipe2, (0, 0 - 520))
        self.bird_flying_collision = self.window.blit(self.birdflying, (0, 0))
        self.bird_collided = False
    def render_background(self, x):
        self.window.blit(self.Background, (x, 50))
        self.window.blit(self.Background, (x + 504, 50))

    def render_pipes(self, x1, y1, x2, y2, x3, y3):
        self.pipes(x1, y1)
        self.pipes(x2, y2)
        self.pipes(x3, y3)

    def pipes(self, x, y):
        self.pipe_collision = self.window.blit(self.pipe, (x, y))
        self.pipe2_collision = self.window.blit(self.pipe2, (x, y - 520))
        self.check_collision()

    def render_birdflying(self, y):
        self.bird_flying_collision = self.window.blit(self.birdflying, (self.x, y))

    def render_birdup(self, y):
        self.bird_up_collision = self.window.blit(self.birdup, (self.x, y))
        self.check_collision()

    def check_collision(self):
        case_1 = self.bird_up_collision.colliderect(self.pipe_collision)
        case_2 = self.bird_up_collision.colliderect(self.pipe2_collision)
        case_3 = self.bird_flying_collision.colliderect(self.pipe_collision)
        case_4 = self.bird_flying_collision.colliderect(self.pipe2_collision)
        if case_1 or case_2 or case_3 or case_4:
            self.bird_collided = True
            time.sleep(3)
