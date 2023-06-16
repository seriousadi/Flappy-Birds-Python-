import pygame
import os
from Imagegenerator import ImageHandler

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 550))
clock = pygame.time.Clock()

# initializing Imagehandler
Imagehandler = ImageHandler(screen)
background_and_pipe_speed = 0
bird_y = Imagehandler.y

running = True
current_directory = os.path.dirname(__file__)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#71C5CF")

    # moving background
    Imagehandler.render_background(background_and_pipe_speed)
    background_and_pipe_speed -= 1
    # movements of bird
    # when mouse isn't clicked the bird falls and when mouse is clicked it fly
    bird_y += 15
    mouse_left_click = pygame.mouse.get_pressed(3)[0]
    if not mouse_left_click:
        Imagehandler.render_birdflying(bird_y)


    else:
        bird_y -= 50
        Imagehandler.render_birdup(bird_y)

    Imagehandler.render_pipes(0, -260)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(10)  # limits FPS to 60

pygame.quit()
