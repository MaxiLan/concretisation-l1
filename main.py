import pygame
import carte
import joueur
import partie
import pioche
import defausse
import click
import manche
import accueil
import strategie_n1
import robot
#variables intiales
fin_partie = False

#INIT ECRAN
HAUTEUR =  950
LARGEUR =  1050
pygame.init()
clock = pygame.time.Clock()
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("SKYJO")
ecran.fill("grey24")


nb_joueurs, nb_robots = accueil.affiche_accueil(ecran)
partie = partie.Partie(nb_joueurs, ecran)

for i in range(nb_robots):
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

  fin_partie = not manche.manche(partie, ecran)

  if partie.fin_partie():
    fin_partie = True
  

pygame.quit()
