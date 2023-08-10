import pygame
from Sprite import sprite
from Turning_Sprite import turning_sprite

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 720))
clock = pygame.time.Clock()
running = True

CharacterAni = turning_sprite(['Images/CharacterFF.png', 'Images/CharacterFB.png',
                               'Images/CharacterFL.png', 'Images/CharacterFR.png'],size=(75,112.5))
ShieldAni = turning_sprite(['Images/Shield Down.png', 'Images/Shield Up.png',
                               'Images/Shield Left.png', 'Images/Shield Right.png'])
ShieldAni.left = pygame.transform.scale(ShieldAni.left, (30, 150))
ShieldAni.right = pygame.transform.scale(ShieldAni.right, (30, 150))
ShieldAni.forward = pygame.transform.scale(ShieldAni.forward, (150, 30))
ShieldAni.backward = pygame.transform.scale(ShieldAni.backward, (150, 30))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # fill the screen with a color to wipe away anything from last frame
    screen.fill('black')

    # RENDER YOUR GAME HERE
    screen.blit(CharacterAni.get_current_image(), [screen.get_width()/2 - CharacterAni.get_current_image().get_width()/2
        ,screen.get_height()/2- CharacterAni.get_current_image().get_height()/2])


    screen.blit(ShieldAni.get_current_image(),
                [screen.get_width() / 2 - ShieldAni.get_current_image().get_width() / 2
                    , screen.get_height() / 2 - ShieldAni.get_current_image().get_height() / 2])
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
