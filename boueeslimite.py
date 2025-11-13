import pygame
import random

class BoueesLimite(pygame.sprite.Sprite): # chargement des bouées de signalisation de baignade

    def __init__(self):
        super().__init__()
        self.color = random.choice(['blue', 'yellow'])
        y = random.randint(0,120)

        if (self.color == 'blue'): #affiche les bouées bleues selon la position choisie par y (aléatoire)
            self.image = pygame.image.load('assets/boueeslimitebleue.png')
            self.rect = self.image.get_rect()
            self.height = self.image.get_height()
            self.rect.x = 0
            self.rect.y = y

        if (self.color == 'yellow'): #affiche les bouées jaunes selon la position choisie par y (aléatoire)
            self.image = pygame.image.load('assets/boueeslimitejaune.png')
            self.rect = self.image.get_rect()
            self.height = self.image.get_height()
            self.rect.x = 0
            self.rect.y = y
