import pygame
import random
import threading
import time
from Shield import shield
from Player import player

# pygame setup
pygame.init()
screen = pygame.display.set_mode((750, 750))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()
running = True

# Creating Character and Shield and Fire Sprites
CharacterAni = player(['Images/CharacterFB.png', 'Images/CharacterFF.png',
                               'Images/CharacterFL.png', 'Images/CharacterFR.png'],
                      colorkey=None, size=(50, 80),position = screen_rect.center)

ShieldAni = shield('Images/Shield Down.png', (80, 20), CharacterAni.get_rect().center[0],
                   CharacterAni.get_rect().center[1])

"""Fire = sprite(['Images/Fire1.png', 'Images/Fire2.png',
               'Images/Fire3.png'], colorkey='black', size=(35, 35))

# Dict of Positions where fire should come from
Fire_Start_Positions = {'Top': [screen.get_width() / 2 - Fire.get_current_image().get_width() / 2, 0],
                        'Bottom': [screen.get_width() / 2 - Fire.get_current_image().get_width() / 2,
                                   screen.get_height() - 50],
                        'Left': [0, screen.get_height() / 2 - Fire.get_current_image().get_height() / 2],
                        'Right': [screen.get_width() - 50,
                                  screen.get_height() / 2 - Fire.get_current_image().get_height() / 2]}

#Used for Threading
def animate_fire(fire_sprite):
    while running:
        fire_sprite.next_image_pointer()
        time.sleep(0.1)  # Delay here for animation


# Create and start the thread for Fire animation
fire_animation_thread = threading.Thread(target=animate_fire, args=(Fire,))
fire_animation_thread.start()

# Function for Fire shooting at character


"""

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill('Black')

    # RENDER YOUR GAME HERE

    # Display Character

    CharacterAni.update_player_display(screen)
    ShieldAni.update_shield(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
