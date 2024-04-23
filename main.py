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


# nb_joueurs = int(input("Combien de joueurs voulez vous ? "))
nb_joueurs = 2 # TEST

partie = partie.Partie(nb_joueurs)

for i in range(nb_joueurs):
  J = joueur.Joueur(i + 1)
  partie.tab_joueurs.append(J)


#INIT ECRAN
HAUTEUR =  950
LARGEUR =  1050
pygame.init()
clock = pygame.time.Clock()
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
ecran.fill("grey24")
#INIT ECRAN

p = pioche.Pioche(ecran)
d = defausse.Defausse()
while not fin_partie:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      fin_partie = True

  manche.manche(partie.tab_joueurs, p, d, ecran)
  #manche.affiche_fin_manche()
  #ecran.fill("grey24")
  #pygame.display.flip()
  partie.mise_a_jour_score()
  print(partie.score)
  #fin_partie = partie.fin_partie()
  

pygame.quit()
