import pygame
import carte
import joueur
import partie
import pioche
import defausse
import click
import manche

#variables intiales
fin_partie = False

p = pioche.Pioche()
d = defausse.Defausse()

# nb_joueurs = int(input("Combien de joueurs voulez vous ? "))
nb_joueurs = 2

partie = partie.Partie(nb_joueurs)

for i in range(nb_joueurs):
  J = joueur.Joueur(i + 1)
  partie.tab_joueurs.append(J)


#INIT ECRAN
HAUTEUR =  750
LARGEUR =  850
pygame.init()
clock = pygame.time.Clock()
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
ecran.fill("grey24")
#INIT ECRAN

while not fin_partie:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      fin_partie = True

  manche.manche(partie.tab_joueurs, p, d, ecran)
  
  partie.fin_partie()
  fin_partie = partie.partie_finie
  

pygame.quit()
