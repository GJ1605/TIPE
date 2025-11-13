import pygame

class Warning (pygame.sprite.Sprite):

    def __init__(self): # on créer les panneaux de danger lors d'une collision
        super().__init__()
        self.image = pygame.image.load('assets/panneaudanger.png')
        self.width = int(self.image.get_width()/2)
        self.height = int(self.image.get_height()/2)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
