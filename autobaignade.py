import pygame
import random

class AutoBaignade(pygame.sprite.Sprite):

    def __init__(self, largeur, hauteur):
        super().__init__()
        self.watertemperature = random.uniform(15, 31) # donne une température de l'eau de mer/océan
        self.bodytemperature = 37.5
        self.ecarttemperature = self.bodytemperature - self.watertemperature
        if (self.ecarttemperature > 15): # compare l'écart de température entre l'eau et le corps pour savoir à quel point c'est dangereux
            self.ecart = 'orange'
            if (self.ecarttemperature > 20):
                self.ecart = 'red'
        else:
            self.ecart = 'green'
            
        self.wind = random.choice(['green','green','green', 'orange', 'red']) # donne une force au vent du moins dangereux au plus dangereux (plus grande probabilité de tomber sur vert pour faciliter l'utilisation du jeu)

        if ((self.ecart == 'green') and (self.wind == 'green')) or ((self.ecart == 'green') and (self.wind == 'orange')) : # teste si toutes les conditions sont remplies pour aller dans l'eau => drapeau vert
            self.vent = 'douce' # force du vent
            self.image = pygame.image.load('assets/drapeauvert.png')
            self.rect = self.image.get_rect() #récupérer la position
            self.rect.x = largeur/20
            self.rect.y = hauteur*0.9 
            self.color = 'green'

        if (((self.ecart == 'orange') and (self.wind == 'orange')) or ((self.ecart == 'green') and (self.wind == 'orange'))) : # => drapeau orange, au moins un indicateur est orange
            self.vent = 'moyenne' # force du vent
            self.image = pygame.image.load('assets/drapeauorange.png')
            self.image = pygame.transform.scale(self.image,(largeur,hauteur))
            self.rect = self.image.get_rect() #récupérer la position
            self.rect.x = 0
            self.rect.y = 0
            self.color = 'orange'

        if (((self.ecart == 'red') and (self.wind == 'red')) or ((self.ecart == 'red') and (self.wind != 'red')) or ((self.ecart != 'red') and (self.wind == 'red'))) : # => drapeau rouge, au moins un indicateur est rouge
            self.vent = 'dangereuse' # force du vent
            self.image = pygame.image.load('assets/drapeaurouge.png')
            self.image = pygame.transform.scale(self.image,(largeur,hauteur))
            self.rect = self.image.get_rect() #récupérer la position
            self.rect.x = 0
            self.rect.y = 0 
            self.color = 'red'
