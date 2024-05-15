import pygame
import partie

def affiche_accueil(ecran):
  """
  Affiche le titre et permet de choisir le nombre de joueur
  """

  nb_joueurs = 2
  nb_robots = 0
  niveau = 1
  robot = False

  nb_choisi = False

  while not nb_choisi:  
    if nb_robots>nb_joueurs:
      nb_robots = nb_joueurs
    affiche_elements(ecran, nb_joueurs, nb_robots, niveau)
    nb_joueurs, nb_choisi, nb_robots, niveau = click(ecran, nb_joueurs, nb_robots, niveau)

  return nb_joueurs, nb_robots, niveau


def affiche_elements(ecran, nb_joueurs, nb_robots, niveau):
  """
  Affiche tous les éléments nécessaires pour l'accueil
  """
  ecran.fill((43, 42, 76))

  H = ecran.get_height()
  L = ecran.get_width()
  milieu_l = L // 2

  #titre
  img = pygame.image.load("images/titre.png")
  img = pygame.transform.scale(img, (500 , 250))

  ecran.blit(img, (milieu_l - 250, 50))
  
  #signe moins
  img = pygame.image.load("images/moins.png")
  img = pygame.transform.scale(img, (50 , 50))

  ecran.blit(img, (milieu_l - 250, 400))
  ecran.blit(img, (milieu_l - 250, 570))
  ecran.blit(img, (milieu_l - 250, 740))

  #signe plus
  img = pygame.image.load("images/plus.png")
  img = pygame.transform.scale(img, (50 , 50))

  ecran.blit(img, (milieu_l + 200, 400))
  ecran.blit(img, (milieu_l + 200, 570))
  ecran.blit(img, (milieu_l + 200, 740))

  #commencer la partie
  rect = pygame.Rect(L-470, H-80, 454, 60)
  objet_font1 =  pygame.font.Font(None, 50)
  pygame.draw.rect(ecran, "white", rect, 2)
  ecran.blit(objet_font1.render("Cliquer pour commencer", True, "white"), (L-450, H-70))

  #nb joueurs
  objet_font2 = pygame.font.Font(None, 70)
  ecran.blit(objet_font2.render(str(nb_joueurs), True, "white"), (milieu_l - 15, 400))
  ecran.blit(objet_font1.render("Nombre de joueurs :", True, "white"), (milieu_l-169, 330))

  #robot
  ecran.blit(objet_font1.render("Nombre de robots : ", True, "white"), (milieu_l-169, 500))
  ecran.blit(objet_font2.render(str(nb_robots), True, "white"), (milieu_l-15, 570))
  
  #difficulté
  ecran.blit(objet_font1.render("Niveau des robots (1-3) :", True, "white"), (milieu_l-201, 670))
  ecran.blit(objet_font2.render(str(niveau), True, "white"), (milieu_l-15, 740))

  pygame.display.flip()


def click(ecran, nb_joueurs, nb_robots, niveau): 
  """
  Change le nombre de joueur selon s'il clique si + ou -
  """
  H = ecran.get_height()
  L = ecran.get_width()
  milieu_l = L // 2

  click_souris = False
  
  while not click_souris:
    pygame.event.get()
    partie.verifie_fermeture()
    s = pygame.mouse.get_pressed()

    if s[0]:
      pos = pygame.mouse.get_pos()
      
      #click nb_joueurs
      if (milieu_l+200<pos[0]<milieu_l+250) and (400<pos[1]<450):
        click_souris = True
        if nb_joueurs<8:
          nb_joueurs += 1
        pygame.time.wait(200)
        return nb_joueurs, False, nb_robots, niveau


      if (milieu_l - 250 <pos[0]< milieu_l - 200) and (400<pos[1]<450):
        click_souris = True
        if nb_joueurs>1:
          nb_joueurs -= 1
        pygame.time.wait(200)
        return nb_joueurs, False, nb_robots, niveau

      
      #click nb_robots
      if (milieu_l - 250<pos[0]<milieu_l - 200) and (570<pos[1]<620):
        click_souris = True
        if nb_robots>0:
          nb_robots -= 1
        pygame.time.wait(200)
        return nb_joueurs, False, nb_robots, niveau


      if (milieu_l+200 <pos[0]< milieu_l+250) and (570<pos[1]<620):
        click_souris = True
        if nb_robots<nb_joueurs:
          nb_robots+= 1
        pygame.time.wait(200)
        return nb_joueurs, False, nb_robots, niveau
      
      #click niveau
      if (milieu_l - 250<pos[0]<milieu_l - 200) and (740<pos[1]<790):
        click_souris = True
        if niveau>1:
          niveau-= 1
        pygame.time.wait(200)
        return nb_joueurs, False, nb_robots, niveau


      if (milieu_l+200 <pos[0]< milieu_l+250) and (740<pos[1]<790):
        click_souris = True
        if niveau<2:
          niveau+= 1
        pygame.time.wait(200)
        return nb_joueurs, False, nb_robots, niveau

      if (L-470<pos[0]<L-20) and (H-80<pos[1]<H-20):
        click_souris = True
        pygame.time.wait(250)
        return nb_joueurs, True, nb_robots, niveau
