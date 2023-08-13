import pygame
import random


class fire_ball(pygame.sprite.Sprite):
    def __init__(self, images, size, screen, colorkey=None):



        super(fire_ball, self).__init__()
        self.__speed = 1
        position_dict = {'Top': [screen.get_width() / 2, 0],
                         'Bottom': [screen.get_width() / 2,
                                    screen.get_height() - 50],
                         'Left': [0, screen.get_height() / 2],
                         'Right': [screen.get_width() - 50,
                                   screen.get_height() / 2]}

        self.__start_position = random.choice(list(position_dict))
        rotation = 0
        if self.__start_position == 'Top':
            pass
        elif self.__start_position == 'Bottom':
            rotation = 180
        elif self.__start_position == 'Left':
            rotation = 90
        elif self.__start_position == 'Right':
            rotation = 270

        self.__animation_list = []
        for image in images:
            animation_to_add = pygame.image.load(image).convert()
            animation_to_add = pygame.transform.scale(animation_to_add, size).convert()
            animation_to_add = pygame.transform.rotate(animation_to_add, rotation)
            animation_to_add.set_colorkey(colorkey)
            self.__animation_list.append(animation_to_add)

        # Set initial current_image
        self.__current_image = self.__animation_list[0]

        # Create the rectangle for the fireball
        self.__rect = self.__current_image.get_rect()
        self.__rect.center = position_dict[self.__start_position]
        self.__image_pointer = 0

    def next_image(self):
        if self.__image_pointer < len(self.__animation_list) - 1:
            self.__image_pointer += 1
        else:
            self.__image_pointer = 0

        self.__current_image = self.__animation_list[self.__image_pointer]

    def shoot(self, screen):
        self.next_image()
        if self.__start_position == 'Top':
            self.__rect.y += self.__speed
        elif self.__start_position == 'Bottom':
            self.__rect.y -= self.__speed
        elif self.__start_position == 'Left':
            self.__rect.x += self.__speed
        elif self.__start_position == 'Right':
            self.__rect.x -= self.__speed
        screen.blit(self.__current_image, self.__rect)

    def get_rect(self):
        return self.__rect


