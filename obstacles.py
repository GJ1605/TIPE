import pygame
import random


#Représenter nos obstacles :
class Obstacles(pygame.sprite.Sprite):

    def __init__(self,largeur,hauteur):

        super().__init__()
        self.positionX = random.uniform(0, largeur) # donne une position en X
        self.positionY = random.uniform(0, int(hauteur*0.6)) # donne une position en Y
        self.obstacle = random.choice(['rocher', 'nageur']) # donne un obstacle aléatoirement

        if (self.obstacle == 'rocher') : # si l'obstacle est le rocher
            x = random.randint(60,80)
            self.image = pygame.image.load('assets/rocher.png')
            self.image = pygame.transform.scale(self.image, (x, x))
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.rect = self.image.get_rect() #récupérer la position
            self.rect.x = self.positionX
            self.rect.y = self.positionY
            
        if (self.obstacle == 'nageur') : # si l'obstacle est le rocher
            self.image = pygame.image.load('assets/nageur.png')
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.rect = self.image.get_rect() #récupérer la position
            self.rect.x = self.positionX
            self.rect.y = self.positionY
