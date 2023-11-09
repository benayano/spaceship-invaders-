import pygame


class Shape(pygame.sprite.Sprite):

    def __init__(self, position, image_path, size, range_of_move, life=1, velocity=(0, 0)):
        super().__init__()
        self.img_shape = None
        self.position = position
        self.velocity = velocity
        self.image = self.load_and_adopt_image(image_path, size)
        self.life = life
        self.range_of_move = range_of_move
        self.rect = self.image.get_rect(center=position)
        self.size = size

    def load_and_adopt_image(self, image_path, size):
        self.img_shape = pygame.image.load(image_path)
        return pygame.transform.scale(self.img_shape, size)

    def draw(self, screen):
        screen.blit(self.img_shape, self.position)

    def accident(self):
        if self.life > 0:
            self.life -= 1
        else:
            self.kill()
            self.remove()


class SpaceShip(Shape):
    def __init__(self, position, image_path, size, range_of_move, life=3, velocity=(3, 0)):
        super().__init__(position, image_path, size, range_of_move, life, velocity)
        self.position = position
        self.velocity = self.velocity[0]

    def move_left(self):
        if self.rect[0] > 0:
            self.rect.move_ip(-self.velocity, 0)

    def move_right(self):
        if self.rect[0] < self.range_of_move[0] - self.size[0]:
            self.rect.move_ip(+self.velocity, 0)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def shoot_sms(self):
        return Munitions(self.rect.midtop, image_path="images/munitions.png", size=(30, 80),
                         range_of_move=self.range_of_move,
                         velocity=(0, -1))


class Invaders(Shape):
    def __init__(self, position, image_path, size, range_of_move, life=1, velocity=(1, 40)):
        super().__init__(position, image_path, size, range_of_move, life, velocity=velocity)
        self.velocity = (self.velocity[0], self.size[1] // 6)

    def update(self, change_direction):
        if change_direction:
            self.move_down()
            self.velocity = (-self.velocity[0], self.velocity[1])
        else:
            self.move(self.velocity[0])

    def move(self, direction):
        self.rect.move_ip(direction, 0)

    def move_down(self):
        self.rect.move_ip(0, self.velocity[1])

    def shoot_sms(self):
        return Munitions(self.rect.midtop, image_path="images/munitions.png", size=(30, 80),
                         range_of_move=self.range_of_move,
                         velocity=(0, 1))


class Munitions(Shape):
    def __init__(self, position, range_of_move, image_path, size, velocity=(0, 3)):
        super().__init__(position, image_path, size, range_of_move, velocity=velocity)

    def update(self):
        if 0 > self.rect.midtop[1] > self.range_of_move[1]:
            self.kill()
        else:
            self.rect.move_ip(0, self.velocity[1])

    def draw(self, screen):
        screen.blit(self.image, self.rect)
