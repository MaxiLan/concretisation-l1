import robot
import random
class Strategie_aleatoire:

    def __init__(self,provenance=1):
        self.provenance=provenance
        self.carte_ouverte=[]


    def carte_ouverte(self,jeu_actuel):
      """
      Renvoie les cartes ouvertes d'un jeu
      """
      self.carte_ouverte=[]
      for i in range(3):
          for j in range(4):
              if jeu_actuel[i][j].etat=="ouverte":
                  self.carte_ouverte.append([i,j])


    def choix_pioche_def(self,jeu_actuel,partie):
        """
        Choisi aléatoirement la carte de la pioche ou de la défausse
        """
        choix_pioche =random.randint(0,1)
        if choix_pioche==1:
            coords=[partie.pioche.abs,partie.pioche.ord]
            self.provenance=1
            return coords 
        else:
            self.provenance=0
            coords=[partie.defausse.abs,partie.defausse.ord]
            return coords
            

    def choix_placement_carte(self,joueur,carte,partie):  
        """
        Va choisir aléatoirement l'endroit où envoyer la carte dans le jeu qu'elle vienne
        de la pioche ou de la defausse.
        """
        self.carte_ouverte(joueur.jeu_actuel)
        if self.provenance==0: #si carte a ete prise depuis la défausse
            echg_with_carte_cachee=random.randint(0,1) 
            #soit on retourne avec une carte ouverte soit une carte cachée
            if echg_with_carte_cachee==1:
                return self.retourne_hasard(joueur)
            else:
                choix_carte=random.randint(0,len(self.carte_ouverte)-1)
                coords=[self.carte_ouverte[choix_carte][0],self.carte_ouverte[choix_carte][1]]
                return coords
        
        else:
            keep_pioche=random.randint(0,1)
            if keep_pioche==0:
                #échange avec une carte déjà ouverte
                echg_with_carte_cachee=random.randint(0,1) 
                #soit on retourne avec une carte ouverte soit une carte cachée
                if echg_with_carte_cachee==1:
                    return self.retourne_hasard(joueur)
                else:
                    choix_carte=random.randint(0,len(self.carte_ouverte)-1)
                    coords=[self.carte_ouverte[choix_carte][0],self.carte_ouverte[choix_carte][1]]
                    return coords
                
            else:
                return [-1,-1]


    def retourne_hasard(self,joueur):
            choix_carte=random.randint(0,len(joueur.ind_carte_cachee)-1) 
            coord=[joueur.ind_carte_cachee[choix_carte][0],joueur.ind_carte_cachee[choix_carte][1]]
            return  coord


    def debut_manche(self,joueur):
        """
        Fonction du début qui choisit les cartes qui se retournent
        """
        coord=[]
        while coord==[]:
            i=random.randint(0,2)
            j=random.randint(0,3)
            if joueur.jeu_actuel[i][j].etat=="cachee":
                coord=[i,j]
        return coord
