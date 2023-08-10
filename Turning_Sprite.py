import pygame
from Sprite import sprite


class turning_sprite(sprite):
    def __init__(self, images, colorkey = 'black', size= (100,100)):
        sprite.__init__(self, images,colorkey,size)
        self.forward = self.get_animation_list()[0]
        self.backward = self.get_animation_list()[1]
        self.left = self.get_animation_list()[2]
        self.right = self.get_animation_list()[3]
        self.position = 'forward'

    def determine_position(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.position = 'backward'
        elif keys[pygame.K_DOWN]:
            self.position = 'forward'
        elif keys[pygame.K_LEFT]:
            self.position = 'left'
        elif keys[pygame.K_RIGHT]:
            self.position = 'right'
        return self.position

    def get_current_image(self):
        if self.determine_position() == 'forward':
            return self.forward
        elif self.determine_position() == 'backward':
            return self.backward
        elif self.determine_position() == 'left':
            return self.left
        elif self.determine_position() == 'right':
            return self.right









