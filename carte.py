import pygame

class Carte:

  def __init__(self, numero):
    self.etat = "cachee"  #ouverte cachée ou invisible =(colonne disparue)
    self.num = numero  #numéro de carte

  def affiche(self):  #affichage d'une carte
    print(self.num)

def cacher_carte(ecran, carte):
  img = pygame.image.load("images/42bis.png")
  img = pygame.transform.scale(img, (110, 160))

  if carte=="pioche":
    ecran.blit(img, (715, 375))
  else:
    ecran.blit(img, (580, 375))

