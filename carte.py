import pygame

class Carte:
  
  def __init__(self, numero, ecran):
    HAUTEUR = ecran.get_height()
    LARGEUR = ecran.get_width()
    facteur = HAUTEUR/850
    self.etat = "cachee"  #ouverte cachée ou invisible =(colonne disparue)
    self.num = numero  #numéro de carte
    self.hauteur=160 * facteur
    self.largeur=110 * facteur


def cacher_carte(ecran, partie):
  """
  Recouvre l'emplacement "carte en main"
  """
  x = ecran.get_width() - 40 - partie.pioche.cartes[0].largeur - partie.pioche.cartes[0].largeur//2
  y = ecran.get_height() - 50 - 2 * partie.pioche.cartes[0].hauteur
  img = pygame.image.load(partie.carte_en_main)
  img = pygame.transform.scale(img, (partie.pioche.cartes[0].largeur, partie.pioche.cartes[0].hauteur))
  ecran.blit(img, (x, y))
  
