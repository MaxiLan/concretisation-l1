import pygame


class Joueur:

  def __init__(self, nom):
    self.jeu_actuel = [[], [], []]
    self.nom = nom
    self.score_individuel = 0  #score de chaque joueur

  def evol_score(self):
    #pour faire évoluer les scores de chaque joueur
    for i in range(3):
      for j in range(4):
        self.score_individuel += self.jeu_actuel[i][j].num

  def affiche_jeu(self, ecran):
    for i in range(3):
      for j in range(4):
        if (self.jeu_actuel[i][j].etat == "cachee"):
          ch = "images/cachee.png"
        else:
          ch = "images/" + str(self.jeu_actuel[i][j].num) + ".png"
        img = pygame.image.load(ch)
        img = pygame.transform.scale(img, (110, 160))
        ecran.blit(img, (25 + j * 130, 30 + i * 175))
