import robot


class Strategie_n2:
    """
    Utilise la probabilité qu'une carte apparaisse
    """

    def __init__(self):
        self.colonne_en_cours=[]
        self.carte_a_suppr = []


    def debut_manche(self,joueur):
        """
        Renvoie les coordonnées des 2 cartes à retourner au début d'une manche
        """
        coord=[]
        for i in range(2):
            if joueur.jeu_actuel[len(joueur.jeu_actuel)-1-i][len(joueur.jeu_actuel[0])-1].etat!="ouverte":
                coord=[len(joueur.jeu_actuel)-1-i,len(joueur.jeu_actuel[0])-1]
        
        return coord   
    

    def nb_cartes_total(self, carte):
        n = carte.num

        if n==-2:
            return 5
        elif nb==0:
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

