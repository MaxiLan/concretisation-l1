import joueur
import random


class Partie:
  def __init__(self, nb_joueurs):
    self.nb_joueurs = nb_joueurs
    self.tab_joueurs = []
    # 1 pour partie finie, 0 pour partie en cours

    self.manche_finie = False
    self.score = []

  def fin_partie(self):  #test si la partie est finie
    result =False
    for element in self.score:
      if element >= 100:
        result=True
    return result
    
  def mise_a_jour_score(self):
    for i in range (len(self.tab_joueurs)):
      self.score.append(self.tab_joueurs[i].score_individuel)

      
  def ajouter_joueur(self, J):
    self.tab_joueurs.append(J)

  

