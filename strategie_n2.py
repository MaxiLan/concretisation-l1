import robot


class Strategie_n2:
    """
    Utilise la probabilité qu'une carte apparaisse
    """

    def __init__(self):
        self.colonne_en_cours=[]
        self.carte_a_suppr = []
        self.probas_carte=[5,10,15]
        for _ in range(12):
            self.probas_carte.append(10)
        


    def debut_manche(self,joueur):
        """
        Renvoie les coordonnées des 2 cartes à retourner au début d'une manche
        """
        coord=[]
        for i in range(2):
            if joueur.jeu_actuel[len(joueur.jeu_actuel)-1-i][len(joueur.jeu_actuel[0])-1].etat!="ouverte":
                coord=[len(joueur.jeu_actuel)-1-i,len(joueur.jeu_actuel[0])-1]  
        return coord   
    
    def evol_proba(self,partie):
        for J in partie.tab_joueurs:
            for ligne in range(3):
                for colonne in range(4):
                    if J.jeu_actuel[ligne][colonne].etat=="ouverte" and J.jeu_actuel[ligne][colonne].lieu!="visitee":
                        self.probas_carte[J.jeu_actuel[ligne][colonne].num+2]-=1
                        J.jeu_actuel[ligne][colonne].lieu="visitee"
        for carte in partie.defausse.carte:
            if carte.etat=="ouverte" and carte.lieu!="visitee":
                carte.lieu==visitee
                self.probas_carte[carte.num+2]-=1

    def nb_cartes_total(self, carte):
        n = carte.num

        if n==-2:
            return 5
        elif n==0:
            return 15
        else:
            return 10


    def nb_cartes_en_jeu(self, carte, partie):
        n = carte.num
        nb = 0

        for joueur in partie.tab_joueurs:
            for ligne in joueur.jeu_actuel:
                for c in ligne:
                    if c.num==n:
                        nb += 1

        return nb


    def proba_tirer_carte_pioche(self, carte, partie):
        if partie.defausse[-1].num == carte.num:
            return (self.nb_cartes_total(carte) - nb_cartes_en_jeu(carte) - 1) / len(partie.pioche)
        else:
            return (self.nb_cartes_total(carte) - nb_cartes_en_jeu(carte)) / len(partie.pioche)

