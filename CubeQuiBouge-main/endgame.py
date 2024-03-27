import pygame

def win(screen):
    screen_width, screen_height = screen.get_size()
    leave = pygame.transform.scale(pygame.image.load("images/quitter.png"), (45,45))
    background = pygame.transform.scale(pygame.image.load("images/lobby (Dall-E).png"), screen.get_size())
    font = pygame.font.SysFont('bold', 60)
    fin = font.render('fin', True, (255, 255, 255))
    #Créations de zones cliquables sous forme de Rect pour simplifier la gestion des collisions avec les images des boutons et régler leur position (en prenant le centre du rectangle)
    leave_rect = leave.get_rect()
    leave_rect.topleft = (screen_width-75, 25)

    ###Boucle principale
    running = True
    while running:
        #Récupération des évènements
        for event in pygame.event.get():
            #on récupère les clics de la souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                #collisions avec les rectangles
                if leave_rect.collidepoint(event.pos):
                    leave = pygame.transform.scale(pygame.image.load("images/quitter.png"), (45,45))
                    #sortie de la boucle
                    exit()
        #Affichages
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen,(0,0,0),pygame.Rect(screen_width/2-100,screen_height/3-50,250,150))
        screen.blit(leave, leave_rect)
        screen.blit(fin, (screen_width/2, screen_height/3))
        pygame.display.flip()
