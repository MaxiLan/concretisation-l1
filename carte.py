import pygame

class Carte:
  
  def __init__(self, numero,ecran):
    HAUTEUR = ecran.get_height()
    LARGEUR = ecran.get_width()
    facteur = HAUTEUR/850
    self.etat = "cachee"  #ouverte cachée ou invisible =(colonne disparue)
    self.num = numero  #numéro de carte
    self.hauteur=160 * facteur
    self.largeur=110 * facteur

  def affiche(self):  #affichage d'une carte
    print(self.num)

def cacher_carte(ecran,carte):
  x = ecran.get_width() - 40 - carte.largeur - carte.largeur//2
  y = ecran.get_height() - 50 - 2 * carte.hauteur
  img = pygame.image.load("images/carte_selectionnee.png")
  img = pygame.transform.scale(img, (carte.largeur, carte.hauteur))
  ecran.blit(img, (x, y))
