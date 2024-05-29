import pygame
import partie as P
import manche
import accueil
import strategie_n1
import robot
import joueur
import strategie_n0
import asyncio
import sys
import platform


async def main():
    relance_partie = True

    while relance_partie:
        fin_partie = False

        HAUTEUR=1000
        LARGEUR=1500
        pygame.init()
        clock = pygame.time.Clock()

        ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
        pygame.display.set_caption("SKYJO")
        ecran.fill('#EEE2DE')

        #on récupère le nombre de joueurs/robots sur l'accueil
        nb_joueurs, nb_robots, niveau = await accueil.affiche_accueil(ecran)
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

            #permet de changer de couleur si le jeu est lancé dans un navigateur
            if sys.platform=="emscripten":
                platform.document.body.style.background="#3d3d3d"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin_partie = True
            
            relance_partie, fin_partie = await manche.manche(partie, ecran)
            
            await asyncio.sleep(0)

        await asyncio.sleep(0)
        pygame.quit()

asyncio.run(main())
