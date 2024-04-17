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
    ch = "images/cachee.png"
    img = pygame.image.load(ch)
    img = pygame.transform.scale(img, (110, 150))
    for i in range(1, 10):
      decalage = i + 1
      ecran.blit(img, (ecran.get_width() - 25 - 110 + decalage,
                       ecran.get_height() - 25 - 150 + i + 1))

    ecran.blit(img,
               (ecran.get_width() - 25 - 110, ecran.get_height() - 25 - 150))

  def melange(self):
    random.shuffle(self.cartes)
