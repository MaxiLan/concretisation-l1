import random
import pygame
import carte


class Defausse:

  def __init__(self):
    self.cartes = []

  def affiche(self, ecran):
    HAUTEUR = ecran.get_height()
    LARGEUR = ecran.get_width()
    facteur = HAUTEUR/850
    h_carte = 160 * facteur
    l_carte = 110 * facteur

    ch = "images/" + str(self.cartes[-1].num) + ".png"
    img = pygame.image.load(ch)
    img = pygame.transform.scale(img, (l_carte, h_carte))
    ecran.blit(img, (LARGEUR - 30 - 20 - 2*l_carte, HAUTEUR - h_carte - 30))

  def ajout_carte(self, carte):
    self.cartes.append(carte)
  
    
  def retire_carte(self):
    return self.cartes.pop()
