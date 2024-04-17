import joueur
import random


class Partie:

  def __init__(self, nb_joueurs):
    self.nb_joueurs = nb_joueurs
    self.tab_joueurs = []
    self.partie_finie = False
    # 1 pour partie finie, 0 pour partie en cours

    self.manche_finie = False
    self.score = []

  def fin_partie(self):  #test si la partie est finie
    for element in self.score:
      if element >= 100:
        self.partie_finie = True

  def ajouter_joueur(self, J):
    self.tab_joueurs.append(J)

  def fin_manche(self, J):
    #J est un joueur on testera s'il a retourné tt ses cartes ou non
    i = 0
    self.manche_finie = True
    while (self.manche_finie and i < 3):
      j = 0
      while (j < 4 and self.manche_finie):
        if J.jeu_actuel[i][j].etat == "ouverte":
          self.manche_finie = False
        j += 1
      i += 1

  


