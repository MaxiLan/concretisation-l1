class Carte:
  
    def __init__(self, numero, ecran):
        HAUTEUR = ecran.get_height()
        facteur = HAUTEUR/850
        self.etat = "cachee" 
        self.num = numero 
        self.hauteur=160 * facteur
        self.largeur=110 * facteur
        self.lieu="pioche" # sert uniquement pour les strategies du robot