import pygame #pour utiliser pygame
from game import Game
from autobaignade import AutoBaignade
import math
pygame.init()



            # generer la fenetre du jeu

pygame.display.set_caption("Bouée EMILY 2.0")
info = pygame.display.Info() # on récupère la largeur et la hauteur de l'écran


            # récupérer la taille de l'écran pour adapter la taille de la fenêtre à tous les écrans
    
hauteur = (info.current_h-100)
largeur = int(info.current_h*100/84)


            # créer la fenêtre (taille)
    
screen = pygame.display.set_mode((largeur, hauteur))


            # changer l'arriere plan du  jeu
    
background = pygame.image.load('assets/plage.jfif')
background = pygame.transform.scale(background,(largeur, hauteur))


            # générer la banière de début du jeu avec le bouton play

        # bannière de début du jeu
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner,(int(largeur/2),int(largeur/6)))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(largeur/4)
banner_rect.y = math.ceil(hauteur/4)

        # bouton play
play_button = pygame.image.load('assets/button.jfif')
play_button = pygame.transform.scale(play_button, (int(largeur/3), int(largeur/8)))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(largeur/3)
play_button_rect.y = math.ceil(banner_rect.y + largeur/6 + 20)


            # charger le début du jeu et les événements aléatoires associés

        # charger le jeu (plateau, bouée etc)

game = Game(largeur, hauteur, screen)


running = True


while running: # faire tourner le programme tant que le joueur ne l'a pas quitté
    jeu = 0 # booléen rendant compte du commencement du jeu

    screen.blit(background, (0,0)) #création de l'arrière plan de la fenêtre
    
    if game.is_playing: #si on a cliqué sur le bouton play et démarré le jeu

        jeu = 1 # le jeu a bien commencé
        game.update(screen, largeur, hauteur, jeu, background) #on affiche tous les éléments nécessaires au jeu

        if game.autorisation.color == 'green' : #si le drapeau de baignade est vert, on peut maintenant créer et afficher le bouton d'urgence de la bouée
            urgence_button = pygame.image.load('assets/button.png')
            urgence_button = pygame.transform.scale(urgence_button,(80,80))
            urgence_button_rect = urgence_button.get_rect()
            urgence_button_rect.x = largeur*0.88
            urgence_button_rect.y = hauteur*0.02
            screen.blit(urgence_button,urgence_button_rect) # affiche le bouton

    else: # si on ne l'a pas fait, alors on affiche le bouton play
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    pygame.display.flip() #mettre à jour l'écran

    
    for event in pygame.event.get(): # gestion des événements de la souris ou du clavier
        
        if event.type == pygame.QUIT: # le joueur a fermé la fenetre :
            running = False
            pygame.quit()
            
                #detecter si un joueur lache une touche du clavier
                
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True #touche active
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # si le joueur clique quelque part
            #vérifier si la souris est en collision avec le bouton "play" :
            
            if play_button_rect.collidepoint(event.pos):
                game.is_playing = True # lancer le jeu

            if game.autorisation.color == 'green': # uniquement lorsque le drapeau est vert (sinon le bouton n'existe pas)
                if (jeu == 1) : #si on a lancé le jeu et donc initialisé le bouton d'urgence (donc après avoir cliqué sur "play")
                    if urgence_button_rect.collidepoint(event.pos): # le joueur clique sur le bouton d'urgence
                        game.playing(largeur, hauteur, screen, background) #renvoyer la bouée sur la plage
