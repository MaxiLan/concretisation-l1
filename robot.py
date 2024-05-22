import strategie_n1
import joueur
import pygame
class Robot(joueur.Joueur):

    def __init__(self,strategie,nom):
        super().__init__(nom)
        self.strategie=strategie #strategie est une classe 
        self.ind_carte_cachee=[]
        self.jeu_individuel= []

    def evol_carte_cachee(self):
        self.ind_carte_cachee=[]
        for i in range(3):
            for j in range(4):
                if self.jeu_actuel[i][j].etat!="ouverte" :
                    self.ind_carte_cachee.append([i,j])

    def choix_pioche_def(self,partie):
        ''' renvoie les coordonnées du click qu'il va faire'''
        coord=self.strategie.choix_pioche_def(self.jeu_actuel,partie)
        return coord

    def choix_placement_carte(self,carte,partie):
        coord=self.strategie.choix_placement_carte(self,carte,partie)
        return coord

    def retourne_hasard(self):
        coord=self.strategie.retourne_hasard(self)
        return coord

    def debut_manche(self,partie,ecran):
        pos=self.strategie.debut_manche(self)
        pygame.time.wait(500)
        self.jeu_actuel[pos[0]][pos[1]].etat = "ouverte"
        self.affiche_jeu(ecran)
        pygame.display.flip()
        return True
