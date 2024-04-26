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

partie = partie.Partie(nb_joueurs, ecran)

for i in range(nb_joueurs):
  J = joueur.Joueur(i + 1)
  partie.tab_joueurs.append(J)


while not fin_partie:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      fin_partie = True

  continuer = manche.manche(partie, ecran)
  partie.mise_a_jour_score()
  fin_partie = partie.fin_partie() and continuer
  

pygame.quit()
