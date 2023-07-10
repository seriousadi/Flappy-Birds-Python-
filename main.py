import pygame
import os
from Imagegenerator import ImageHandler
from random import randint

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 550))
clock = pygame.time.Clock()


# give random int
def getRandInt():
    return randint(225, 500)


# initializing Imagehandler
Imagehandler = ImageHandler(screen)
background_speed = 0
bird_y = Imagehandler.y
pipe1x, pipe1y = 400, getRandInt()
pipe2x, pipe2y = 600, getRandInt()
pipe3x, pipe3y = 800, getRandInt()
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
    Imagehandler.render_background(background_speed)

    if background_speed < -504:
        background_speed = 0
        y_for_pipes = getRandInt()
    background_speed -= 5
    # movements of bird
    # when mouse isn't clicked the bird falls and when mouse is clicked it fly
    bird_y += 15
    mouse_left_click = pygame.mouse.get_pressed(3)[0]
    if not mouse_left_click:
        Imagehandler.render_birdflying(bird_y)


    else:
        bird_y -= 50
        Imagehandler.render_birdup(bird_y)
    # managing pipes movements
    pipe1x -= 5
    pipe2x -= 5
    pipe3x -= 5
    if pipe1x <= -66:
        pipe1x = pipe3x + 200
        pipe1y = getRandInt()
    if pipe2x <= -66:
        pipe2x = pipe1x + 200
        pipe2y = getRandInt()
    if pipe3x <= -66:
        pipe3x = pipe2x + 200
        pipe3y = getRandInt()

    Imagehandler.render_pipes(x1=pipe1x, y1=pipe1y, x2=pipe2x, y2=pipe2y, x3=pipe3x, y3=pipe3y)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(10)  # limits FPS to 60

pygame.quit()
