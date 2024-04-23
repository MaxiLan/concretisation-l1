import pygame
import carte
class Joueur:

  def __init__(self, nom):
    self.jeu_actuel = [[], [], []]
    self.nom = nom
    self.score_individuel = 0  #score de chaque joueur

  def evol_score(self):
    #pour faire évoluer les scores de chaque joueur
    for i in range(3):
      for j in range(4):
        if  str (self.jeu_actuel[i][j].num) != "42bis" :
          self.score_individuel += self.jeu_actuel[i][j].num

  def retrait_colonne(self,defausse,ecran):
    for j in range(4):
      if self.jeu_actuel[0][j].num==self.jeu_actuel[1][j].num and self.jeu_actuel[1][j].num==self.jeu_actuel[2][j].num:
         if self.jeu_actuel[1][j].num!="42bis" and self.jeu_actuel[1][j].etat=="ouverte" and self.jeu_actuel[2][j].etat=="ouverte" and self.jeu_actuel[0][j].etat=="ouverte":  
          for i in range(3):
              c=carte.Carte("42bis",ecran)
              c.etat="ouverte"

              #ajouter les cartes de la colonne dans la defausse
              c_ajout_defausse=self.jeu_actuel[i][j]
              defausse.cartes.append(c_ajout_defausse)
              self.jeu_actuel[i][j]=c

  def affiche_jeu(self, ecran):
    HAUTEUR = ecran.get_height()
    LARGEUR = ecran.get_width()
    for i in range(3):
      for j in range(4):
        if (self.jeu_actuel[i][j].etat == "cachee"):
          ch = "images/cachee.png"
        else:
          ch = "images/" + str(self.jeu_actuel[i][j].num) + ".png"
        img = pygame.image.load(ch)
        img = pygame.transform.scale(img, (self.jeu_actuel[i][j].largeur, self.jeu_actuel[i][j].hauteur))
        ecran.blit(img, (30 + j * self.jeu_actuel[i][j].largeur+j*20, 30 + i * self.jeu_actuel[i][j].hauteur +i*20))


