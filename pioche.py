import random
import carte
import pygame


class Pioche:

    def __init__(self,ecran):
        HAUTEUR = ecran.get_height()
        LARGEUR = ecran.get_width()
        facteur = HAUTEUR/850
        h=160 * facteur
        l=110 * facteur
        self.cartes = []
        self.ord= HAUTEUR-30-h
        #self.abs= LARGEUR-30-l
        self.abs = LARGEUR//2 + l//2 + 20
        

    def rempli(self, ecran):
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

                
    def vide(self):
        self.cartes.clear()


    def affiche(self, ecran): 
        HAUTEUR = ecran.get_height()
        LARGEUR = ecran.get_width()

        ch = "images/cachee.png"
        img = pygame.image.load(ch)
        img = pygame.transform.scale(img, (self.cartes[0].largeur, self.cartes[0].hauteur))

        #ecran.blit(img, (LARGEUR - 30 - self.cartes[0].largeur, HAUTEUR - 30 - self.cartes[0].hauteur))
        ecran.blit(img, (self.abs, self.ord))

  
    def melange(self):
        random.shuffle(self.cartes)


    def est_vide(self, defausse):
        if len(self.cartes)==0:
            while len(defausse.cartes)>1:
                self.cartes.append(defausse.cartes.pop(1))

        self.melange()