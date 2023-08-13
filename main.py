import pygame
from FireBall import fire_ball
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

single_fire_ball = fire_ball(['Images/Fire1.png', 'Images/Fire2.png',
               'Images/Fire3.png'],(35,35),screen,'black')


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

    if (single_fire_ball.get_rect().colliderect(ShieldAni.get_rect())):
        single_fire_ball.kill()
    else:
        single_fire_ball.shoot(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
