class ShapeSettings:

    def __init__(self, spaceship_size=(75, 100), columns_invaders=6, row_invaders=3,
                 invaders_velocity=(2, 2)):
        self.spaceship_size = spaceship_size
        self.columns_invaders = columns_invaders
        self.row_invaders = row_invaders
        self.invaders_velocity = invaders_velocity

        # I don't want to offer to change it
        self.invader_size, self.space_objects = (70, 60), (50, 100)
        self.invaders_image_path = 'images/Invaders-removebg-preview.png'
        self.spaceship_image_path = "images/spaceship-removebg-preview.png"
