import random
import carte
import pygame


class Pioche:

  def __init__(self):
    self.cartes = []
    #cartes de -1 à 12
    for i in range(-1, 13):
      for _ in range(10):
        c = carte.Carte(i)
        self.cartes.append(c)

    #cartes 0
    for _ in range(5):
      c = carte.Carte(0)
      self.cartes.append(c)

    #cartes -2
    for _ in range(5):
      c = carte.Carte(-2)
      self.cartes.append(c)

    self.taille = len(self.cartes)

  def affiche(self, ecran): 
    HAUTEUR = ecran.get_height()
    LARGEUR = ecran.get_width()
    facteur = HAUTEUR/850
    h_carte = 160 * facteur
    l_carte = 110 * facteur

    ch = "images/cachee.png"
    img = pygame.image.load(ch)
    img = pygame.transform.scale(img, (l_carte, h_carte))
    """
    for i in range(1, 10):
      decalage = i + 1
      ecran.blit(img, (HAUTEUR- 25 - 110 + decalage,
                       LARGEUR - 25 - 150 + i + 1))
    """
    ecran.blit(img, (LARGEUR - 30 - l_carte, HAUTEUR - 30 - h_carte))
  
  def melange(self):
    random.shuffle(self.cartes)
