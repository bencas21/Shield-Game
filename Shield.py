import pygame
from ArrowKeyController import arrow_key_controller


class shield(pygame.sprite.Sprite):

    def __init__(self, image, size, player_x, player_y):
        super().__init__()
        # Load the image
        self.__image_load = pygame.image.load(image).convert()
        self.__image_load = pygame.transform.scale(self.__image_load, size).convert()
        self.__image_load.set_colorkey('black')

        # Create the controler
        self.__shield_controller = arrow_key_controller()

        # Create the shield rectangle
        self.__rect = self.__image_load.get_rect()
        self.__rect.center = (player_x, player_y)
        self.__player_x = player_x
        self.__player_y = player_y

    def update_shield(self, screen):

        # Indicate direction from arrow keys
        self.__shield_controller.update_direction()

        #rotate shield based on shield controller
        if self.__shield_controller.get_current_direction() == 'up':
            transformed = pygame.transform.rotate(self.__image_load, 180)
            self.__rect = transformed.get_rect()
            self.__rect.center = (self.__player_x, self.__player_y - 50)
            screen.blit(transformed, self.__rect)

        elif self.__shield_controller.get_current_direction() == 'down':
            transformed = pygame.transform.rotate(self.__image_load, 0)
            self.__rect = transformed.get_rect()
            self.__rect.center = (self.__player_x, self.__player_y + 50)
            screen.blit(transformed, self.__rect)

        elif self.__shield_controller.get_current_direction() == 'left':
            transformed = pygame.transform.rotate(self.__image_load, 270)
            self.__rect = transformed.get_rect()
            self.__rect.center = (self.__player_x - 50, self.__player_y)
            screen.blit(transformed, self.__rect)

        elif self.__shield_controller.get_current_direction() == 'right':
            transformed = pygame.transform.rotate(self.__image_load, 90)
            self.__rect = transformed.get_rect()
            self.__rect.center = (self.__player_x + 50, self.__player_y)
            screen.blit(transformed, self.__rect)

    def get_rect(self):
        return self.__rect
