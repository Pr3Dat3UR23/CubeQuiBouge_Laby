### BIBLIOTHEQUES & MODULES
import pygame
import os
import mazescan
import game
import random

### Initialisation de la fenêtre pygame
pygame.init()
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption("Cubequibouge")

###Chargement des ressources

#Chargement des images de labyrinthes
maze_files = [f for f in os.listdir('images/MAZE') if f.endswith('.png')]

#Range les chemins d'accès dans une liste maze
maze = {}
for i, f in enumerate(maze_files):
    maze_path = os.path.join('images/MAZE', f)
    maze[i] = mazescan.scan(maze_path)

mazemap=maze[random.randint(0,len(maze)-1)]
mazescan.create_xml_file(mazemap)

#Chargement des images de boutons & fond de la page d'accueil
background = pygame.transform.scale(pygame.image.load("images/lobby (Dall-E).png"), screen.get_size())
play = pygame.transform.scale(pygame.image.load("images/play.png"), (200,150))

#Créations de zones cliquables sous forme de Rect pour simplifier la gestion des collisions avec les images des boutons et régler leur position (en prenant le centre du rectangle)
play_rect = play.get_rect()
play_rect.topleft =(SCREEN_HEIGHT/2-100, (SCREEN_WIDTH/3)*2)

###Boucle principale
running = True
while running:
    #Récupération des évènements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
        #on récupère les clics de la souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_rect.collidepoint(event.pos):
                play = pygame.transform.scale(pygame.image.load("images/play_off.png"), (200,150))
                running = False
                #lancement du jeu
                game.start(screen, mazemap)

    #Affichages
    screen.blit(background, (0, 0))
    screen.blit(play, play_rect)
    pygame.display.flip()

#fermeture de pygame
pygame.quit()