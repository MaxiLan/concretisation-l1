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

    pygame.display.init()
    pygame.font.init()
    pygame.display.set_icon(pygame.image.load("images/icon.png"))
    clock = pygame.time.Clock()


    plein_ecran = input("Voulez-vous jouer en plein écran ? (0/N) : ")
    
    if plein_ecran=='o' or plein_ecran=='O':
        ecran = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    else:
        HAUTEUR = max(1000, int(input("Hauteur de la fenêtre (min 1000)")))
        LARGEUR = max(1500, int(input("Largeur de la fenêtre (min 1500)")))
        ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))

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