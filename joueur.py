import pygame
import carte

class Joueur:

    def __init__(self, nom):
        self.jeu_actuel = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]
        self.nom = nom
        self.score_individuel = 0


    def debut_manche(self,partie,ecran):
        click=False
        h = partie.pioche.cartes[0].hauteur
        l = partie.pioche.cartes[0].largeur
        ecart = ecran.get_width()//2 - 2*l - 30
        pygame.event.get()
        s = pygame.mouse.get_pressed()
        if s[0]:
            pos = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(4):
                    if (ecart + j * l+j*20< pos[0] < ecart + j * l+j*20 + l) and (60 + i * h+i*15< pos[1] <  60 + i * h+i*15 + h):
                        if self.jeu_actuel[i][j].etat != "ouverte":
                            self.jeu_actuel[i][j].etat = "ouverte"
                            self.affiche_jeu(ecran)
                            pygame.display.flip()
                            click = True
        return click
        
         
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


    def affiche_petit(self, ecran, cote):
        """
        Affiche le jeu du joueur en petit 
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