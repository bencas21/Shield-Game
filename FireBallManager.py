import math

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
        start_for_rand_count = level * 2
        end_for_rand_count = start_for_rand_count * 2
        fire_ball_count = random.randint(start_for_rand_count, end_for_rand_count)

        # for each fireball determine a random speed
        for i in range(fire_ball_count):
            start_for_rand_speed =math.ceil(level * 0.1)
            end_for_rand_speed = math.ceil(level * 0.3)
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
            time.sleep(random.uniform(3/(self.__level), 6/(self.__level)))

    # shoot fireballs normal
    def shoot_fire_balls(self,player_rect,shield_rect):
        if len(self.fire_balls.sprites()) == 0:
            return 'Next Level'
        for ball in self.fire_balls:
            if ball.shot_yet and ball.active:
                ball.shoot(self.__screen)

                # Fireball events
                if ball.hit_player_or_shield(player_rect, shield_rect) == 'Player Hit':
                    ball.kill()
                    ball.active = False
                    return 'Hit'
                if ball.hit_player_or_shield(player_rect, shield_rect) == 'Shield Hit':
                    ball.kill()
                    ball.active = False
                    return 'Blocked'

        return 'None'








