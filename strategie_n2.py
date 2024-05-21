import robot


class Strategie_n2:
    """
    Utilise la probabilité qu'une carte apparaisse
    """
    def __init__(self):
        self.colonne_en_cours=[]
        self.carte_a_suppr = []
        self.nb_cartes=[5,10,15]
        self.score_par_colonne=[15,15,15,15]
        self.ind_interdit=[]
        self.carte_cachee=0
        for _ in range(12):
            self.nb_cartes.append(10)


    def debut_manche(self,joueur):
        """
        Renvoie les coordonnées des 2 cartes à retourner au début d'une manche
        """
        coord=[]
        for i in range(2):
            if joueur.jeu_actuel[len(joueur.jeu_actuel)-1-i][len(joueur.jeu_actuel[0])-1].etat!="ouverte":
                coord=[len(joueur.jeu_actuel)-1-i,len(joueur.jeu_actuel[0])-1]  
        return coord   


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
            return 13


    def evol_score_colonne(self,jeu_actuel):
        """ 
            calcule le score colonne par colonne
        """
        for colonne in range(4):
            somme_col=0
            for ligne in range(3):
                if jeu_actuel[ligne][colonne].etat=="ouverte" :
                    if jeu_actuel[ligne][colonne].num!="42bis":
                        somme_col+=jeu_actuel[ligne][colonne].num
                else:
                    somme_col+=5
            self.score_par_colonne[colonne]=somme_col


    def evol_nb_cartes(self,partie):
        """
            met a jour a chaque tour le nombre de cartes non découvertes
        """
        self.carte_cachee=len(partie.pioche.carte)

        #on parcourt les jeux des joueurs et on regarde si de nouvelles cartes on été dévoilées (qu'elles viennent de la pioche ou de la défausse)
        for J in partie.tab_joueurs:
            for ligne in range(3):
                for colonne in range(4):
                    if J.jeu_actuel[ligne][colonne].etat=="cachee":
                        self.carte_cachee+=1 # on profite de ce parcourt pour mettre à jour le nombre total de carte cachee dans la partie
                    elif J.jeu_actuel[ligne][colonne].lieu!="visitee" and carte.num!="42bis":
                        self.nb_cartes[J.jeu_actuel[ligne][colonne].num+2]-=1
                        J.jeu_actuel[ligne][colonne].lieu="visitee"
        
        for carte in partie.defausse.carte:
            if carte.num!="42bis":
                if carte.etat=="ouverte" and carte.lieu!="visitee":
                    carte.lieu==visitee
                    self.nb_cartes[carte.num+2]-=1


    def proba_constr_col(self,carte,jeu_actuel,partie):
        """
            calcule la probabilité de réussir à réaliser la colonne au coup suivant
        """
        proba_c_pioche=0
        self.evol_nb_cartes(partie)
        for j in range(len(partie.tab_joueurs)-1):
            #nb_c_pioche=len(partie.pioche.cartes)-i
            proba_c_pioche+= ( (self.nb_cartes[carte.num+2])/(self.carte_cachee-i))
        proba_c_pioche=1-proba_c_pioche
        return proba_c_pioche
        

    def carte_valide(self,carte,jeu_actuel,partie):
        if self.proba_constr_col(carte,jeu_actuel,partie)>0.5  or carte.num<=0:
            return True
        else :
            return False
        

    def choix_pioche_def(self,jeu_actuel,partie):
        """
        Renvoie les coordonnées de la pioche ou de la défausse, selon la situation
        """
        self.evol_nb_cartes(partie)
        d=partie.defausse.cartes[-1]
        coords=[partie.pioche.abs,partie.pioche.ord]
        if self.carte_valide(d) or self.nb_cartes[d.num+2]>7:
            #si carte négative dans la défausse, on la prend
            coords=[partie.defausse.abs,partie.defausse.ord]
        return coords


    def choix_placement_carte(self,joueur,carte,partie):  
        """
        Choisi l'endroit où envoyer la carte dans le jeu, qu'elle vienne
        de la pioche ou de la défausse.
        """

        #met à jour les cartes à supprimer, les colonnes en cours et les indices interdits
        self.evol_colonne_encours(joueur.jeu_actuel)
       
        #si la carte est pas valide on la met dans la défausse
        if not self.carte_valide(carte) and not self.fin_partie(joueur):
            coord=[-1,-1]
            return coord
    
        #sinon plusieurs options
        else:
            
            #si il y des colonnes à finir
            for col in self.colonne_en_cours:
                if self.num_colonne_en_cours(joueur.jeu_actuel, col)==carte.num:
                    #si la carte en main est positive, on complète la colonne
                    if carte.num > 0:
                        for i in range(3):
                            if joueur.jeu_actuel[i][col].etat=="cachee":
                                return [i, col]
                    
                    #sinon, on rend ces coordonnées interdites pour ne pas faire une colonne négative
                    else:
                        for i in range(3):
                            if joueur.jeu_actuel[i][col].etat=="cachee":
                               self.ind_interdit.append([i,col])
                        

            #avancée des colonnes
            for i in range (3):
                for j in range(4):
                    if joueur.jeu_actuel[i][j].etat=="ouverte" and joueur.jeu_actuel[i][j].num==carte.num:  
                            ligne=self.etude_colonne(joueur.jeu_actuel,j,carte)
                            coord=[ligne,j]
                            if ligne!=-1:
                                return coord


            #si il reste des cartes non valides dans le jeu du joueur    
            if len(self.carte_a_suppr)!=0:
                for i in range(3):
                    for j in range(4):
                        if joueur.jeu_actuel[i][j].num==self.carte_a_suppr[0] and joueur.jeu_actuel[i][j].etat=="ouverte":
                            self.carte_a_suppr.pop(0)
                            coord=[i,j]
                            return coord 

            #sinon, si ce n'est pas la fin de partie, on retourne une carte au hasard            
            if not self.fin_partie(joueur):

                choix_carte=random.randint(0,len(joueur.ind_carte_cachee)-1)
                while [joueur.ind_carte_cachee[choix_carte][0],joueur.ind_carte_cachee[choix_carte][1]] in self.ind_interdit:
                    choix_carte=random.randint(0,len(joueur.ind_carte_cachee)-1)
                coord=[joueur.ind_carte_cachee[choix_carte][0],joueur.ind_carte_cachee[choix_carte][1]]
                return coord 

            #sinon, on appelle une fonction pour la fin de partie
            else:
                return self.joueur_gagnant(joueur,carte,partie)

    


   
    def proba_tirer_carte(self, carte, partie):
        return self.probas_carte[carte.num+2] / self.carte_cachee
