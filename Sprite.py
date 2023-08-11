import threading

import pygame
import time
from threading import Thread

class sprite:

    def __init__(self, images, colorkey = None, size = (100,100)):
        self.animation_list = []
        self.image_pointer = 0

        for image in images:
            animation_to_add = pygame.image.load(image).convert()
            animation_to_add = pygame.transform.scale(animation_to_add,size).convert()
            animation_to_add.set_colorkey(colorkey)

            self.animation_list.append(animation_to_add)

    def get_animation_list(self):
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





