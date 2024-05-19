import pygame
import carte
class Joueur:

    def __init__(self, nom):
        self.jeu_actuel = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]
        self.nom = nom
        self.score_individuel = 0


    def evol_score(self):
        """
        Fait évoluer le score de chaque joueur
        """
        self.score_individuel=0
        for i in range(3):
            for j in range(4):
                if  str (self.jeu_actuel[i][j].num) != "42bis" and self.jeu_actuel[i][j].etat!="cachee":
                    self.score_individuel += self.jeu_actuel[i][j].num
          

    def retrait_colonne(self,defausse,ecran):
        """
        Retire une colonne si elle remplie du même nombre
        """
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
        """
        Affiche le jeu du joueur
        """
        HAUTEUR = ecran.get_height()
        LARGEUR = ecran.get_width()
        ecart = LARGEUR//2 - 2*self.jeu_actuel[0][0].largeur - 30

        for i in range(3):
            for j in range(4):
                if (self.jeu_actuel[i][j].etat == "cachee"):
                    ch = "images/cachee.png"
                else:
                    ch = "images/" + str(self.jeu_actuel[i][j].num) + ".png"
                img = pygame.image.load(ch)
                img = pygame.transform.scale(img, (self.jeu_actuel[i][j].largeur, self.jeu_actuel[i][j].hauteur))
                ecran.blit(img, (ecart + j * self.jeu_actuel[i][j].largeur+j*20, 60 + i * self.jeu_actuel[i][j].hauteur +i*20))


    def affiche_jeu_vision_ext(self,ecran):
        """
        Affiche le jeu des autres joueurs si la loupe est sélectionner
        """
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
                ecran.blit(img,(LARGEUR//4 + j * self.jeu_actuel[i][j].largeur+j*20-30, 130 + i * self.jeu_actuel[i][j].hauteur +i*20))

    
    def affiche_petit(self, ecran, cote):
        """
        Affiche le jeu du joueur
        """
        HAUTEUR = ecran.get_height()
        LARGEUR = ecran.get_width()

        if cote=='g':
            for i in range(3):
                for j in range(4):
                    if (self.jeu_actuel[i][j].etat == "cachee"):
                        ch = "images/cachee.png"
                    else:
                        ch = "images/" + str(self.jeu_actuel[i][j].num) + ".png"
                    img = pygame.image.load(ch)
                    img = pygame.transform.scale(img, (73, 106))
                    ecran.blit(img, (60 + j * 73+j*20, 200 + i * 106 +i*20))

        else:
            ecart = LARGEUR - 4*73-60 - 60
            for i in range(3):
                for j in range(4):
                    if (self.jeu_actuel[i][j].etat == "cachee"):
                        ch = "images/cachee.png"
                    else:
                        ch = "images/" + str(self.jeu_actuel[i][j].num) + ".png"
                    img = pygame.image.load(ch)
                    img = pygame.transform.scale(img, (73, 106))
                    ecran.blit(img, (ecart + j * 73+j*20, 200 + i * 106 +i*20))
