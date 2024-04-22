import pygame
import carte
import defausse
import pioche


#choix entre pioche et défausse (1er et 2e click)
def click_pioche_defausse(joueur, p, d, ecran): 
  HAUTEUR = ecran.get_height()
  LARGEUR = ecran.get_width()
  facteur = HAUTEUR/850
  h_carte = 160 * facteur
  l_carte = 110 * facteur

  click_carte = False
  pygame.event.get()
  souris = pygame.mouse.get_pressed()

  if souris_sur_aide(ecran, h_carte):
    affiche_aide(ecran, h_carte, section=0)
  else:
    cache_aide(ecran, l_carte, h_carte)
  
  #attend un click (sinon la fonction sera ré-executer) 
  if souris[0]:
    pos = pygame.mouse.get_pos()

    #si le click est sur la défausse
    if (LARGEUR- 2*l_carte - 50< pos[0] < LARGEUR-30-20-l_carte) and (HAUTEUR-30-h_carte < pos[1] < HAUTEUR-30):
      
      #on deplace la carte de la defausse
      carte_select = d.retire_carte()
      ch = "images/" + str(carte_select.num) + ".png"
      img = pygame.image.load(ch)
      img = pygame.transform.scale(img, (l_carte, h_carte))
      ecran.blit(img, (LARGEUR - 30 - l_carte - 10 - l_carte//2, HAUTEUR-50-2*h_carte))
      d.affiche(ecran)
      pygame.display.flip()

      #on attend la décision du joueur (carte à échanger)
      while (not click_carte):

        if souris_sur_aide(ecran, h_carte):
          affiche_aide(ecran, h_carte, section=1)
        else:
          cache_aide(ecran,l_carte,  h_carte)
      
        pygame.event.get()
        s = pygame.mouse.get_pressed()

        if s[0]:
          pos = pygame.mouse.get_pos()
          
          #on regarde si le click est sur une carte
          for i in range(3):
            for j in range(4):
              if (30 + j * l_carte+j*20< pos[0] <30 + j * l_carte+j*20 + l_carte) and (30 + i * h_carte +i*15< pos[1] <  30 + i * h_carte +i*15 + h_carte):

                #on échange les cartes
                #click_carte = True
                if joueur.jeu_actuel[i][j].num!="42bis":
                  aux = joueur.jeu_actuel[i][j]
                  joueur.jeu_actuel[i][j] = carte_select
                  joueur.jeu_actuel[i][j].etat = "ouverte"
                  d.ajout_carte(aux)
                  carte.cacher_carte(ecran)
                  pygame.display.flip()
                  return True

    #sinon si le click est sur la pioche
    elif (LARGEUR-30-l_carte< pos[0] < LARGEUR-30 and HAUTEUR-30-h_carte< pos[1] < HAUTEUR-30):
      
      # on deplace la carte de la pioche
      carte_select = p.cartes[0]
      carte_select.etat = "ouverte"
      p.cartes.pop(0)
      p.affiche(ecran)
      ch = "images/" + str(carte_select.num) + ".png"
      img = pygame.image.load(ch)
      img = pygame.transform.scale(img, (l_carte, h_carte))
      ecran.blit(img, (LARGEUR - 30 - l_carte - 10 - l_carte//2, HAUTEUR-50-2*h_carte))
      pygame.display.flip()

      click_defausse = False
      #on attend le choix du joueur (jouer sur son jeu ou sur la defausse)
      while not (click_carte or click_defausse): 

        if souris_sur_aide(ecran, h_carte):
          affiche_aide(ecran, h_carte, section=2) 
        else:
          cache_aide(ecran,l_carte,  h_carte)

        pygame.event.get()
        s = pygame.mouse.get_pressed()

        if s[0]:
          pos = pygame.mouse.get_pos()

          #si le click est sur le jeu du joueur
          for i in range(3):
            for j in range(4):
              if(30 + j * l_carte+j*20< pos[0] <30 + j * l_carte+j*20 + l_carte) and (30 + i * h_carte +i*15< pos[1] <  30 + i * h_carte +i*15 + h_carte):

                #on echange les cartes
                if joueur.jeu_actuel[i][j].num != "42bis":
                  click_carte = True
                  aux = joueur.jeu_actuel[i][j]
                  joueur.jeu_actuel[i][j] = carte_select
                  joueur.jeu_actuel[i][j].etat = "ouverte"
                  d.ajout_carte(aux)
                  carte.cacher_carte(ecran)
                  return True
          
          #si le click est sur la defausse
          if (LARGEUR- 2*l_carte - 50< pos[0] < LARGEUR-30-20-l_carte) and (HAUTEUR-30-h_carte < pos[1] < HAUTEUR-30):
            
           

            d.ajout_carte(carte_select)
            d.affiche(ecran)
            carte.cacher_carte(ecran)
            pygame.display.flip()
            click_defausse = True
            
            #et on retourne une carte selectionnnée par le joueur (fonction ci-dessous)
            return retourne_cartes(joueur, ecran)

  else:
    #sinon on renvoie False, et la fonction sera rappelée
    return False


#fonction annexe (utilisée ci-dessus)
def retourne_cartes(joueur, ecran): 
  HAUTEUR = ecran.get_height()
  LARGEUR = ecran.get_width()
  facteur = HAUTEUR/850
  h_carte = 160 * facteur
  l_carte = 110 * facteur

  carte_selectionner = False
  while not (carte_selectionner): 
    if souris_sur_aide(ecran, h_carte):
      affiche_aide(ecran, h_carte, section=3) 
    else:
      cache_aide(ecran,l_carte ,h_carte)
    pygame.event.get()
    s = pygame.mouse.get_pressed()

    if s[0]:
      pos = pygame.mouse.get_pos()
      for i in range(3):
        for j in range(4):
          if(30 + j * l_carte+j*20< pos[0] <30 + j * l_carte+j*20 + l_carte) and (30 + i * h_carte +i*15< pos[1] <  30 + i * h_carte +i*15 + h_carte):
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
