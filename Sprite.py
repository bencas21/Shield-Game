import pygame


class sprite:

    def __init__(self, images, colorkey = None, size = (100,100)):
        self.animation_list = []
        for image in images:
            animation_to_add = pygame.image.load(image).convert()
            animation_to_add = pygame.transform.scale(animation_to_add,size).convert()
            animation_to_add.set_colorkey(colorkey)

            self.animation_list.append(animation_to_add)


    def get_animation_list(self):
        return self.animation_list
