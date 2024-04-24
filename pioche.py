import random
import carte
import pygame


class Pioche:

  def __init__(self,ecran):
    self.cartes = []
    #cartes de -1 à 12
    for i in range(-1, 13):
      for _ in range(10):
        c = carte.Carte(i,ecran)
        self.cartes.append(c)

    #cartes 0
    for _ in range(5):
      c = carte.Carte(0,ecran)
      self.cartes.append(c)

    #cartes -2
    for _ in range(5):
      c = carte.Carte(-2,ecran)
      self.cartes.append(c)

    self.taille = len(self.cartes)

  def affiche(self, ecran): 
    HAUTEUR = ecran.get_height()
    LARGEUR = ecran.get_width()

    ch = "images/cachee.png"
    img = pygame.image.load(ch)
    img = pygame.transform.scale(img, (self.cartes[0].largeur, self.cartes[0].hauteur))
    """
    for i in range(1, 10):
      decalage = i + 1
      ecran.blit(img, (HAUTEUR- 25 - 110 + decalage,
                       LARGEUR - 25 - 150 + i + 1))
    """
    ecran.blit(img, (LARGEUR - 30 - self.cartes[0].largeur, HAUTEUR - 30 - self.cartes[0].hauteur))
  
  def melange(self):
    random.shuffle(self.cartes)

  def est_vide(self, defausse):
    if len(self.cartes)==0:
      while len(defausse.cartes)>1:
        self.cartes.append(defausse.cartes.pop(1))

      self.melange()
