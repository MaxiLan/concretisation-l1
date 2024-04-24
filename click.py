import pygame
import carte
import defausse
import pioche


#choix entre pioche et défausse (1er et 2e click)
def click_pioche_defausse(joueur, p, d, ecran,tab_joueurs): 

  print("je devrais pas etre la ")
  HAUTEUR = ecran.get_height()
  LARGEUR = ecran.get_width()
  click_carte = False
  pygame.event.get()
  souris = pygame.mouse.get_pressed()

  if souris_sur_aide(ecran, d.cartes[0].hauteur):
    affiche_aide(ecran, d.cartes[0].hauteur, section=0)
  else:
    cache_aide(ecran, d.cartes[0].largeur, d.cartes[0].hauteur)
  
  #attend un click (sinon la fonction sera ré-executer) 
  if souris[0]:
    pos = pygame.mouse.get_pos()

    #si le click est sur la défausse
    if (LARGEUR- 2*d.cartes[0].largeur - 50< pos[0] < LARGEUR-50-d.cartes[0].largeur) and (HAUTEUR-30-d.cartes[0].hauteur < pos[1] < HAUTEUR-30):
      
      #on deplace la carte de la defausse
      carte_select = d.retire_carte()
      ch = "images/" + str(carte_select.num) + ".png"
      img = pygame.image.load(ch)
      img = pygame.transform.scale(img, (d.cartes[0].largeur,d.cartes[0].hauteur))
      ecran.blit(img, (LARGEUR - 40 - d.cartes[0].largeur - d.cartes[0].largeur//2, HAUTEUR-50-2*d.cartes[0].hauteur))
      d.affiche(ecran)
      pygame.display.flip()

      #on attend la décision du joueur (carte à échanger)
      while (not click_carte):

        if souris_sur_aide(ecran,d.cartes[0].hauteur):
          affiche_aide(ecran, d.cartes[0].hauteur, section=1)
        else:
          cache_aide(ecran,d.cartes[0].largeur,  d.cartes[0].hauteur)
      
        pygame.event.get()
        s = pygame.mouse.get_pressed()

        if s[0]:
          pos = pygame.mouse.get_pos()
          
          #on regarde si le click est sur une carte
          for i in range(3):
            for j in range(4):
              if (30 + j * d.cartes[0].largeur+j*20< pos[0] <30 + j * d.cartes[0].largeur+j*20 + d.cartes[0].largeur) and (30 + i * d.cartes[0].hauteur +i*15< pos[1] <  30 + i * d.cartes[0].hauteur +i*15 + d.cartes[0].hauteur):

                #on échange les cartes
                #click_carte = True
                if joueur.jeu_actuel[i][j].num!="42bis":
                  aux = joueur.jeu_actuel[i][j]
                  joueur.jeu_actuel[i][j] = carte_select
                  joueur.jeu_actuel[i][j].etat = "ouverte"
                  d.ajout_carte(aux)
                  carte.cacher_carte(ecran,d.cartes[0])
                  pygame.display.flip()
                  return True

    #sinon si le click est sur la pioche
    elif (LARGEUR-30-d.cartes[0].largeur< pos[0] < LARGEUR-30 and HAUTEUR-30-d.cartes[0].hauteur< pos[1] < HAUTEUR-30):
      
      # on deplace la carte de la pioche
      carte_select = p.cartes[0]
      carte_select.etat = "ouverte"
      p.cartes.pop(0)
      p.affiche(ecran)
      ch = "images/" + str(carte_select.num) + ".png"
      img = pygame.image.load(ch)
      img = pygame.transform.scale(img, (d.cartes[0].largeur, d.cartes[0].hauteur))
      ecran.blit(img, (LARGEUR - 40 - d.cartes[0].largeur - d.cartes[0].largeur//2, HAUTEUR-50-2*d.cartes[0].hauteur))
      pygame.display.flip()

      click_defausse = False
      #on attend le choix du joueur (jouer sur son jeu ou sur la defausse)
      while not (click_carte or click_defausse): 

        if souris_sur_aide(ecran, d.cartes[0].hauteur):
          affiche_aide(ecran, d.cartes[0].hauteur, section=2) 
        else:
          cache_aide(ecran,d.cartes[0].largeur, d.cartes[0].hauteur)

        pygame.event.get()
        s = pygame.mouse.get_pressed()

        if s[0]:
          pos = pygame.mouse.get_pos()

          #si le click est sur le jeu du joueur
          for i in range(3):
            for j in range(4):
              if(30 + j * d.cartes[0].largeur+j*20< pos[0] <30 + j * d.cartes[0].largeur+j*20 + d.cartes[0].largeur) and (30 + i * d.cartes[0].hauteur +i*15< pos[1] <  30 + i * d.cartes[0].hauteur +i*15 + d.cartes[0].hauteur):

                #on echange les cartes
                if joueur.jeu_actuel[i][j].num != "42bis":
                  click_carte = True
                  aux = joueur.jeu_actuel[i][j]
                  joueur.jeu_actuel[i][j] = carte_select
                  joueur.jeu_actuel[i][j].etat = "ouverte"
                  d.ajout_carte(aux)
                  carte.cacher_carte(ecran, d.cartes[0])
                  return True
          
          #si le click est sur la defausse
          if (LARGEUR- 2*d.cartes[0].largeur - 50< pos[0] < LARGEUR-50-d.cartes[0].largeur) and (HAUTEUR-30-d.cartes[0].hauteur < pos[1] < HAUTEUR-30):
            
           

            d.ajout_carte(carte_select)
            d.affiche(ecran)
            carte.cacher_carte(ecran,d.cartes[0])
            pygame.display.flip()
            click_defausse = True
            
            #et on retourne une carte selectionnnée par le joueur (fonction ci-dessous)
            return retourne_cartes(joueur, ecran)
    elif ( ecran.get_width()-80< pos[0] < ecran.get_width()-30) and (30 < pos[1] < 80):
        click_croix=False
        while not click_croix:
          click_croix=voir_autre_jeu(ecran,tab_joueurs)
      
  else:
    #sinon on renvoie False, et la fonction sera rappelée
    return False


#fonction annexe (utilisée ci-dessus)
def retourne_cartes(joueur, ecran): 
  HAUTEUR = ecran.get_height()
  LARGEUR = ecran.get_width()
  carte_selectionner = False
  while not (carte_selectionner): 
    if souris_sur_aide(ecran, joueur.jeu_actuel[0][0].hauteur): # joueur.jeu_atuel[0] NOUS PERMET DE RECUPERER LA TAILLE D'UNE CARTE CHOIX ARBITRAIRE D'UNE CARTE
      affiche_aide(ecran, joueur.jeu_actuel[0][0].hauteur, section=3) 
    else:
      cache_aide(ecran,joueur.jeu_actuel[0][0].largeur ,joueur.jeu_actuel[0][0].hauteur)
    pygame.event.get()
    s = pygame.mouse.get_pressed()

    if s[0]:
      pos = pygame.mouse.get_pos()
      for i in range(3):
        for j in range(4):
          if(30 + j * joueur.jeu_actuel[0][0].largeur+j*20< pos[0] <30 + j * joueur.jeu_actuel[0][0].largeur+j*20 +joueur.jeu_actuel[0][0].largeur) and (30 + i * joueur.jeu_actuel[0][0].hauteur +i*15< pos[1] <  30 + i * joueur.jeu_actuel[0][0].hauteur +i*15 + joueur.jeu_actuel[0][0].hauteur):
          #if (25 + j * 130 < pos[0] < 135 + j * 130) and (30 + i * 175 < pos[1]< 190 + i * 175):
            if joueur.jeu_actuel[i][j].etat != "ouverte":
              joueur.jeu_actuel[i][j].etat = "ouverte"
              carte_selectionner = True

  return True


def affiche_aide(ecran, h_carte, section):
  img = pygame.image.load("images/question.png")
  img = pygame.transform.scale(img, (40, 40))
  ecran.blit(img, (30, 30+3*15+3*h_carte + 10))
  objet_texte = pygame.font.Font(None, 28)

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
  img = pygame.image.load("images/question.png")
  img = pygame.transform.scale(img, (40, 40))
  ecran.blit(img, (30, 30+3*15+3*h_carte + 10))

  rect = pygame.Rect(30,30+3*15+3*h_carte + 10 +40, 4*l_carte+140, 30)
  pygame.draw.rect(ecran, "grey24", rect)
  pygame.display.flip()


def souris_sur_aide(ecran, h_carte):
  pos = pygame.mouse.get_pos()
  if (30<pos[0]<30+40) and (30+3*15+3*h_carte + 10<pos[1]<30+3*15+3*h_carte + 10+40):
    return True
  else:
    return False

def voir_autre_jeu(ecran,tab_joueurs):

  click_croix=False
  ecran.fill("grey24")
  ch = "images/fermer.png"
  pygame.time.wait(200)
  img = pygame.image.load(ch)
  img = pygame.transform.scale(img, (30,30))
  ecran.blit(img, (ecran.get_width()-80, 30))
  pygame.display.flip()
  pygame.event.get()
  souris = pygame.mouse.get_pressed()
  if souris[0]:
    pos = pygame.mouse.get_pos()
    while not ((ecran.get_width()-80 < pos[0] < ecran.get_width()-50) and (30 < pos[1] < 60)):   
      ecran.fill("blue")
      ch = "images/fermer.png"
      img = pygame.image.load(ch)
      img = pygame.transform.scale(img, (50,50))
      ecran.blit(img, (ecran.get_width()-80, 30))
    click_croix=True
    pygame.time.wait(250)
    ch = "images/loupe.png"
    img = pygame.image.load(ch)
    img = pygame.transform.scale(img, (50,50))
    ecran.blit(img, (ecran.get_width()-80, 30))
  return click_croix