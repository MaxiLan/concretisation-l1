import joueur
import random
import pioche
import defausse
import pygame


class Partie:

    def __init__(self, nb_joueurs, ecran,robot=0):
        self.nb_joueurs = nb_joueurs
        self.tab_joueurs = []
        self.pioche = pioche.Pioche(ecran)
        self.defausse = defausse.Defausse(ecran)
        self.carte_en_main="images/carte_selectionnee.png"
        self.manche_finie = False
        self.robot=robot
        self.score = [0 for _ in range(nb_joueurs)]


    def fin_partie(self):
        """
        Renvoie vrai si la partie est fini i.e. un joueur a atteint 100 points
        Renvoie faux sinon
        """
        result =False
        for element in self.score:
            if element >= 100:
                result=True
        return result
    
    def mise_a_jour_score(self):
        """
        Met à jour les scores après une manche
        """
        for i in range (len(self.tab_joueurs)):
            self.score[i] += self.tab_joueurs[i].score_individuel

      
    def ajouter_joueur(self, J):
        """
        Ajoute des joueurs à la partie
        """
        self.tab_joueurs.append(J)


def verifie_fermeture():
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
