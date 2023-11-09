import pygame


class Font:
    def __init__(self, green=(0, 255, 0), blue=(0, 0, 128)):
        self.__font = pygame.font.Font('freesansbold.ttf', 32)
        self.game_over_text = self.__font.render('game over', True, green, blue)
        self.textRect = self.game_over_text.get_rect()

    def draw(self, screen):
        screen.blit(self.game_over_text, self.textRect)
