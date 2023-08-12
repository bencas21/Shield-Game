import threading
from ArrowKeyController import arrow_key_controller
import pygame
import time
from threading import Thread

class player:
    def __init__(self, images, colorkey = None, size = (100,100), position = (50,50)):
        #create the list of animations (must be in the format FF, FB, FL, Fr)
        self.__animation_list = []
        for image in images:
            animation_to_add = pygame.image.load(image).convert()
            animation_to_add = pygame.transform.scale(animation_to_add,size).convert()
            animation_to_add.set_colorkey(colorkey)
            self.__animation_list.append(animation_to_add)

        # Create a controller
        self.__player_controller = arrow_key_controller()

        # Set initial current_image to 'up'
        self.__current_image = self.__animation_list[0]

        # Create the rectangle for the player
        self.__rect = self.__current_image.get_rect()
        self.__rect.center = position

    # updating the character direction with the controller
    def __update_player_image_selection(self):
        self.__player_controller.update_direction()
        if self.__player_controller.get_current_direction() == 'up':
            self.__current_image = self.__animation_list[0]
        elif self.__player_controller.get_current_direction() == 'down':
            self.__current_image = self.__animation_list[1]
        elif self.__player_controller.get_current_direction() == 'left':
            self.__current_image = self.__animation_list[2]
        elif self.__player_controller.get_current_direction() == 'right':
            self.__current_image = self.__animation_list[3]

    # update the display and draw character
    def update_player_display(self,screen):
        self.__update_player_image_selection()
        screen.blit(self.__current_image, self.__rect)

    def get_rect(self):
        return self.__rect








    """ def get_animation_list(self):
        return self.animation_list

    def next_image_pointer(self):
        if self.image_pointer < len(self.animation_list) - 1:
            self.image_pointer += 1
        else:
            self.image_pointer = 0



    def get_image_pointer(self):
        return self.image_pointer

    def get_current_image(self):
        return self.animation_list[self.image_pointer]
        
    """







