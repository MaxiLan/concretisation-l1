import pygame
import carte
import joueur
import partie as P
import pioche
import defausse
import click
import manche
import accueil
import strategie_n1
import robot
import strategie_n0


relance_partie = True

while relance_partie:
    fin_partie = False

    HAUTEUR = 1080
    LARGEUR = 1920
    pygame.init()
    clock = pygame.time.Clock()
    ecran = pygame.display.set_mode((LARGEUR, HAUTEUR), pygame.FULLSCREEN)
    pygame.display.set_caption("SKYJO")
    ecran.fill('#EEE2DE')

    #on récupère le nombre de joueurs/robots sur l'accueil
    nb_joueurs, nb_robots, niveau = accueil.affiche_accueil(ecran)
    partie = P.Partie(nb_joueurs, ecran)

    for i in range(nb_robots):
        if niveau==1:
            S=strategie_n0.Strategie_aleatoire()
        elif niveau==2:
            S=strategie_n1.Strategie_n1()
        R=robot.Robot(S,i+1)
        partie.tab_joueurs.append(R)


    for i in range (nb_robots, nb_joueurs):
        J = joueur.Joueur(i + 1)
        partie.tab_joueurs.append(J)


    while not fin_partie:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin_partie = True

        relance_partie, fin_partie = manche.manche(partie, ecran)

    pygame.quit()