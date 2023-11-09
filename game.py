import pygame

from shape import SpaceShip

game_size = (800, 700)
spaceship_size = (100, 150)
snake_speed = 30
bg = pygame.image.load("images/bg.jpg")
spaceship_img = pygame.image.load("images/spaceship.jpg")
spaceship_img = pygame.transform.scale(spaceship_img, spaceship_size)

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

pygame.init()

screen = pygame.display.set_mode(game_size)

clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)

game_over = False
center_place = (game_size[0] // 2, game_size[1] // 2)
place = center_place
change = (0, 0)

spaceship = SpaceShip(center_place, "images/spaceship.jpg", spaceship_size, game_size)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [*center_place])


def checkGameOver(please):
    if please[0] > game_size[0] or please[1] > game_size[1] or please[0] < 0 or please[1] < 0:
        return True
    return False


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                spaceship.move_left()
            elif event.key == pygame.K_RIGHT:
                spaceship.move_right()

    screen.blit(bg, (0, 0))
    spaceship.draw(screen)
    pygame.display.update()
    clock.tick(snake_speed)
pygame.quit()
quit()
