import pygame
import random
import time
from FireBall import fire_ball
from threading import Thread


class fire_ball_manager():
    def __init__(self, level, screen):

        # screen and level
        self.__screen = screen
        self.__level = level

        # sprite group used for current level's fireballs
        self.fire_balls = pygame.sprite.Group()

        # random fireball count for fireballs
        start_for_rand_count = level
        end_for_rand_count = start_for_rand_count * 2
        fire_ball_count = random.randint(start_for_rand_count, end_for_rand_count)

        # for each fireball determine a random speed
        for i in range(fire_ball_count):
            start_for_rand_speed = level * 0.5
            end_for_rand_speed = level
            fire_ball_speed = random.uniform(start_for_rand_speed, end_for_rand_speed)

            fire_ball_temp = fire_ball(['Images/Fire1.png', 'Images/Fire2.png',
                                        'Images/Fire3.png'], (35, 35), screen, fire_ball_speed, 'black')
            self.fire_balls.add(fire_ball_temp)

        # start the initial shot of each fireball
        t = Thread(target=self.__first_shot_balls)
        t.start()

    # initial shot of the fireballs with a delay (used in a thread)
    def __first_shot_balls(self):
        for ball in self.fire_balls:
            ball.shoot(self.__screen)
            time.sleep(random.uniform(0.05, 1))

    # shoot fireballs normal
    def shoot_fire_balls(self):
        for ball in self.fire_balls:
            if ball.shot_yet and ball.active:
                ball.shoot(self.__screen)


