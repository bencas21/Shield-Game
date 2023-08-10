import pygame
import random
import threading
import time

from Sprite import sprite
from Turning_Sprite import turning_sprite

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 720))
clock = pygame.time.Clock()
running = True

# Creating Character and Shield Sprites
CharacterAni = turning_sprite(['Images/CharacterFF.png', 'Images/CharacterFB.png',
                               'Images/CharacterFL.png', 'Images/CharacterFR.png'], size=(75, 112.5))
ShieldAni = turning_sprite(['Images/Shield Down.png', 'Images/Shield Up.png',
                            'Images/Shield Left.png', 'Images/Shield Right.png'])
Fire = sprite(['Images/Fire1.png', 'Images/Fire2.png',
               'Images/Fire3.png'], colorkey='black', size = (50,50))


def animate_fire(fire_sprite):
    while running:
        fire_sprite.next_image_pointer()
        time.sleep(0.5)  # Delay here for animation


def animate_fire(fire_sprite):
    while running:
        fire_sprite.next_image_pointer()
        time.sleep(0.1)  # Delay here for animation


# Create and start the thread for Fire animation
fire_animation_thread = threading.Thread(target=animate_fire, args=(Fire,))
fire_animation_thread.start()

# Reformating Shield (Will optimize later)
ShieldAni.left = pygame.transform.scale(ShieldAni.left, (25, 125))
ShieldAni.right = pygame.transform.scale(ShieldAni.right, (25, 125))
ShieldAni.forward = pygame.transform.scale(ShieldAni.forward, (125, 25))
ShieldAni.backward = pygame.transform.scale(ShieldAni.backward, (125, 25))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill('Black')

    # RENDER YOUR GAME HERE
    screen.blit(CharacterAni.get_current_image(),
                [screen.get_width() / 2 - CharacterAni.get_current_image().get_width() / 2
                    , screen.get_height() / 2 - CharacterAni.get_current_image().get_height() / 2])

    screen.blit(Fire.animation_list[Fire.get_image_pointer()], [50, 50])



    if ShieldAni.determine_position() == 'forward':
        x_sep_distance = 0
        y_sep_distance = 75
    elif ShieldAni.determine_position() == 'backward':
        x_sep_distance = 0
        y_sep_distance = -75
    elif ShieldAni.determine_position() == 'left':
        x_sep_distance = -75
        y_sep_distance = 0
    elif ShieldAni.determine_position() == 'right':
        x_sep_distance = 75
        y_sep_distance = 0

    screen.blit(ShieldAni.get_current_image(),
                [screen.get_width() / 2 - ShieldAni.get_current_image().get_width() / 2 + x_sep_distance
                    , screen.get_height() / 2 - ShieldAni.get_current_image().get_height() / 2 + y_sep_distance])

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
