import robot
import random
import manche
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
    def __init__(self):
        self.colonne_encours=[]

    def fin_partie(self,joueur,partie):
        for i in range (len(partie.tab_joueurs)):
            if manche.fin_manche(i,partie.tab_joueurs):
                return True
        return len(joueur.ind_carte_cachee)==1 
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
        ''' renvoie les coordonnées de la pioche ou de la defausse'''
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

    def num_colonne_en_cours(self,jeu_actuel,j):
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
                if self.num_colonne_en_cours(jeu_actuel,colonne)>=carte.num:
                    if jeu_actuel[i][colonne].num==carte.num and carte.num<=0:
                        compte_neg+=1
                        
                    if jeu_actuel[i][colonne].num>max and jeu_actuel[i][colonne].num!=carte.num :
                        ind_max=i
                        max=jeu_actuel[i][colonne].num
            elif max==-4:
                max=-3
                ind_max=i
        if compte_neg==1:
            return -1
        else:
            return ind_max

    def evol_colonne_encours(self,jeu_actuel):
        self.colonne_encours=[]
        for colonne in range(3):
            if (jeu_actuel[0][colonne].etat=="ouverte" and jeu_actuel[1][colonne].etat=="ouverte" and jeu_actuel[0][colonne].num==jeu_actuel[1][colonne].num) or (jeu_actuel[1][colonne].etat=="ouverte"  and jeu_actuel[2][colonne].etat=="ouverte" and jeu_actuel[1][colonne].num==jeu_actuel[2][colonne].num) or (jeu_actuel[0][colonne].etat=="ouverte"  and jeu_actuel[2][colonne].etat=="ouverte" and jeu_actuel[0][colonne].num==jeu_actuel[2][colonne].num):
                    self.colonne_encours.append(colonne)
                    
    def choix_placement_carte(self,joueur,carte,partie): #joueur est de type robot
            '''
        va choisir l'endroit où envoyer la carte dans le jeu qu'elle vienne
        de la pioche ou de la defausse.
        '''
            self.carte_a_suppr(joueur)
            if not self.carte_valide(carte) and not self.fin_partie(joueur,partie): #si la carte est pas valide on la met dans la defausse
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

                if not self.fin_partie(joueur,partie):
                    choix_carte=random.randint(0,len(joueur.ind_carte_cachee)-1) 
                    coord=[joueur.ind_carte_cachee[choix_carte][0],joueur.ind_carte_cachee[choix_carte][1]]
                    return coord 

                else:
                    return self.joueur_gagnant(joueur,carte,partie)
    
    def affiche(self,jeu_actuel):
        for i in range(3):
            for j in range(4):
                if jeu_actuel[i][j].etat=="ouverte":
                    print(jeu_actuel[i][j].num, "; ")
                else:
                    print(5, "; ")
    def calcul_score(self,joueur,carte):
        joueur.evol_score()
        if joueur.jeu_actuel[0][joueur.ind_carte_cachee[0][1]]==joueur.jeu_actuel[1][joueur.ind_carte_cachee[0][1]]==joueur.jeu_actuel[2][joueur.ind_carte_cachee[0][1]]:
            joueur.score_individuel-=3*carte.num -(joueur.jeu_actuel[joueur.ind_carte_cachee[0][0]][joueur.ind_carte_cachee[0][1]].num-carte.num)
    def joueur_gagnant(self,joueur,carte,partie):
        print(joueur.nom)
        nb_joueur_meilleur=0
        i=0

        self.calcul_score(joueur,carte)
        while (i<=len(partie.tab_joueurs)-1):

            fact_carte_cachee=0
            partie.tab_joueurs[i].evol_score()
            if partie.tab_joueurs[i].nom!=joueur.nom:
                for ligne in range(3):
                        for j in range(4):
                            if partie.tab_joueurs[i].jeu_actuel[ligne][j].etat=="cachee":
                                fact_carte_cachee+=5
                partie.tab_joueurs[i].score_individuel+=fact_carte_cachee
                if partie.tab_joueurs[i].score_individuel< joueur.score_individuel+carte.num and partie.tab_joueurs[i].nom!=joueur.nom:
                    nb_joueur_meilleur+=1
                print(partie.tab_joueurs[i].nom,"mon score est estimé à: ",partie.tab_joueurs[i].score_individuel)
                self.affiche(partie.tab_joueurs[i].jeu_actuel)
            i+=1
        if nb_joueur_meilleur==0:
            print("je suis le joueur",joueur.nom, " et je gagne avec: ",joueur.score_individuel+carte.num)
            return joueur.ind_carte_cachee[0]
        else: 
            return self.jeu_fin_partie(joueur,carte,partie)

    def jeu_fin_partie(self,joueur,carte,partie):
            self.evol_colonne_encours(joueur.jeu_actuel)
            max_=-3
            if len(self.colonne_encours)<4:
                for colonne in range(4):
                    if colonne in self.colonne_encours:
                        continue
                    else:
                        if joueur.jeu_actuel[0][colonne].num!="42bis":
                            ma_colonne=[joueur.jeu_actuel[0][colonne].num,joueur.jeu_actuel[1][colonne].num,joueur.jeu_actuel[2][colonne].num]
                            max_tmp=max(ma_colonne)
                            if max_tmp>max_ and max_tmp>=0:
                                max_=max_tmp
                                coord=[ma_colonne.index(max_),colonne,]
                if max_>-3:
                    return coord
            
            coord_max_tmp=[]
            for colonne in self.colonne_encours:
                if colonne not in self.colonne_encours:
                    continue
                else:
                    if joueur.jeu_actuel[0][colonne].num=="42bis":
                        continue
                    elif joueur.jeu_actuel[0][colonne].num!=joueur.jeu_actuel[1][colonne].num and joueur.jeu_actuel[0][colonne].num!=joueur.jeu_actuel[2][colonne].num:
                        coord_max_tmp.append([0,colonne])
                    elif joueur.jeu_actuel[1][colonne].num!=joueur.jeu_actuel[0][colonne].num and joueur.jeu_actuel[1][colonne].num!=joueur.jeu_actuel[2][colonne].num:
                        coord_max_tmp.append([1,colonne])
                    else:
                        coord_max_tmp.append([2,colonne])
            for k in range(1,len(coord_max_tmp)):
                val=joueur.jeu_actuel[coord_max_tmp[k][0]][coord_max_tmp[k][1]].num
                if val>max_ and val>0 :
                    coord=[coord_max_tmp[k][0],coord_max_tmp[k][1]]
                    max_=val
            if max_>-3:
                return coord
            
            else:
                '''on recherche juste le maximum dans tout le jeu'''
                pass

            
            






            
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

        
