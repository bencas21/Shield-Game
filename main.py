import pygame
from FireBall import fire_ball
from Shield import shield
from Player import player
from FireBallManager import fire_ball_manager
from PlayerStats import player_stats

# pygame setup
pygame.init()
screen = pygame.display.set_mode((750, 750))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()
running = True

# Creating Character and Shield
CharacterAni = player(['Images/CharacterFB.png', 'Images/CharacterFF.png',
                       'Images/CharacterFL.png', 'Images/CharacterFR.png'],
                      colorkey=None, size=(50, 80), position=screen_rect.center)
ShieldAni = shield('Images/Shield Down.png', (80, 20), CharacterAni.get_rect().center[0],
                   CharacterAni.get_rect().center[1])

# Player Stats class
stats = player_stats()

while running:

    # fireballs for current level
    fireballs = fire_ball_manager(stats.get_level(), screen)

    # is the current level done?
    level_over = False

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    while not level_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                level_over = True
        # fill the screen with a color to wipe away anything from last frame
        screen.fill('Black')

        # fireball events
        event = fireballs.shoot_fire_balls(CharacterAni.get_rect(), ShieldAni.get_rect())

        # do relevant stuff for event
        if event == 'Hit':
            stats.lose_health()
        elif event == 'Blocked':
            stats.score_up()
        elif event == 'Next Level':
            stats.next_level()
            print(stats.get_level())
            level_over = True
        else:
            pass

        # Update character and shield directions
        CharacterAni.update_player_display(screen)
        ShieldAni.update_shield(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    # RENDER YOUR GAME HERE

    # Display Character

pygame.quit()
