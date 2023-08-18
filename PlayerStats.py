class player_stats:
    def __init__(self):
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

    def score(self):
        self.__score +=1