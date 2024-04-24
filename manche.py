import click
import pygame
import random
import carte


def tour(joueur, pioche, defausse, ecran,tab_joueurs):
  #réalise le tour d'un joueur
  ecran.fill("grey24")
  tour_fini=click.click_pioche_defausse(joueur,pioche,defausse,ecran,tab_joueurs)
  
  ch = "images/loupe.png"
  img = pygame.image.load(ch)
  img = pygame.transform.scale(img, (50,50))
  ecran.blit(img, (ecran.get_width()-80, 30))
  #tant que son tour n'est pas fini, son jeu reste affiché
  carte.cacher_carte(ecran,defausse.cartes[0])
  font=pygame.font.Font(None, 35)
  text=font.render("Joueur n°"+str(joueur.nom),1, "white")
  ecran.blit(text,(4*(110 * ecran.get_height()/850) +120,30))
    
  joueur.affiche_jeu(ecran)
  pioche.affiche(ecran)
  defausse.affiche(ecran)
  pygame.display.flip()
  while not tour_fini:  
    tour_fini = click.click_pioche_defausse(joueur, pioche, defausse, ecran,tab_joueurs)
    
  


def lancement_manche(pioche, defausse, tab_joueurs,ecran):
  
  ma_carte=carte.Carte(42,ecran)
  pioche.melange()
  for joueur in tab_joueurs:
    for i in range(3):
      for _ in range(4):
        joueur.jeu_actuel[i].append(pioche.cartes[0])
        pioche.cartes.pop(0)

    abs = random.randint(0, 2)
    ord = random.randint(0, 3)
    joueur.jeu_actuel[abs][ord].etat = "ouverte"
    while (joueur.jeu_actuel[abs][ord].etat != "cachee"):
      abs = random.randint(0, 2)
      ord = random.randint(0, 3)

    joueur.jeu_actuel[abs][ord].etat = "ouverte"

  #AFFICHAGE des le debut de l'emplacement "carte en main" 
  carte.cacher_carte(ecran,ma_carte)
  defausse.ajout_carte(ma_carte)
  defausse.ajout_carte(pioche.cartes[0])
  pioche.cartes.pop(0)
  pioche.cartes[0].etat = "ouverte"


def fin_manche(ind_joueur,tab_joueurs):
  #J est un joueur, on testera s'il a retourné toutes ses cartes ou non
  i = 0
  manche_finie = True
  while (manche_finie and i < 3):
    j = 0
    while (j < 4 and manche_finie):
      if tab_joueurs[ind_joueur].jeu_actuel[i][j].etat == "cachee":
        manche_finie = False
      j += 1
    i += 1
  return manche_finie

def joueur_commence(tab_joueurs):
  ind_j1=0
  for i in range(1,len(tab_joueurs)):
    if tab_joueurs[i].score_individuel>tab_joueurs[ind_j1].score_individuel:
      ind_j1=i
  return ind_j1

def affichage_fin_manche(tab_joueurs,ecran):
  font=pygame.font.Font(None, 45)
  text=font.render("RESULTATS MANCHE: ",1,"white")
  ecran.blit(text,(30,30))
  i=1
  for joueurs in tab_joueurs:
      text=font.render("Score joueur n°"+str(joueurs.nom)+" : " +str(joueurs.score_individuel),1, "white")
      ecran.blit(text,(150,150+i))
      pygame.display.flip()
      i=i+25

def jeu_fin_manche(tab_joueurs,ecran):
  #ACTUALISATION DE TOUT LES JEUX DES SCORES= ON RETOURNE TOUE LES CARTES DU JEU
    for joueur in tab_joueurs:
      for i in range(3):
        for j in range(4):
          if joueur.jeu_actuel[i][j].etat!="ouverte":
            joueur.jeu_actuel[i][j].etat="ouverte"
      joueur.evol_score()
    ecran.fill("grey24")
    affichage_fin_manche(tab_joueurs,ecran)
    


def manche(tab_joueurs, pioche, defausse, ecran): 
  lancement_manche(pioche, defausse, tab_joueurs,ecran)
  for joueur in tab_joueurs:
    joueur.evol_score()
  i_joueur = joueur_commence(tab_joueurs)
  print(i_joueur)
  joueur = tab_joueurs[i_joueur]
  manche_fin = False
  
  
  while not manche_fin:
    
    tour(joueur, pioche, defausse, ecran,tab_joueurs) #deroulement d'un tour
    #mise a jour ecran
    defausse.affiche(ecran)
    joueur.retrait_colonne(defausse,ecran)
    joueur.affiche_jeu(ecran) 
    pygame.display.flip() 

    manche_fin = fin_manche(i_joueur,tab_joueurs)#test fin de manche
    gagant=joueur
    #changement de joueur pour la suite
    i_joueur = (i_joueur + 1) % len(tab_joueurs)
    joueur = tab_joueurs[i_joueur]
    pygame.time.wait(500) #laisse le temps au joueur de voir son score

  #une fois qu'un joueur a retourné toute ses cartes il faut encore faire un tour :
  for i in range(len(tab_joueurs)-1):
    tour(joueur, pioche, defausse, ecran,tab_joueurs)
    defausse.affiche(ecran)
    joueur.retrait_colonne(pioche,ecran)
    joueur.affiche_jeu(ecran) 
    pygame.display.flip()
    i_joueur = (i_joueur + 1) % len(tab_joueurs)
    joueur = tab_joueurs[i_joueur]
    pygame.time.wait(2000)

  #tout le monde a joué il faut maintenant mettre tout les jeux joueurs ouverts et afficher les gagnants
  jeu_fin_manche(tab_joueurs,ecran)
  return True

  
  
