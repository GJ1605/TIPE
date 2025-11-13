import pygame

class Urgence :

    def __init__(self, hauteur): # on créer l'ambulance (image et position)
        self.image = pygame.image.load('assets/ambulance.png')
        self.image = pygame.transform.scale(self.image,(90,90))
        self.ambulance_rect = self.image.get_rect()
        self.ambulance_width = self.image.get_width()
        self.ambulance_rect.x = - self.ambulance_width
        self.ambulance_rect.y = hauteur*0.85
