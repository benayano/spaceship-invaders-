import random

import pygame.sprite

from settings.ScreenSettings import ScreenSettings
from ShapeCreator import ShapeCreator
from shape import SpaceShip, Invaders


class ScreenGame:

    def __init__(self):
        self.stop_game = False
        self.settings = ScreenSettings()
        self.screen = pygame.display.set_mode(self.settings.game_size)
        self.creator = ShapeCreator(self.settings.game_size, self.screen)
        self.spaceship = self.creator.create_spaceship()
        self.bg = pygame.image.load(self.settings.bg_img_path)

        self.screen.blit(self.bg, (0, 0))
        self.font = pygame.font.Font(None, 36)

        self.game_size = self.settings.game_size
        self.munitionsFriendly = pygame.sprite.Group()
        self.munitionsEnemy = pygame.sprite.Group()
        self.invaders = pygame.sprite.Group()
        self.speed_invaders = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()

        self.create_invaders()

    def update(self):
        if not self.stop_game:
            self.game_is_running()
        else:
            self.game_is_stop()

    def game_is_running(self):
        self.screen.blit(self.bg, (0, 0))
        self.spaceship.draw(self.screen)
        self.munitionsFriendly.update()
        self.munitionsEnemy.update()
        self.blocks.update()
        self.update_invader_grope(self.invaders)
        self.update_invader_grope(self.speed_invaders)
        self.invaders.draw(self.screen)
        self.speed_invaders.draw(self.screen)
        self.munitionsFriendly.draw(self.screen)
        self.munitionsEnemy.draw(self.screen)
        self.check_accidents()
        self.draw_spaceship_lives(self.spaceship.life)
        self.you_winner()
        pygame.display.update()

    def game_is_stop(self):
        self.screen.blit(self.bg, (0, 0))
        # pygame.display.update()

    def update_invader_grope(self, invaders):
        for invader in invaders:
            if invader.rect.right > self.game_size[0] or invader.rect.left < 0:
                invaders.update(True)
                break
        invaders.update(False)

    def spaceship_shooting(self):
        self.munitionsFriendly.add(self.spaceship.shoot_sms())
        self.munitionsFriendly.draw(self.screen)

    def invaders_shooting(self):
        if self.invaders.sprites():
            random_invader = random.choice(self.invaders.sprites())
            self.munitionsEnemy.add(random_invader.shoot_sms())

    def create_invaders(self):
        self.creator.createInvaders(self.invaders)
        self.creator.create_speed_invaders(self.speed_invaders)

    def draw_spaceship_lives(self, live_rest):
        if live_rest:
            self.creator.draw_lives(live_rest)
        else:
            self.stop_game = True
            self.creator.draw_text_on_screen('game over')

    def check_accidents(self):
        pygame.sprite.groupcollide(self.invaders, self.munitionsFriendly, True, True)
        pygame.sprite.groupcollide(self.speed_invaders, self.munitionsFriendly, True, True)
        pygame.sprite.groupcollide(self.blocks, self.munitionsFriendly, True, True)
        pygame.sprite.groupcollide(self.blocks, self.munitionsEnemy, True, True)
        pygame.sprite.groupcollide(self.munitionsFriendly, self.munitionsEnemy, True, True)

        if pygame.sprite.spritecollide(self.spaceship, self.munitionsEnemy, True):
            self.spaceship.accident()

    def you_winner(self):
        if not self.invaders and not self.speed_invaders:
            self.stop_game = True
            self.creator.draw_text_on_screen('you are winner !!!!')
