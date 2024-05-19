import pygame

class Carte:
  
    def __init__(self, numero, ecran):
        HAUTEUR = ecran.get_height()
        LARGEUR = ecran.get_width()
        facteur = HAUTEUR/850
        self.etat = "cachee" 
        self.num = numero 
        self.hauteur=160 * facteur
        self.largeur=110 * facteur


def cacher_carte(ecran, partie):
    """
    Recouvre l'emplacement "carte en main"
    """
    x = ecran.get_width()//2 - partie.pioche.cartes[0].largeur//2
    y = ecran.get_height() - partie.pioche.cartes[0].hauteur - 60
    img = pygame.image.load(partie.carte_en_main)
    img = pygame.transform.scale(img, (partie.pioche.cartes[0].largeur, partie.pioche.cartes[0].hauteur))
    ecran.blit(img, (x, y))
    
