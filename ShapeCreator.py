import pygame

from settings.ShapeSettings import ShapeSettings
from shape import Invaders, SpaceShip


class ShapeCreator:
    def __init__(self, game_size, screen):
        self.game_size = game_size
        self.settings = ShapeSettings()
        self.screen = screen

    def createInvaders(self, invedetsGrop):

        for i in range(0, self.settings.row_invaders):
            for j in range(0, self.settings.columns_invaders):
                # calculate position of each invader
                position = (j * self.settings.invader_size[0] + self.settings.space_objects[0] + 10,
                            i * self.settings.invader_size[1] + self.settings.space_objects[1])
                invader = Invaders(position, self.settings.invaders_image_path, self.settings.invader_size,
                                   self.game_size, velocity=self.settings.invaders_velocity)
                invedetsGrop.add(invader)

    def create_spaceship(self):
        start_place = (self.game_size[0] // 2, self.game_size[1] - self.settings.spaceship_size[1] // 2)
        return SpaceShip(start_place, self.settings.spaceship_image_path,
                         self.settings.spaceship_size, self.game_size)

    def create_speed_invaders(self, speed_invaders):
        position = (self.settings.invader_size[0] + self.settings.space_objects[0] + 10,
                    self.settings.invader_size[1] + self.settings.space_objects[1])
        invader = Invaders(position, self.settings.invaders_image_path, self.settings.invader_size, self.game_size,
                           velocity=(3, 0))
        speed_invaders.add(invader)

    def draw_lives(self, live_rest):
        for i in range(live_rest):
            place = (self.settings.spaceship_size[0] * i + 20, self.settings.spaceship_size[1])
            SpaceShip(place, self.settings.spaceship_image_path, self.settings.spaceship_size, self.game_size).draw(
                self.screen)

    def draw_text_on_screen(self, text, green=(0, 255, 0), blue=(0, 0, 128), size=100):
        font = pygame.font.Font('freesansbold.ttf', size)
        text_status = font.render(text, True, green, blue)
        textRect = text_status.get_rect()
        textRect.move_ip((self.game_size[0] - size * 0.5 * len(text)) // 3, self.game_size[1] // 3)
        self.screen.blit(text_status, textRect)
