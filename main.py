import pygame
import carte
import joueur
import partie
import pioche
import defausse
import click
import manche
import accueil

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


nb_joueurs = accueil.affiche_accueil(ecran)

partie = partie.Partie(nb_joueurs)

for i in range(nb_joueurs):
  J = joueur.Joueur(i + 1)
  partie.tab_joueurs.append(J)


p = pioche.Pioche(ecran)
d = defausse.Defausse()
while not fin_partie:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      fin_partie = True

  manche.manche(partie.tab_joueurs, p, d, ecran)
  partie.mise_a_jour_score()
  fin_partie = partie.fin_partie()
  

pygame.quit()
