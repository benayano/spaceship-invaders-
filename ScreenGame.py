import random

import pygame.sprite

from Font import Font
from shape import SpaceShip, Invaders


class ScreenGame:

    def __init__(self, game_size=(1200, 800)):
        spaceship_size = (75, 100)
        start_place = (game_size[0] / 2, game_size[1] - spaceship_size[1] // 2)
        self.spaceship = SpaceShip(start_place, "images/spaceship.jpg", spaceship_size, game_size)

        self.bg = pygame.image.load("images/bg.jpg")

        self.screen = pygame.display.set_mode(game_size)
        self.screen.blit(self.bg, (0, 0))
        self.font = pygame.font.Font(None, 36)

        self.game_size = game_size
        self.munitionsFriendly = pygame.sprite.Group()
        self.munitionsEnemy = pygame.sprite.Group()
        self.invaders = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()

        self.create_invaders()

    def update(self):

        self.screen.blit(self.bg, (0, 0))
        self.spaceship.draw(self.screen)
        self.munitionsFriendly.update()
        self.munitionsEnemy.update()
        self.blocks.update()
        self.update_invader_grope(self.invaders)
        self.invaders.draw(self.screen)
        self.munitionsFriendly.draw(self.screen)
        self.munitionsEnemy.draw(self.screen)
        self.check_accidents()
        self.winner()
        pygame.display.update()

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
        else:
            self.winner()

    def create_invaders(self, row=2, columns=6):
        image_path, invader_size, space_objects = 'images/Invaders.jpg', (70, 60), (50, 100)
        for i in range(0, row):
            for j in range(0, columns):
                # calculate potion of each invader
                position = (j * invader_size[0] + space_objects[0] + 10, i * invader_size[1] + space_objects[1])
                invader = Invaders(position, image_path, invader_size, self.game_size)
                self.invaders.add(invader)

    def check_accidents(self):
        pygame.sprite.groupcollide(self.invaders, self.munitionsFriendly, True, True)
        pygame.sprite.groupcollide(self.blocks, self.munitionsFriendly, True, True)
        pygame.sprite.groupcollide(self.blocks, self.munitionsEnemy, True, True)
        pygame.sprite.groupcollide(self.munitionsFriendly, self.munitionsEnemy, True, True)

        if pygame.sprite.spritecollide(self.spaceship, self.munitionsEnemy, True):
            print(f"the ship is collide{self.spaceship.life}")
            self.spaceship.accident()

    def winner(self, green=(0, 255, 0), blue=(0, 0, 128)):
        font = pygame.font.Font('freesansbold.ttf', 180)
        game_over_text = font.render('game over', True, green, blue)
        textRect = game_over_text.get_rect()
        textRect.move_ip(self.game_size[0]//3,self.game_size[1]//3)

        self.screen.blit(game_over_text, textRect)


