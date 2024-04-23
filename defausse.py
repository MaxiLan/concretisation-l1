import random
import pygame
import carte


class Defausse:
  def __init__(self):
    self.cartes = []

  def affiche(self, ecran):
    HAUTEUR = ecran.get_height()
    LARGEUR = ecran.get_width()
    ch = "images/" + str(self.cartes[-1].num) + ".png"
    img = pygame.image.load(ch)
    img = pygame.transform.scale(img, (self.cartes[0].largeur, self.cartes[0].hauteur))
    ecran.blit(img, (LARGEUR - 50 - 2*self.cartes[0].largeur, HAUTEUR - self.cartes[0].hauteur - 30))

  def ajout_carte(self, carte):
    self.cartes.append(carte)
    
  
  def retire_carte(self):
    return self.cartes.pop()
