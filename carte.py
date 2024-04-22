import pygame

class Carte:
  def __init__(self, numero):
    self.etat = "cachee"  #ouverte cachée ou invisible =(colonne disparue)
    self.num = numero  #numéro de carte

  def affiche(self):  #affichage d'une carte
    print(self.num)

def cacher_carte(ecran):
  HAUTEUR = ecran.get_height()
  LARGEUR = ecran.get_width()
  facteur = HAUTEUR/850
  h_carte = 160 * facteur
  l_carte = 110 * facteur
  x = LARGEUR - 30 - l_carte - 10 - l_carte//2
  y = HAUTEUR - 30 - 20 - 2 * h_carte
  img = pygame.image.load("images/carte_selectionnee.png")
  img = pygame.transform.scale(img, (l_carte, h_carte))
  ecran.blit(img, (x, y))
