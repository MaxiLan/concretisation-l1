import pygame

class Carte:

  def __init__(self, numero):
    self.etat = "cachee"  #ouverte cachée ou invisible =(colonne disparue)
    self.num = numero  #numéro de carte

  def affiche(self):  #affichage d'une carte
    print(self.num)

def cacher_carte(ecran):
  img = pygame.image.load("images/carte_selectionnee.png")
  img = pygame.transform.scale(img, (110, 160))
  ecran.blit(img, (715, 375))
