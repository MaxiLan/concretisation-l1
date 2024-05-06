import click
import pygame
import random
import carte
import robot

def tour(joueur,partie, ecran):
  """
  Réalise le tour d'un joueur
  """
  if isinstance(joueur, robot.Robot):
    joueur.evol_carte_cachee()
    print("yes")
  ecran.fill("grey24")
  tour_fini=False
  partie.carte_en_main="images/carte_selectionnee.png"
  ch = "images/loupe.png"
  img = pygame.image.load(ch)
  img = pygame.transform.scale(img, (50,50))
  ecran.blit(img, (ecran.get_width()-80, 30))
  #tant que son tour n'est pas fini, son jeu reste affiché
  carte.cacher_carte(ecran,partie)
  font=pygame.font.Font(None, 35)
  text=font.render("Joueur n°"+str(joueur.nom),1, "white")
  ecran.blit(text,(4*(110 * ecran.get_height()/850) +120,30))
    
  joueur.affiche_jeu(ecran)
  partie.pioche.affiche(ecran)
  partie.defausse.affiche(ecran)
  pygame.display.flip()
  
  while not tour_fini:  
    tour_fini = click.click_pioche_defausse(joueur,partie, ecran)
    
  
def retourne_carte(partie, joueur, ecran):
  """
  Retourne une carte choisie par le joueur dans son jeu
  """ 
  h = partie.pioche.cartes[0].hauteur
  l = partie.pioche.cartes[0].largeur
  
  click = False
  while not click:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

    if isinstance(joueur,Robot):
      pygame.time.wait(500)
      pos=joueur.retourne_carte()
      joueur.jeu_actuel[pos[0]][pos[1]].etat = "ouverte"
      joueur.affiche_jeu(ecran)
      pygame.display.flip()
      click = True
    else: 
      pygame.event.get()
      s = pygame.mouse.get_pressed()

      if s[0]:
        pos = pygame.mouse.get_pos()

        for i in range(3):
          for j in range(4):
            if (30 + j * l+j*20< pos[0] <30 + j * l+j*20 + l) and (30 + i * h+i*15< pos[1] <  30 + i * h+i*15 + h):
            
              if joueur.jeu_actuel[i][j].etat != "ouverte":
                joueur.jeu_actuel[i][j].etat = "ouverte"
                joueur.affiche_jeu(ecran)
                pygame.display.flip()
                

  pygame.time.wait(150)


def lancement_manche(partie,ecran):
  """
  Prépare le début de la manche  (mélange, distribution de la pioche et retourne
  des cartes au hasard)
  """
  l_milieu = ecran.get_width() // 2
  H = ecran.get_height()

  ma_carte=carte.Carte(42,ecran)
  partie.pioche.vide()
  partie.pioche.rempli(ecran)
  partie.pioche.melange()

  #distribution des cartes  
  for joueur in partie.tab_joueurs:
    for i in range(3):
      for j in range(4):
        joueur.jeu_actuel[i][j] = partie.pioche.cartes.pop(0)
    
    ecran.fill("grey24")
    objet_font1 = pygame.font.Font(None, 45)
    ecran.blit(objet_font1.render("Retournez 2 cartes", True, "white"), (l_milieu - 137, H-200))
    objet_font2=pygame.font.Font(None, 35)
    text=objet_font2.render("Joueur n°"+str(joueur.nom),1, "white")
    ecran.blit(text,(4*(110 * ecran.get_height()/850) +120,30))

    joueur.affiche_jeu(ecran)
    pygame.display.flip()

    retourne_carte(partie, joueur, ecran)
    retourne_carte(partie, joueur, ecran)
    
    pygame.display.flip()
    pygame.time.wait(1000)

  #affichage dès le debut de l'emplacement "carte en main" 
  ma_carte=carte.Carte(42,ecran)
  partie.defausse.ajout_carte(ma_carte)
  partie.defausse.ajout_carte(partie.pioche.cartes[0])
  carte.cacher_carte(ecran,partie)
  partie.pioche.cartes.pop(0)
  partie.pioche.cartes[0].etat = "ouverte"


def fin_manche(ind_joueur,tab_joueurs):
  """
  Renvoie vrai si la manche est terminée,
  i.e. un joueur a retourné toutes ses cartes
  """
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
  """
  Renvoie l'indice du joueur ayant la plus au score au départ
  """
  ind_j1=0
  for i in range(1,len(tab_joueurs)):
    if tab_joueurs[i].score_individuel>tab_joueurs[ind_j1].score_individuel:
      ind_j1=i
  return ind_j1


def affichage_fin_manche(partie,ecran):
  """
  Affiche les scores des joueurs à la fin de la manche
  """
  font=pygame.font.Font(None, 45)
  text=font.render("RESULTATS MANCHE: ",1,"white")
  ecran.blit(text,(30,30))
  h=1
  for i in range(len(partie.tab_joueurs)):
      text=font.render("Score joueur n°"+str(i+1)+" : " +str(partie.score[i]),1, "white")
      ecran.blit(text,(150,150+h))
      pygame.display.flip()
      h=h+25
  

def jeu_fin_manche(joueur,ecran):
    """
    Avant de finir la manche, retourne les cartes de tous les joueurs
    pour pouvoir calculer les scores
    """
    joueur.evol_score()
    for i in range(3):
      for j in range(4):
        if joueur.jeu_actuel[i][j].etat!="ouverte":
          joueur.jeu_actuel[i][j].etat="ouverte"
    ecran.fill("grey24")


def continuer_partie(ecran, partie):
  """
  Relance une manche ou arrête la partie
  """
  l_milieu = ecran.get_width() // 2
  objet_font = pygame.font.Font(None, 30) 
  ecran.blit(objet_font.render("Cliquez pour continuer", True, "white"), (l_milieu-228 - 50, 600))
  ecran.blit(objet_font.render("Cliquez pour arrêtez", True, "white"), (l_milieu + 50, 600))
  pygame.display.flip()

  cliquer = False
  while not cliquer:
    pygame.event.get()
    s = pygame.mouse.get_pressed()

    if s[0]:
      pos = pygame.mouse.get_pos()

      if (l_milieu-228 - 50<pos[0]<l_milieu - 50 ) and (600<pos[1]<620):
        cliquer = True
        return True
      elif (l_milieu + 50<pos[0]<l_milieu + 50 + 200) and (600<pos[1]<620):
        cliquer = True
        return False


def manche(partie, ecran): 
  """
  Réalise une manche entière
  """
  lancement_manche(partie,ecran)
  for joueur in partie.tab_joueurs:
    joueur.evol_score()
  i_joueur = joueur_commence(partie.tab_joueurs)
  
  joueur = partie.tab_joueurs[i_joueur]
  manche_fin = False
  
  pygame.time.wait(150)
  while not manche_fin:
    #déroulement d'un tour
    tour(joueur, partie, ecran)    

    #mise à jour de l'écran
    partie.defausse.affiche(ecran)
    joueur.retrait_colonne(partie.defausse,ecran)
    joueur.affiche_jeu(ecran) 
    pygame.display.flip() 
    
    #test si fin de manche
    manche_fin = fin_manche(i_joueur,partie.tab_joueurs)
    i_gagnant=i_joueur
    joueur.evol_score()

    #changement de joueur pour la suite
    i_joueur = (i_joueur + 1) % len(partie.tab_joueurs)
    joueur = partie.tab_joueurs[i_joueur]
    #laisse le temps au joueur de voir son score
    pygame.time.wait(500)

  #une fois qu'un joueur a retourné toute ses cartes il faut encore faire un tour
  for i in range(len(partie.tab_joueurs)-1):
    tour(joueur, partie, ecran)
    partie.defausse.affiche(ecran)
    joueur.retrait_colonne(partie.pioche,ecran)
    jeu_fin_manche(joueur,ecran)
    joueur.affiche_jeu(ecran) 
    pygame.display.flip()
    i_joueur = (i_joueur + 1) % len(partie.tab_joueurs)
    joueur = partie.tab_joueurs[i_joueur]
    pygame.time.wait(2000)
  
  for num_joueur in range (len(partie.tab_joueurs)):
    if partie.tab_joueurs[i_gagnant].score_individuel>=partie.tab_joueurs[num_joueur].score_individuel and i_gagnant != num_joueur:
        partie.tab_joueurs[i_gagnant].score_individuel=partie.tab_joueurs[i_gagnant].score_individuel*2

  #tout le monde a joué il faut maintenant mettre tout les jeux joueurs ouverts et afficher les gagnants
  ecran.fill("grey24")
  partie.mise_a_jour_score()
  affichage_fin_manche(partie,ecran)
  return continuer_partie(ecran, partie)
