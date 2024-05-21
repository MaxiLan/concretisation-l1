import random
import pygame
import carte


class Defausse:

    def __init__(self,ecran):
        HAUTEUR = ecran.get_height()
        LARGEUR = ecran.get_width()
        facteur = HAUTEUR/850
        h=160 * facteur
        l=110 * facteur
        self.cartes = []
        self.ord= HAUTEUR-30-h
        self.abs= LARGEUR//2 - l - l//2 - 20


    def affiche(self, ecran):
        """
        Affiche la défausse
        """
        HAUTEUR = ecran.get_height()
        LARGEUR = ecran.get_width()
        ch = "images/" + str(self.cartes[-1].num) + ".png"
        img = pygame.image.load(ch)
        img = pygame.transform.scale(img, (self.cartes[0].largeur, self.cartes[0].hauteur))
        ecran.blit(img, (self.abs, self.ord))


    def ajout_carte(self, carte):
        """
        Ajoute une carte à la défausse
        """
        self.cartes.append(carte)
    
    
    def retire_carte(self):
        """
        Retire une carte de la défausse
        """
        return self.cartes.pop()