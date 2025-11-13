import pygame
from urgence import Urgence

#creer une premiere classe qui va representer la bouée
class Bouee(pygame.sprite.Sprite): #élément sprite => élément qui peut se déplacer, composant graphique

    def __init__(self, largeur, hauteur):
        super().__init__() #initialise la superclass Sprite
        self.velocity = 5 #vitesse
        self.image = pygame.image.load('assets/bouee.png')
        self.rect = self.image.get_rect() #récupérer la position
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = (largeur/2 - self.image.get_width()/2)  #postition selon x
        self.rect.y = hauteur*0.9 #position selon y


    def move_right(self): # permettre de déplacer la bouée dans la direction demandée avec les flèches
        self.rect.x += self.velocity

    def move_left(self): # permettre de déplacer la bouée dans la direction demandée avec les flèches
        self.rect.x -= self.velocity

    def move_up(self): # permettre de déplacer la bouée dans la direction demandée avec les flèches
        self.rect.y -= self.velocity

    def move_down(self): # permettre de déplacer la bouée dans la direction demandée avec les flèches
        self.rect.y += self.velocity
