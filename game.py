import pygame
from bouee import Bouee
from boueeslimite import BoueesLimite
from autobaignade import AutoBaignade
from obstacles import Obstacles
from warning import Warning
from urgence import Urgence

#Créer une classe qui va initialiser le jeu :
class Game :

    def __init__(self, largeur, hauteur, screen):
        #définir si notre jeu a commencé ou non
        self.is_playing = False #on initialise le jeu comme "pas commencé"
        self.bouee = Bouee(largeur, hauteur) #generer la bouée
        self.boueeslimite = BoueesLimite() #generer les bouées de limite de la zone baigneurs.
        self.obstacle = Obstacles(largeur,hauteur) #génère les obstacles
        self.autorisation = AutoBaignade(largeur, hauteur) #génère l'autorisation de baignade (ou non)
        self.warning = Warning() #générer le panneau de danger (collision avec un obstacle et/ou dépassement des bouées)
        self.ambulance = Urgence(hauteur) #générer l'ambulance en cas d'urgence
        self.pressed = {

        }


    def update(self, screen, largeur, hauteur, jeu, background): #pour changer le jeu lorsque l'on joue

                #affiche notre bouée :
        screen.blit(self.bouee.image,self.bouee.rect)

                # afficher le drapeau d'autorisation de la baignade :
        screen.blit(self.autorisation.image,self.autorisation.rect)

                #appliquer l'image de l'obstacles (nageur et rocher si le drapeau est vert, uniquement rocher sinon car baignade interdite):
        if ((self.autorisation.color == 'red') and (self.obstacle.obstacle == 'rocher')) or ((self.autorisation.color == 'orange') and (self.obstacle.obstacle == 'rocher')) or                 (self.autorisation.color == 'green') :
            screen.blit(self.obstacle.image,self.obstacle.rect)

                #positionner les bouées de limite de la zone baigneur :
        i = 0
        j = 0
        for i in range(largeur):
            if (i == j):
                screen.blit(self.boueeslimite.image,(i,self.boueeslimite.rect.y))
                j = j+100

                
                #écriture des indications de baignade :
                
        font = pygame.font.SysFont("monospace", 16)
        temperature_text = font.render(f"L'écart de température est de: {self.autorisation.ecarttemperature} °C et la force du vent est {self.autorisation.vent}.",1,(0,0,0))
        screen.blit(temperature_text,(20,20))

        
                #affichage de l'ambulance si besoin :
            
        screen.blit(self.ambulance.image, self.ambulance.ambulance_rect)

                #Vérifier où le joueur veut se diriger et l'empêcher de toucher les obstacles :

            #Aller à droite : (si on presse la flèche de droite + on ne dépasse pas du cadre de la fenêtre + si on ne se déplace pas au-dessus d'un obstacle)
        if (self.pressed.get(pygame.K_RIGHT) and (self.bouee.rect.x + self.bouee.width < largeur) and
        ( ((self.bouee.rect.x + self.bouee.width + 20 < self.obstacle.rect.x) or (self.bouee.rect.x > self.obstacle.rect.x + self.obstacle.width ))
        or ((self.bouee.rect.y + self.bouee.height + 20 < self.obstacle.rect.y) or (self.bouee.rect.y > self.obstacle.rect.y + self.obstacle.height + 20 )) ) ) :
            
            self.bouee.move_right()
            self.ambulance = Urgence(hauteur)
            

            #Aller à gauche : (si on presse la flèche de gauche + on ne dépasse pas du cadre de la fenêtre + si on ne se déplace pas au-dessus d'un obstacle)
        elif ( self.pressed.get(pygame.K_LEFT) and self.bouee.rect.x > 0 and ( ((self.bouee.rect.x + self.bouee.width < self.obstacle.rect.x) or (self.bouee.rect.x >                       self.obstacle.rect.x + self.obstacle.width + 20 )) or ((self.bouee.rect.y + self.bouee.height + 20 < self.obstacle.rect.y) or (self.bouee.rect.y > self.obstacle.rect.y +           self.obstacle.height + 20)) ) ):
            
            self.bouee.move_left()
            self.ambulance = Urgence(hauteur)

            #Aller en haut : (si on presse la flèche de haut + on ne dépasse pas du cadre de la fenêtre + si on ne se déplace pas au-dessus d'un obstacle + coordonnées bloquées lorsque le drapeau n'est pas vert)
        elif (self.pressed.get(pygame.K_UP) and self.bouee.rect.y > (self.boueeslimite.rect.y + self.boueeslimite.height) and self.autorisation.color == 'green' and (                     ((self.bouee.rect.y + self.bouee.height < self.obstacle.rect.y) or (self.bouee.rect.y > self.obstacle.rect.y + self.obstacle.height + 20 )) or ((self.bouee.rect.x +               self.bouee.width + 20 < self.obstacle.rect.x) or (self.bouee.rect.x > self.obstacle.rect.x + self.obstacle.width + 20)) ) ) or (self.pressed.get(pygame.K_UP) and                   self.bouee.rect.y > (hauteur*0.8) and self.autorisation.color != 'green'):
            self.bouee.move_up()
            self.ambulance = Urgence(hauteur)

            #Aller en bas : (si on presse la flèche de bas + on ne dépasse pas du cadre de la fenêtre + si on ne se déplace pas au-dessus d'un obstacle)
        elif ( self.pressed.get(pygame.K_DOWN) and self.bouee.rect.y + self.bouee.height < screen.get_height() and ( ((self.bouee.rect.y + self.bouee.height + 20 <                         self.obstacle.rect.y) or (self.bouee.rect.y > self.obstacle.rect.y + self.obstacle.height )) or ((self.bouee.rect.x + self.bouee.width + 20 < self.obstacle.rect.x) or             (self.bouee.rect.x > self.obstacle.rect.x + self.obstacle.width + 20)) ) ):
            self.bouee.move_down()
            self.ambulance = Urgence(hauteur)


                    #Messages d'attention si le joueur rencontre un problème :

        Probleme = False #on initialise le booléen pour signifier qu'il n'y a aucune collision
        FontWarning = pygame.font.SysFont("monospace", 16) #on charge la police et la taille du message

                #Création du message en fonction du problème :
            
        if self.bouee.rect.y < (self.boueeslimite.rect.y + self.boueeslimite.height + 20): #collision avec les bouées qu'on ne peut pas dépasser
            message = FontWarning.render("Ne pas dépasser les bouées",1,(0,0,0))
            positiony = hauteur*0.90
            Probleme = True

        elif (self.bouee.rect.y + self.bouee.height > self.obstacle.rect.y - 50) and (self.bouee.rect.y < self.obstacle.rect.y + self.obstacle.height + 50) and (self.bouee.rect.x         + self.bouee.width > self.obstacle.rect.x - 50) and (self.bouee.rect.x < self.obstacle.rect.x + self.obstacle.width + 50): #collision avec un obstacle, rocher ou nageur
            message = FontWarning.render("Attention à l'obstacle",1,(0,0,0))
            positiony = hauteur*0.90
            Probleme = True

        if Probleme == True : #quand il y a collision, on affiche l'image et le message
            width_message = message.get_width()
            positionx = int(largeur/2 - (width_message + 2*self.warning.width + 40)/2)
            screen.blit(self.warning.image,(positionx, positiony)) # générer panneau de gauche
            screen.blit(message,(positionx + self.warning.width + 20, positiony + int(self.warning.height/3) )) # générer le message
            screen.blit(self.warning.image,(positionx + self.warning.width + width_message + 40,positiony)) # générer panneau de droite

    def playing(self, largeur, hauteur, screen, background): #pour que la bouée retourne sur la plage si on appuie sur le bouton d'urgence

                    # ramener la bouée sur la plage
        while (self.bouee.rect.y < hauteur*0.9): # on ramène la bouée sur la plage
            screen.blit(background, self.bouee.rect, self.bouee.rect)   # effacer le dernière position de la bouée
            self.bouee.rect = self.bouee.rect.move(0, 20)   # déplacer la bouée
            screen.blit(self.bouee.image,self.bouee.rect)   # charger une nouvelle bouée
            pygame.display.flip()   # afficher le tout
            pygame.time.delay(100)  # faire une pause dans l'affichage pour voir la bouée se déplacer
        
            
                    # faire venir l'ambulance appelée directement par la bouée
        if ((self.bouee.rect.x - 50) < self.ambulance.ambulance_width) : # si l'ambulance ne peut pas venir de la gauche, on la fait venir de la droite
            self.ambulance.ambulance_rect.x = largeur + self.ambulance.ambulance_width # on modifie la position de l'ambulance pour qu'elle vienne de droite
            self.ambulance.image = pygame.transform.flip(self.ambulance.image, 1, 0) # on retourne l'image pour que l'ambulance arrive dans le bon sens
            
            while ((self.ambulance.ambulance_rect.x + self.ambulance.ambulance_width) > (self.bouee.rect.x + self.bouee.width + 125)):  # on déplace l'ambulance jusqu'à la bouée
                screen.blit(background, self.ambulance.ambulance_rect, self.ambulance.ambulance_rect)   # effacer la dernière position de l'ambulance
                self.ambulance.ambulance_rect = self.ambulance.ambulance_rect.move(-20, 0)   # déplacer l'ambulance
                screen.blit(self.ambulance.image, self.ambulance.ambulance_rect)    # charger une nouvelle ambulance
                pygame.display.flip()   # afficher le tout
                pygame.time.delay(100)  # faire une pause dans l'affichage pour voir la bouée se déplacer
                
        else: # si l'ambulance peut venir de la gauche
            
            while ((self.ambulance.ambulance_rect.x + self.ambulance.ambulance_width) < (self.bouee.rect.x - 50)):  # on déplace l'ambulance jusqu'à la bouée
                screen.blit(background, self.ambulance.ambulance_rect, self.ambulance.ambulance_rect)   # effacer la dernière position de l'ambulance
                self.ambulance.ambulance_rect = self.ambulance.ambulance_rect.move(20, 0)   # déplacer l'ambulance
                screen.blit(self.ambulance.image, self.ambulance.ambulance_rect)    # charger une nouvelle ambulance
                pygame.display.flip()   # afficher le tout
                pygame.time.delay(100)  # faire une pause dans l'affichage pour voir la bouée se déplacer