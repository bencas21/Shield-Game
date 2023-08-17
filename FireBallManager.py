import pygame
import random
import time
from FireBall import fire_ball

class fire_ball_manager():
    def __init__(self, level, screen):
        self.__screen = screen
        self.level = level

        self.fire_balls = pygame.sprite.Group()

        start_for_rand_count = level * 3
        end_for_rand_count = start_for_rand_count * 2
        fire_ball_count = random.randint(start_for_rand_count, end_for_rand_count)

        for i in range(fire_ball_count):
            start_for_rand_speed = level * 0.5
            end_for_rand_speed = level * 3
            fire_ball_speed = random.uniform(start_for_rand_speed, end_for_rand_speed)

            fire_ball_temp = fire_ball(['Images/Fire1.png', 'Images/Fire2.png',
                                        'Images/Fire3.png'], (35, 35), screen, fire_ball_speed, 'black')

            self.fire_balls.add(fire_ball_temp)

    def shoot_fire_balls(self):
        for ball in self.fire_balls:
            ball.shoot(self.__screen)




