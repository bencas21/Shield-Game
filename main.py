import pygame
from FireBall import fire_ball
from Shield import shield
from Player import player
from FireBallManager import fire_ball_manager

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

fireballs = fire_ball_manager(1, screen)


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
    fireballs.shoot_fire_balls()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
