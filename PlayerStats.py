import pygame

class player_stats:
    def __init__(self, screen):
        self.__screen = screen
        self.__level = 1
        self.__health = 4
        self.__score = 0

    def get_level(self):
        return self.__level

    def get_health(self):
        return self.__health

    def get_score(self):
        return self.__score

    def next_level(self):
        self.__level += 1

    def lose_health(self):
        self.__health -= 1

    def score_up(self):
        self.__score += 1

    def display_stats(self):
        font = pygame.font.SysFont("Arial", 30)
        level_text = font.render('Level: ' + str(self.__level), True, 'white')
        self.__screen.blit(level_text, (self.__screen.get_width() - 115, 10))
        lives_text = font.render('Lives: ' + str(self.__health), True, 'white')
        self.__screen.blit(lives_text, (self.__screen.get_width() - 115, 10 + level_text.get_height()))
        score_text = font.render('Score: ' + str(self.__score), True, 'white')
        self.__screen.blit(score_text, (25, 10))