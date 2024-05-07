import robot
import random
class Strategie_n1:
    ''' 
        ne prends pas les cartes au dessus égales à 7
        pioche ou defausse :
        defausse si on peut avancer une colonne sup a 0 ou si carte <=0
        pioche sinon. 
            si carte valide
                on la met dans une colonne 
            sinon on retourne une carte du jeu
    '''

    def carte_valide(self,c):
        # carte en dessous de 7
        if c.num>= 7:
            return False
        else :
            return True

    def carte_a_suppr(self,joueur):
            joueur.carte_a_suppr=[]
            for i in range (3):
                for j in range(4):
                    if joueur.jeu_actuel[i][j].num!="42bis":
                        if joueur.jeu_actuel[i][j].etat=="ouverte" and not self.carte_valide(joueur.jeu_actuel[i][j]):
                            joueur.carte_a_suppr.append(joueur.jeu_actuel[i][j].num)


    def choix_pioche_def(self,jeu_actuel,partie):
        d=partie.defausse.cartes[-1]
        coords=[partie.pioche.abs,partie.pioche.ord]
        if self.carte_valide(d):
            if d.num<=0:
                coords=[partie.defausse.abs,partie.defausse.ord]
                return coords
            else:
                for j in range(4):
                    if jeu_actuel[0][j].num==d.num or jeu_actuel[1][j].num==d.num or jeu_actuel[2][j].num==d.num:
                        coords=[partie.defausse.abs,partie.defausse.ord]
                        return coords
        
        return coords

    def colonne_en_cours(self,jeu_actuel,j):
        if jeu_actuel[0][j].etat=="ouverte" and ( (jeu_actuel[0][j].num==jeu_actuel[1][j].num and jeu_actuel[1][j].etat=="ouverte") or (jeu_actuel[0][j].num==jeu_actuel[2][j].num and jeu_actuel[2][j].etat=="ouverte") ):
            return jeu_actuel[0][j].num
        elif jeu_actuel[2][j].etat=="ouverte" and ( (jeu_actuel[2][j].num==jeu_actuel[1][j].num and jeu_actuel[1][j].etat=="ouverte") or (jeu_actuel[0][j].num==jeu_actuel[2][j].num and jeu_actuel[0][j].etat=="ouverte") ):
            return jeu_actuel[1][j].num
        else :
            return 12
    def etude_colonne(self,jeu_actuel,colonne,carte):
        '''appelée si une carte est de la meme valeur dans la colonne
        on va alors chercher ou mettre cette derniere et renvoyer les indices impliqués
        '''
        compte_neg=0
        max=-4
        ind_max=-1
        for i in range(3):
            if jeu_actuel[i][colonne].etat=="ouverte":
                if self.colonne_en_cours(jeu_actuel,colonne)>=carte.num:
                    if jeu_actuel[i][colonne].num==carte.num and carte.num<=0:
                        compte_neg+=1
                    if jeu_actuel[i][colonne].num>max and jeu_actuel[i][colonne].num!=carte.num :
                        ind_max=i
                        max=jeu_actuel[i][colonne].num
            elif max==-4:
                max=-3
                ind_max=i
        if compte_neg==2:
            return -1
        else:
            return ind_max

    def choix_placement_carte(self,joueur,carte,partie): #joueur est de type robot
            '''
        va choisir l'endroit où envoyer la carte dans le jeu qu'elle vienne
        de la pioche ou de la defausse.
        '''
        #if not self.fin_partie(joueur):
            indice_coord_carte=[]
            self.carte_a_suppr(joueur)
            if not self.carte_valide(carte): #si la carte est pas valide on la met dans la defausse
                coord=[-1,-1]
                return coord
        
            else:#sinon plusieurs options
                for i in range (3):#tests des colonnes/avancée des colonnes
                    for j in range(4):
                        if joueur.jeu_actuel[i][j].etat=="ouverte" and joueur.jeu_actuel[i][j].num==carte.num:  
                                ligne=self.etude_colonne(joueur.jeu_actuel,j,carte)
                                coord=[ligne,j]
                                if ligne!=-1:
                                    return coord

                #y a t'il des cartes qui ne sont pas valides dans notre jeu actuel ?           
                if len(joueur.carte_a_suppr)!=0:
                    for i in range(3):
                        for j in range(4):
                            if joueur.jeu_actuel[i][j].num==joueur.carte_a_suppr[0] and joueur.jeu_actuel[i][j].etat=="ouverte":
                                joueur.carte_a_suppr.pop(0)
                                coord=[i,j]
                                return coord #alors on retourne les indices de la carte a supprimer


                choix_carte=random.randint(0,len(joueur.ind_carte_cachee)-1) 
                coord=[joueur.ind_carte_cachee[choix_carte][0],joueur.ind_carte_cachee[choix_carte][1]]
                return coord 

        # else:
        #     joueur.evol(score)
        #     for J in partie.tab_joueurs:
        #         fact_carte_cachee=0
        #         J.evol_score()
        #         for i in range (3):
        #             for j in range(4):
        #                 if J.jeu_actuel[i][j].etat=="cachee":
        #                     fact_carte_cachee+=5
        #         J.score_actuel+=fact_carte_cachee
        #         if not J.score_actuel<= joueur.score_actuel:
                    




            
    def retourne_hasard(self,joueur):
            choix_carte=random.randint(0,len(joueur.ind_carte_cachee)-1) 
            coord=[joueur.ind_carte_cachee[choix_carte][0],joueur.ind_carte_cachee[choix_carte][1]]
            return  coord

    def retourne_carte(self,joueur):
            coord=[]
            for i in range(3):
                    if joueur.jeu_actuel[len(joueur.jeu_actuel)-1-i][len(joueur.jeu_actuel[0])-1].etat!="ouverte":
                        coord=[len(joueur.jeu_actuel)-1-i,len(joueur.jeu_actuel[0])-1]
                        return coord

        
