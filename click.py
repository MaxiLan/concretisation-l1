import pygame
import carte
import defausse
import pioche


def click_pioche_defausse(joueur,partie, ecran):
  """
  Permet au joueur de choisir ses cartes à jouer
  """
  HAUTEUR = ecran.get_height()
  LARGEUR = ecran.get_width()
  h = partie.defausse.cartes[0].hauteur
  l = partie.defausse.cartes[0].largeur
  click_carte = False
  pygame.event.get()
  souris = pygame.mouse.get_pressed()

  if souris_sur_aide(ecran, h):
    affiche_aide(ecran, h, section=0)
  else:
    cache_aide(ecran, l,h)
  
  #attend un click (sinon la fonction sera ré-executer) 
  if souris[0]:
    pos = pygame.mouse.get_pos()

    #si le click est sur la défausse
    if (LARGEUR- 2*l- 50< pos[0] < LARGEUR-50-l) and (HAUTEUR-30-h< pos[1] < HAUTEUR-30):
      pygame.event.get()
      s = pygame.mouse.get_pressed()
      if s[0]:
        pos = pygame.mouse.get_pos()
        if (LARGEUR-80< pos[0] < LARGEUR-30) and (30 < pos[1] < 80):
          test_appel_loupe(ecran,partie,joueur)
      #on déplace la carte de la defausse
      carte_select = partie.defausse.retire_carte()
      partie.carte_en_main="images/" + str(carte_select.num) + ".png"
      carte.cacher_carte(ecran,partie)
      partie.defausse.affiche(ecran)
      pygame.display.flip()

      #on attend la décision du joueur (carte à échanger)
      while (not click_carte):

        if souris_sur_aide(ecran,h):
          affiche_aide(ecran,h, section=1)
        else:
          cache_aide(ecran,l, h)
      
        pygame.event.get()
        s = pygame.mouse.get_pressed()

        if s[0]:
          pos = pygame.mouse.get_pos()
          
          #on regarde si le click est sur une carte
          for i in range(3):
            for j in range(4):
              if (30 + j * l+j*20< pos[0] <30 + j * l+j*20 + l) and (30 + i * h+i*15< pos[1] <  30 + i * h+i*15 + h):

                #on échange les cartes
                if joueur.jeu_actuel[i][j].num!="42bis":
                  partie.carte_en_main="images/carte_selectionnee.png"
                  aux = joueur.jeu_actuel[i][j]
                  joueur.jeu_actuel[i][j] = carte_select
                  joueur.jeu_actuel[i][j].etat = "ouverte"
                  partie.defausse.ajout_carte(aux)
                  carte.cacher_carte(ecran,partie)
                  return True
          if (LARGEUR-80< pos[0] < LARGEUR-30) and (30 < pos[1] < 80):
            test_appel_loupe(ecran,partie,joueur)
    #sinon si le click est sur la pioche
    elif (LARGEUR-30-l< pos[0] < LARGEUR-30 and HAUTEUR-30-h< pos[1] < HAUTEUR-30):
      pygame.event.get()
      s = pygame.mouse.get_pressed()
      if s[0]:
        pos = pygame.mouse.get_pos()
        if (LARGEUR-80< pos[0] < LARGEUR-30) and (30 < pos[1] < 80):
          test_appel_loupe(ecran,partie,joueur)
      # on deplace la carte de la pioche
      carte_select = partie.pioche.cartes[0]
      carte_select.etat = "ouverte"
      partie.pioche.cartes.pop(0)
      partie.pioche.est_vide(partie.defausse)
      partie.pioche.affiche(ecran)
      partie.carte_en_main= "images/" + str(carte_select.num) + ".png"
      carte.cacher_carte(ecran,partie)
      pygame.display.flip()

      click_defausse = False

      #on attend le choix du joueur (jouer sur son jeu ou sur la défausse)
      while not (click_carte or click_defausse): 

        if souris_sur_aide(ecran, h):
          affiche_aide(ecran, h, section=2) 
        else:
          cache_aide(ecran,l, h)

        pygame.event.get()
        s = pygame.mouse.get_pressed()
        if s[0]:
          pos = pygame.mouse.get_pos()
          #si le click est sur le jeu du joueur
          for i in range(3):
            for j in range(4):
              if (30 + j *l+j*20< pos[0] <30 + j * l+j*20 + l) and (30 + i * h+i*15< pos[1] <  30 + i * h+i*15 +h):

                #on echange les cartes
                if joueur.jeu_actuel[i][j].num != "42bis":
                  partie.carte_en_main="images/carte_selectionnee.png"
                  click_carte = True
                  aux = joueur.jeu_actuel[i][j]
                  joueur.jeu_actuel[i][j] = carte_select
                  joueur.jeu_actuel[i][j].etat = "ouverte"
                  partie.defausse.ajout_carte(aux)
                  carte.cacher_carte(ecran, partie)
                  return True
          if (LARGEUR-80< pos[0] < LARGEUR-30) and (30 < pos[1] < 80):
            test_appel_loupe(ecran,partie,joueur)
          #si le click est sur la defausse
          if (LARGEUR- 2*l- 50< pos[0] < LARGEUR-50-l) and (HAUTEUR-30-h< pos[1] < HAUTEUR-30):
            partie.carte_en_main="images/carte_selectionnee.png"
            partie.defausse.ajout_carte(carte_select)
            partie.defausse.affiche(ecran)
            carte.cacher_carte(ecran,partie)
            pygame.display.flip()
            click_defausse = True
            #on retourne une carte selectionnnée par le joueur
            return retourne_cartes(joueur, ecran,partie)

          

    #si le joueur clique sur la loupe 
    elif (LARGEUR-80< pos[0] < LARGEUR-30) and (30 < pos[1] < 80):
        test_appel_loupe(ecran,partie,joueur)
 
  else:
    #sinon on renvoie False, et la fonction sera rappelée
    return False

def test_appel_loupe(ecran,partie,joueur):
  click_croix=False
  i_joueur=0 #arbitraire
  
  while not click_croix:
    pygame.time.wait(100)
    click_croix,i_joueur=voir_autre_jeu(ecran,partie.tab_joueurs,i_joueur)

  font=pygame.font.Font(None, 35)
  text=font.render("Joueur n°"+str(joueur.nom),1, "white")
  ecran.blit(text,(4*(110 * ecran.get_height()/850) +120,30))
  joueur.affiche_jeu(ecran)
  partie.pioche.affiche(ecran)
  partie.defausse.affiche(ecran)
  carte.cacher_carte(ecran,partie)
  pygame.display.flip()
  pygame.time.wait(200)

def retourne_cartes(joueur, ecran,partie): 
  """
  Retourne une carte dans le jeu du joueur
  """
  HAUTEUR = ecran.get_height()
  LARGEUR = ecran.get_width()
  h = joueur.jeu_actuel[0][0].hauteur
  l = joueur.jeu_actuel[0][0].largeur 
  carte_selectionner = False

  while not (carte_selectionner):
    if souris_sur_aide(ecran, h):
      affiche_aide(ecran, h, section=3) 
    else:
      cache_aide(ecran,l,h)
    pygame.event.get()
    s = pygame.mouse.get_pressed()

    if s[0]:
      pos = pygame.mouse.get_pos()
      if (LARGEUR-80< pos[0] < LARGEUR-30) and (30 < pos[1] < 80):
          test_appel_loupe(ecran,partie,joueur)
      for i in range(3):
        for j in range(4):
          if(30 + j * l+j*20< pos[0] <30 + j * l+j*20 +l) and (30 + i * h+i*15< pos[1] <  30 + i * h+i*15 + h):
            if joueur.jeu_actuel[i][j].etat != "ouverte":
              joueur.jeu_actuel[i][j].etat = "ouverte"
              carte_selectionner = True


  return True


def affiche_aide(ecran, h_carte, section):
  """
  Affiche de l'aide si le joueur place sa souris sur le point d'intérrogation
  """
  img = pygame.image.load("images/question.png")
  img = pygame.transform.scale(img, (40, 40))
  ecran.blit(img, (30, 30+3*15+3*h_carte + 10))
  objet_texte = pygame.font.Font(None, 32)

  if section==0:
    texte="Prenez une carte de la défausse ou de la pioche"
  elif section==1:
    texte="Echangez avec une de vos cartes"
  elif section==2:
    texte="Echangez avec une de vos cartes ou posez la dans la défausse"
  elif section==3:
    texte="Retournez maintenant une carte"
  

  ecran.blit(objet_texte.render(texte, True, "white"), (30,30+3*15+3*h_carte + 10 +40))
  pygame.display.flip()


def cache_aide(ecran, l_carte, h_carte):
  """
  Cache l'aide si le joueur a enlevé sa souris de l'aide
  """
  img = pygame.image.load("images/question.png")
  img = pygame.transform.scale(img, (40, 40))
  ecran.blit(img, (30, 30+3*15+3*h_carte + 10))

  rect = pygame.Rect(30,30+3*15+3*h_carte + 10 +40, 4*l_carte+140, 30)
  pygame.draw.rect(ecran, "grey24", rect)
  pygame.display.flip()


def souris_sur_aide(ecran, h_carte):
  """
  Renvoie vrai si la souris se trouve sur l'aide, faux sinon
  """
  pos = pygame.mouse.get_pos()
  if (30<pos[0]<30+40) and (30+3*15+3*h_carte + 10<pos[1]<30+3*15+3*h_carte + 10+40):
    return True
  else:
    return False

def affiche_page_autre_joueur(ecran,tab_joueurs):
  """
  Affiche l'écran qui permet de voir les autres jeux des joueurs
  """
  HAUTEUR = ecran.get_height()
  LARGEUR = ecran.get_width()
  ecran.fill("grey24")
  ch = "images/fermer.png"
  img = pygame.image.load(ch)
  img = pygame.transform.scale(img, (30,30))
  ecran.blit(img, (ecran.get_width()-80, 30))

  ch="images/suiv.png"
  img=pygame.image.load(ch)
  img = pygame.transform.scale(img, (80,50))
  ecran.blit(img,(LARGEUR//8, 130+(3*tab_joueurs[0].jeu_actuel[0][0].hauteur//2)))
  ch="images/suiv.png"
  img=pygame.image.load(ch)
  img = pygame.transform.scale(img, (80,50))
  img=pygame.transform.rotate(img,180)
  ecran.blit(img,(LARGEUR//4 + 4 *(tab_joueurs[0].jeu_actuel[0][0].largeur)+50, 130+(3*tab_joueurs[0].jeu_actuel[0][0].hauteur//2)))


def voir_autre_jeu(ecran,tab_joueurs,i_joueur):
  """
  Affiche les jeux des autres joueurs
  """
  HAUTEUR = ecran.get_height()
  LARGEUR = ecran.get_width()
  h = tab_joueurs[0].jeu_actuel[0][0].hauteur
  l = tab_joueurs[0].jeu_actuel[0][0].largeur
  click_croix=False
  affiche_page_autre_joueur(ecran,tab_joueurs)
  pygame.event.get()
  souris = pygame.mouse.get_pressed()
  tab_joueurs[i_joueur].affiche_jeu_vision_ext(ecran)
  font=pygame.font.Font(None, 35)
  text=font.render("Joueur n°"+str(i_joueur+1),1, "white")
  ecran.blit(text,(LARGEUR//4 + l +20-30+l//2,150 + 3 * h +3*20))

  pygame.display.flip()

  #si on clique sur la croix
  if souris[0]:
    pos = pygame.mouse.get_pos()
    if ((LARGEUR-80 < pos[0] < LARGEUR-50) and (30 < pos[1] < 60)):  
      click_croix=True
      ecran.fill("grey24")
      ch = "images/loupe.png"
      img = pygame.image.load(ch)
      img = pygame.transform.scale(img, (50,50))
      ecran.blit(img, (LARGEUR-80, 30))
      pygame.display.flip()
    
    elif ((LARGEUR//8 < pos[0] < LARGEUR//8+80) and (130+(3*h//2 < pos[1] < 180+(3*h//2)))):
      i_joueur=(i_joueur-1)%len(tab_joueurs)
     
    elif ((LARGEUR//4 + 4 *l+50 < pos[0] < LARGEUR//4 + 4 *l+130) and (130+(3*h//2 < pos[1] < 180+(3*h//2)))):
      i_joueur=(i_joueur+1)%len(tab_joueurs)
     

  return click_croix,i_joueur
