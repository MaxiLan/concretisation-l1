import pygame
import partie as P
import carte
import defausse
import pioche
import robot

def actions_tour(joueur,partie, ecran):
    """
    Gère toutes les actions du tour 
    """
    #variables nécessaires
    P.verifie_fermeture()
    HAUTEUR = ecran.get_height()
    LARGEUR = ecran.get_width()
    h = partie.defausse.cartes[0].hauteur
    l = partie.defausse.cartes[0].largeur
    x_defausse, y_defausse = partie.defausse.abs, partie.defausse.ord
    x_pioche, y_pioche = partie.pioche.abs, partie.pioche.ord
    ecart = LARGEUR//2 - 2*l - 30
    
    click_carte = False
  
    #affiche ou cache l'aide
    if souris_sur_aide(ecran, h):
        affiche_aide(ecran, h, section=0)
    else:
        cache_aide(ecran, l,h)
    
    #si le joueur est un robot     
    if isinstance(joueur,robot.Robot):
        pos = joueur.choix_pioche_def(partie)
        pos[0]=pos[0]+10
        pos[1]=pos[1]+10

        pygame.time.wait(500)
        pygame.event.get()
    else:
        #attend un click (sinon la fonction sera ré-executer) 
        pygame.event.get()

        souris = pygame.mouse.get_pressed()
        if souris[0]:
            pos = pygame.mouse.get_pos()

        #sinon on renvoie False, et la fonction sera rappelée  
        else:
            return False
      
    #si le click est sur la défausse
    if (x_defausse < pos[0] < x_defausse+l) and (y_defausse< pos[1] < y_defausse+h):

        if not (isinstance(joueur,robot.Robot)):
          pygame.event.get()
          s = pygame.mouse.get_pressed()

          if s[0]:
            pos = pygame.mouse.get_pos()
            if (LARGEUR-80< pos[0] < LARGEUR-30) and (30 < pos[1] < 80):
              appel_loupe(ecran,partie,joueur)

        #on déplace la carte de la defausse
        carte_select = partie.defausse.retire_carte()
        partie.carte_en_main="images/" + str(carte_select.num) + ".png"
        carte.actualise_carte_en_main(ecran,partie)
        partie.defausse.affiche(ecran)
        pygame.display.flip()

        #on attend la décision du joueur (carte à échanger)
        while (not click_carte):
            P.verifie_fermeture()

            if isinstance(joueur,robot.Robot):
                pygame.time.wait(700)
                pygame.event.get()
                pos=joueur.choix_placement_carte(carte_select,partie)
                partie.carte_en_main="images/carte_selectionnee.png"
                click_carte = True
                partie.carte_en_main="images/carte_selectionnee.png"
                aux = joueur.jeu_actuel[pos[0]][pos[1]]
                joueur.jeu_actuel[pos[0]][pos[1]] = carte_select
                joueur.jeu_actuel[pos[0]][pos[1]].etat = "ouverte"
                partie.defausse.ajout_carte(aux)
                carte.actualise_carte_en_main(ecran,partie)
                return True

            else:
                if souris_sur_aide(ecran,h):
                    affiche_aide(ecran,h, section=1)
                else:
                    cache_aide(ecran,l, h)
            
            pygame.event.get()
            s = pygame.mouse.get_pressed()

            if s[0]:
                pos = pygame.mouse.get_pos()

                if (LARGEUR-80< pos[0] < LARGEUR-30) and (30 < pos[1] < 80):
                    appel_loupe(ecran,partie,joueur)
                    pygame.time.wait(200)

                #on cherche le click sur une carte
                for i in range(3):
                    for j in range(4):
                        if (ecart + j * l+j*20< pos[0] <ecart + j * l+j*20 + l) and (30 + i * h+i*15< pos[1] <  30 + i * h+i*15 + h):
                            #on échange les cartes
                            if joueur.jeu_actuel[i][j].num!="42bis":
                                partie.carte_en_main="images/carte_selectionnee.png"
                                aux = joueur.jeu_actuel[i][j]
                                joueur.jeu_actuel[i][j] = carte_select
                                joueur.jeu_actuel[i][j].etat = "ouverte"
                                partie.defausse.ajout_carte(aux)
                                carte.actualise_carte_en_main(ecran,partie)
                                return True


    #sinon si le click est sur la pioche
    elif (x_pioche< pos[0] < x_pioche+l and y_pioche< pos[1] < y_pioche+h):
        if not isinstance(joueur,robot.Robot):
            pygame.event.get()
            s = pygame.mouse.get_pressed()
            if s[0]:
              pos = pygame.mouse.get_pos()
              if (LARGEUR-80< pos[0] < LARGEUR-30) and (30 < pos[1] < 80):
                appel_loupe(ecran,partie,joueur)

        # on deplace la carte de la pioche
        carte_select = partie.pioche.cartes[0]
        carte_select.etat = "ouverte"
        partie.pioche.cartes.pop(0)
        partie.pioche.est_vide(partie.defausse)
        partie.pioche.affiche(ecran)
        partie.carte_en_main= "images/" + str(carte_select.num) + ".png"
        carte.actualise_carte_en_main(ecran,partie)
        pygame.display.flip()

        click_defausse = False
        #on attend le choix du joueur (jouer sur son jeu ou sur la défausse)
        while not (click_carte or click_defausse): 
            P.verifie_fermeture()

            if souris_sur_aide(ecran, h):
                affiche_aide(ecran, h, section=2) 
            else:
                cache_aide(ecran,l, h)
            if isinstance(joueur,robot.Robot):
                pygame.time.wait(300)
                pygame.event.get()
                pos=joueur.choix_placement_carte(carte_select,partie)
                if pos[0]==-1:
                    partie.carte_en_main="images/carte_selectionnee.png"
                    partie.defausse.ajout_carte(carte_select)
                    partie.defausse.affiche(ecran)
                    carte.actualise_carte_en_main(ecran,partie)
                    pygame.display.flip()
                    click_defausse = True
                    pygame.time.wait(300)

                    pos=joueur.retourne_hasard()
                    joueur.jeu_actuel[pos[0]][pos[1]].etat = "ouverte"
                    carte_selectionner = True
                    pygame.display.flip()
                    #on retourne une carte selectionnnée par le joueur
                    return True
                else:
                    partie.carte_en_main="images/carte_selectionnee.png"
                    carte.actualise_carte_en_main(ecran,partie)
                    click_carte = True
                    aux = joueur.jeu_actuel[pos[0]][pos[1]]
                    joueur.jeu_actuel[pos[0]][pos[1]] = carte_select
                    joueur.jeu_actuel[pos[0]][pos[1]].etat = "ouverte"
                    partie.defausse.ajout_carte(aux)
                    return True
            else:
                pygame.event.get()
                s = pygame.mouse.get_pressed()
                if s[0]:
                    pos = pygame.mouse.get_pos()
                
                    #si le click est sur le jeu du joueur
                    for i in range(3):
                        for j in range(4):
                            if (ecart + j *l+j*20< pos[0] <ecart + j * l+j*20 + l) and (30 + i * h+i*15< pos[1] <  30 + i * h+i*15 +h):

                                #on echange les cartes
                                if joueur.jeu_actuel[i][j].num != "42bis":
                                    partie.carte_en_main="images/carte_selectionnee.png"
                                    click_carte = True
                                    aux = joueur.jeu_actuel[i][j]
                                    joueur.jeu_actuel[i][j] = carte_select
                                    joueur.jeu_actuel[i][j].etat = "ouverte"
                                    partie.defausse.ajout_carte(aux)
                                    carte.actualise_carte_en_main(ecran, partie)
                                    return True
                    if (LARGEUR-80< pos[0] < LARGEUR-30) and (30 < pos[1] < 80):
                        appel_loupe(ecran,partie,joueur)

              
                #si le click est sur la defausse
                if (x_defausse< pos[0] < x_defausse+l) and (y_defausse< pos[1] < y_defausse+h):
                    partie.carte_en_main="images/carte_selectionnee.png"
                    partie.defausse.ajout_carte(carte_select)
                    partie.defausse.affiche(ecran)
                    carte.actualise_carte_en_main(ecran,partie)
                    pygame.display.flip()
                    click_defausse = True
                    #on retourne une carte selectionnnée par le joueur
                    return retourne_cartes(joueur, ecran,partie)
        
    #si le joueur clique sur la loupe 
    elif (LARGEUR-80< pos[0] < LARGEUR-30) and (30 < pos[1] < 80):
        appel_loupe(ecran,partie,joueur)
  

def retourne_cartes(joueur, ecran,partie): 
    """
    Retourne une carte dans le jeu du joueur
    """
    HAUTEUR = ecran.get_height()
    LARGEUR = ecran.get_width()
    h = joueur.jeu_actuel[0][0].hauteur
    l = joueur.jeu_actuel[0][0].largeur 
    ecart = LARGEUR//2 - 2*l - 30

    carte_selectionner = False

    while not (carte_selectionner):
        P.verifie_fermeture()
        if souris_sur_aide(ecran, h):
            affiche_aide(ecran, h, section=3) 
        else:
            cache_aide(ecran,l,h)
        pygame.event.get()
        s = pygame.mouse.get_pressed()

        if s[0]:
            pos = pygame.mouse.get_pos()
            if (LARGEUR-80< pos[0] < LARGEUR-30) and (30 < pos[1] < 80):
                appel_loupe(ecran,partie,joueur)

            for i in range(3):
                for j in range(4):
                    if(ecart + j * l+j*20< pos[0] <30 + j * l+j*20 +l) and (ecart + i * h+i*15< pos[1] <  30 + i * h+i*15 + h):
                        if joueur.jeu_actuel[i][j].etat != "ouverte":
                            joueur.jeu_actuel[i][j].etat = "ouverte"
                            carte_selectionner = True
    return True


def affiche_aide(ecran, h_carte, section):
    """
    Affiche de l'aide si le joueur place sa souris sur le point d'intérrogation
    """
    img = pygame.image.load("images/question.png")
    img = pygame.transform.scale(img, (50, 50))
    ecran.blit(img, (30, ecran.get_height()-80))
    objet_texte = pygame.font.Font(None, 32)

    if section==0:
        texte="Prenez une carte de la défausse ou de la pioche"
    elif section==1:
        texte="Echangez avec une de vos cartes"
    elif section==2:
        texte="Placez la dans le défausse ou votre jeu"
    elif section==3:
        texte="Retournez maintenant une carte"
    
    ecran.blit(objet_texte.render(texte, True, "white"), (30, ecran.get_height()-110))


def cache_aide(ecran, l_carte, h_carte):
    """
    Cache l'aide si le joueur a enlevé sa souris de l'aide
    """
    img = pygame.image.load("images/question.png")
    img = pygame.transform.scale(img, (50, 50))
    ecran.blit(img, (30, ecran.get_height()-80))

    rect = pygame.Rect(30, ecran.get_height()-110, 510, 25)
    pygame.draw.rect(ecran, "grey24", rect)


def souris_sur_aide(ecran, h_carte):
    """
    Renvoie vrai si la souris se trouve sur l'aide, faux sinon
    """
    pos = pygame.mouse.get_pos()
    return (30<pos[0]<80) and (ecran.get_height()-80<pos[1]<ecran.get_height()-30)


def appel_loupe(ecran,partie,joueur, section="jeu"):
    click_croix=False
    i_joueur=0
    pygame.time.wait(200)

    while not click_croix:
        P.verifie_fermeture()
        click_croix,i_joueur=voir_autre_jeu(ecran,partie.tab_joueurs,i_joueur)
        
    if section=="jeu":
        j_precedent = partie.tab_joueurs[joueur.nom - 2]
        j_suivant = partie.tab_joueurs[joueur.nom%len(partie.tab_joueurs)]

        font1=pygame.font.Font(None, 35)
        font1.underline = True

        text1=font1.render("Joueur n°"+str(joueur.nom),1, "white")
        ecran.blit(text1,(ecran.get_width()//2-61,15))
        
        joueur.affiche_jeu(ecran)
        partie.pioche.affiche(ecran)
        partie.defausse.affiche(ecran)
        carte.actualise_carte_en_main(ecran,partie)

        font2=pygame.font.Font(None, 35)
        if len(partie.tab_joueurs)==2:
            j_suivant.affiche_petit(ecran, 'd')
            text2=font2.render("Joueur n°"+str(j_suivant.nom),1, "white")
            ecran.blit(text2,((ecran.get_width()-60-30-2*73)-61,150))

        if len(partie.tab_joueurs)>2:
            j_precedent.affiche_petit(ecran, 'g')
            text2=font2.render("Joueur n°"+str(j_precedent.nom),1, "white")
            ecran.blit(text2,((60+30+2*73)-61,150))

            j_suivant.affiche_petit(ecran, 'd')
            text3=font2.render("Joueur n°"+str(j_suivant.nom),1, "white")
            ecran.blit(text3,((ecran.get_width()-60-30-2*73)-61,150))
        
        pygame.display.flip()
        pygame.time.wait(200)


def affiche_page_autre_joueur(ecran,tab_joueurs):
    """
    Affiche l'écran qui permet de voir les autres jeux des joueurs
    """
    HAUTEUR = ecran.get_height()
    LARGEUR = ecran.get_width()
    h = tab_joueurs[0].jeu_actuel[0][0].hauteur
    l = tab_joueurs[0].jeu_actuel[0][0].largeur

    ecran.fill("grey24")
    ch = "images/fermer.png"
    img = pygame.image.load(ch)
    img = pygame.transform.scale(img, (30,30))
    ecran.blit(img, (ecran.get_width()-80, 30))

    ch="images/suiv.png"
    img=pygame.image.load(ch)
    img = pygame.transform.scale(img, (80,50))
    ecran.blit(img,(LARGEUR//2 - 80 - 60 - 2*l, 130+(3*h//2)))

    ch="images/suiv.png"
    img=pygame.image.load(ch)
    img = pygame.transform.scale(img, (80,50))
    img=pygame.transform.rotate(img,180)
    ecran.blit(img,(LARGEUR//2 + 2*l + 60, 130+(3*h//2)))


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
    tab_joueurs[i_joueur].affiche_jeu(ecran)
    font=pygame.font.Font(None, 35)
    text=font.render("Joueur n°"+str(i_joueur+1),1, "white")
    ecran.blit(text,(ecran.get_width()//2-61,150 + 3 * h +3*20))

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
        
        elif ((LARGEUR//2 - 80 - 60 - 2*l < pos[0] < LARGEUR//2 - 60 - 2*l) and (130+(3*h//2 < pos[1] < 180+(3*h//2)))):
            i_joueur=(i_joueur-1)%len(tab_joueurs)
        
        elif ((LARGEUR//2 + 2*l + 60 < pos[0] < LARGEUR//2 + 2*l + 140) and (130+(3*h//2 < pos[1] < 180+(3*h//2)))):
            i_joueur=(i_joueur+1)%len(tab_joueurs)
        
        pygame.time.wait(200)
        

    return click_croix,i_joueur