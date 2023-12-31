import pygame

from ScreenGame import ScreenGame


class MainGame:

    def __init__(self, running=True):
        self.running = running
        self.clock = pygame.time.Clock()
        self.space_between_shoots = 1
        SPACE_SHOOTING = 150
        pygame.init()

        self.screen_game = ScreenGame()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.screen_game.spaceship_shooting()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.screen_game.spaceship.move_left()
            if keys[pygame.K_RIGHT]:
                self.screen_game.spaceship.move_right()

            self.space_between_shoots = (self.space_between_shoots + 1) % SPACE_SHOOTING
            if self.space_between_shoots == 1:
                self.screen_game.invaders_shooting()

            self.clock.tick(60)
            self.screen_game.update()

        pygame.quit()
