import random
import pygame
import carte


class Defausse:

  def __init__(self):
    self.cartes = []

  def affiche(self, ecran):
    ch = "images/" + str(self.cartes[-1].num) + ".png"
    img = pygame.image.load(ch)
    img = pygame.transform.scale(img, (110, 150))
    ecran.blit(img, (ecran.get_width() - 270, ecran.get_height() - 175))

  def ajout_carte(self, carte):
    self.cartes.append(carte)
  
    
  def retire_carte(self):
    return self.cartes.pop()
