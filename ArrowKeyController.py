import threading

import pygame
import time
from threading import Thread

class arrow_key_controller:
    def __init__(self):
        self.__current_direction = 'down'

    def update_direction(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.__current_direction = 'up'
        elif keys[pygame.K_DOWN]:
            self.__current_direction = 'down'
        elif keys[pygame.K_LEFT]:
            self.__current_direction = 'left'
        elif keys[pygame.K_RIGHT]:
            self.__current_direction = 'right'

    def get_current_direction(self):
        return self.__current_direction






