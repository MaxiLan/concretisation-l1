import robot
import random
import manche
class Strategie_n1:
    """ 
    Ne prends pas les cartes au dessus égales à 7
    pioche ou defausse :
    defausse si on peut avancer une colonne sup a 0 ou si carte <=0
    pioche sinon. 
        si carte valide
            on la met dans une colonne 
        sinon on retourne une carte du jeu
    """

    def __init__(self):
        self.colonne_en_cours=[]
        self.carte_a_suppr = []


    def fin_partie(self,joueur):
        return len(joueur.ind_carte_cachee)==1


    def carte_valide(self,c):
        """
        Renvoie vrai si le numéro de la carte est strictement inférieur à 7
        """
        if c.num>= 7:
            return False
        else :
            return True


    def carte_a_suppr_maj(self,joueur):
        """
        Met à jour la liste de cartes à supprimer en priorité
        """
        self.carte_a_suppr=[]
        for i in range (3):
            for j in range(4):
                if joueur.jeu_actuel[i][j].num!="42bis":
                    if joueur.jeu_actuel[i][j].etat=="ouverte" and not self.carte_valide(joueur.jeu_actuel[i][j]):
                        self.carte_a_suppr.append(joueur.jeu_actuel[i][j].num) 


    def evol_colonne_encours(self,jeu_actuel):
        """
        Met à jour les colonnes en cours (si 2 cartes égales sont présent dans une colonne) 
        """
        self.colonne_en_cours=[]
        for colonne in range(3):
            if ((jeu_actuel[0][colonne].etat=="ouverte" and jeu_actuel[1][colonne].etat=="ouverte" and jeu_actuel[0][colonne].num==jeu_actuel[1][colonne].num) 
                or (jeu_actuel[1][colonne].etat=="ouverte" and jeu_actuel[2][colonne].etat=="ouverte" and jeu_actuel[1][colonne].num==jeu_actuel[2][colonne].num) 
                or (jeu_actuel[0][colonne].etat=="ouverte" and jeu_actuel[2][colonne].etat=="ouverte" and jeu_actuel[0][colonne].num==jeu_actuel[2][colonne].num)):

                  self.colonne_en_cours.append(colonne)


    def num_colonne_en_cours(self,jeu_actuel,j):
        """
        Si une colonne j est en cours, la fonction renvoie le numéro de la carte la plus présente
        """
        if (jeu_actuel[0][j].etat=="ouverte" 
            and ( (jeu_actuel[0][j].num==jeu_actuel[1][j].num and jeu_actuel[1][j].etat=="ouverte") 
                 or (jeu_actuel[0][j].num==jeu_actuel[2][j].num and jeu_actuel[2][j].etat=="ouverte") )):

            return jeu_actuel[0][j].num

        elif (jeu_actuel[2][j].etat=="ouverte" 
              and ( (jeu_actuel[2][j].num==jeu_actuel[1][j].num and jeu_actuel[1][j].etat=="ouverte") 
                   or (jeu_actuel[0][j].num==jeu_actuel[2][j].num and jeu_actuel[0][j].etat=="ouverte") )):
            return jeu_actuel[1][j].num
        else :
            return 12 


    def retourne_hasard(self,joueur):
        """
        Choisi des coordonnées aléatoires parmi les cartes cachées du jeu
        """
        
        choix_carte=random.randint(0,len(joueur.ind_carte_cachee)-1) 
        coord=[joueur.ind_carte_cachee[choix_carte][0],joueur.ind_carte_cachee[choix_carte][1]]
        return  coord


    def debut_manche(self,joueur):
        """
        Renvoie les coordonnées des 2 cartes à retourner au début d'une manche
        """
        coord=[]
        for i in range(2):
            if joueur.jeu_actuel[len(joueur.jeu_actuel)-1-i][len(joueur.jeu_actuel[0])-1].etat!="ouverte":
                coord=[len(joueur.jeu_actuel)-1-i,len(joueur.jeu_actuel[0])-1]
                #coord=[i,0]
        
        return coord


    def choix_pioche_def(self,jeu_actuel,partie):
        """
        Renvoie les coordonnées de la pioche ou de la défausse, selon la situation
        """
        d=partie.defausse.cartes[-1]
        coords=[partie.pioche.abs,partie.pioche.ord]
        if self.carte_valide(d):
            #si carte négative dans la défausse, on la prend
            if d.num<=0:
                coords=[partie.defausse.abs,partie.defausse.ord]

            #si la defausse contient une carte qui fait avancer une colonne, on la prend
            else:
                for j in range(4):
                    if jeu_actuel[0][j].num==d.num or jeu_actuel[1][j].num==d.num or jeu_actuel[2][j].num==d.num:
                        coords=[partie.defausse.abs,partie.defausse.ord]
        
        return coords


    def etude_colonne(self,jeu_actuel,colonne,carte):
        """
        Fonction appelée si une carte est de la meme valeur dans la colonne
        on va alors chercher où mettre cette dernière et renvoyer les indices impliqués
        """
        compte_neg=0
        maximum=-3
        ind_max=-1
        for i in range(3):
            if jeu_actuel[i][colonne].etat=="ouverte":
                if self.num_colonne_en_cours(jeu_actuel,colonne)>=carte.num:

                    #si la carte en main est négative, on compte le nombre de carte négatives dans la colonne
                    if jeu_actuel[i][colonne].num==carte.num and carte.num<=0:
                        compte_neg+=1
                    
                    #on récupère la carte la plus grande de la colonne, différente de la carte en main
                    if jeu_actuel[i][colonne].num>maximum and jeu_actuel[i][colonne].num!=carte.num:
                        ind_max=i
                        maximum=jeu_actuel[i][colonne].num

            elif maximum<0:
                #A TESTER
                maximum=0
                ind_max=i

        if compte_neg==2:
            return -1
        else:
            return ind_max

                    
    def choix_placement_carte(self,joueur,carte,partie):  
        """
        Choisi l'endroit où envoyer la carte dans le jeu, qu'elle vienne
        de la pioche ou de la défausse.
        """

        #met à jour les cartes à supprimer et les colonnes en cours
        self.carte_a_suppr_maj(joueur)
        self.evol_colonne_encours(joueur.jeu_actuel)
    
        #si la carte est pas valide on la met dans la défausse
        if not self.carte_valide(carte) and not self.fin_partie(joueur):
            coord=[-1,-1]
            return coord
    
        #sinon plusieurs options
        else:
            
            #si il y des colonnes à finir
            if carte.num > 0:
                for c in self.colonne_en_cours:
                    if self.num_colonne_en_cours(joueur.jeu_actuel, c)==carte.num:
                        for i in range(3):
                            if joueur.jeu_actuel[i][c].etat=="cachee":
                                return [i, c]

            
            #avancée des colonnes
            for i in range (3):
                for j in range(4):
                    if joueur.jeu_actuel[i][j].etat=="ouverte" and joueur.jeu_actuel[i][j].num==carte.num:  
                            ligne=self.etude_colonne(joueur.jeu_actuel,j,carte)
                            coord=[ligne,j]
                            if ligne!=-1:
                                return coord

            #y a t'il des cartes qui ne sont pas valides dans notre jeu actuel ?           
            if len(self.carte_a_suppr)!=0:
                for i in range(3):
                    for j in range(4):
                        if joueur.jeu_actuel[i][j].num==self.carte_a_suppr[0] and joueur.jeu_actuel[i][j].etat=="ouverte":
                            self.carte_a_suppr.pop(0)
                            coord=[i,j]
                            return coord #alors on retourne les indices de la carte a supprimer

            if not self.fin_partie(joueur):
                choix_carte=random.randint(0,len(joueur.ind_carte_cachee)-1) 
                coord=[joueur.ind_carte_cachee[choix_carte][0],joueur.ind_carte_cachee[choix_carte][1]]
                return coord 

            else:
                return self.joueur_gagnant(joueur,carte,partie)

    

    def calcul_score(self,joueur,carte):
        joueur.evol_score()
        if joueur.jeu_actuel[0][joueur.ind_carte_cachee[0][1]]==joueur.jeu_actuel[1][joueur.ind_carte_cachee[0][1]]==joueur.jeu_actuel[2][joueur.ind_carte_cachee[0][1]]:
            joueur.score_individuel -= 3*carte.num -(joueur.jeu_actuel[joueur.ind_carte_cachee[0][0]][joueur.ind_carte_cachee[0][1]].num-carte.num)
    

    def carte_max(self, jeu_actuel):
        coord = [0, 0]

        for l in range(3):
            for c in range(4):
                if jeu_actuel[l][c].num > c_max.num:
                    coord = [l, c]

        return coord


    def joueur_gagnant(self,joueur,carte,partie):
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
                self.affiche(partie.tab_joueurs[i].jeu_actuel)
            i+=1
        if nb_joueur_meilleur==0:
            return joueur.ind_carte_cachee[0]
        else: 
            return self.jeu_fin_partie(joueur,carte,partie)


    def jeu_fin_partie(self,joueur,carte,partie):
            self.evol_colonne_encours(joueur.jeu_actuel)
            max_=-3
            if len(self.colonne_en_cours)<4:
                for colonne in range(4):
                    if colonne in self.colonne_en_cours:
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
            for colonne in self.colonne_en_cours:
                if colonne not in self.colonne_en_cours:
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
                #on recherche juste le maximum dans tout le jeu
                return self.carte_max(jeu_actuel)

            
            






            


        
