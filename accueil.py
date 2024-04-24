import pygame

def affiche_accueil(ecran):
  nb_joueurs = 2

  nb_choisi = False

  while not nb_choisi:  
    ecran.fill("grey24")
    affiche_elements(ecran, nb_joueurs)
    nb_joueurs, nb_choisi = click(ecran, nb_joueurs)

  return nb_joueurs


def affiche_elements(ecran, nb_joueurs):
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

  #signe plus
  img = pygame.image.load("images/plus.png")
  img = pygame.transform.scale(img, (50 , 50))

  ecran.blit(img, (milieu_l + 200, 400))

  #commencer la partie
  rect = pygame.Rect(L-470, H-80, 454, 60)
  objet_font1 =  pygame.font.Font(None, 50)
  pygame.draw.rect(ecran, "white", rect, 2)
  ecran.blit(objet_font1.render("Cliquer pour commencer", True, "white"), (L-450, H-70))

  #nb joueurs
  objet_font2 = pygame.font.Font(None, 70)
  ecran.blit(objet_font2.render(str(nb_joueurs), True, "white"), (milieu_l - 15, 400))

  ecran.blit(objet_font1.render("Nombre de joueurs :", True, "white"), (milieu_l-169, 330))

  pygame.display.flip()


def click(ecran, nb_joueurs): 
  H = ecran.get_height()
  L = ecran.get_width()
  milieu_l = L // 2

  click_souris = False
  
  while not click_souris:
    pygame.event.get()
    s = pygame.mouse.get_pressed()

    if s[0]:
      pos = pygame.mouse.get_pos()

      if (milieu_l+200<pos[0]<milieu_l+250) and (400<pos[1]<450):
        click_souris = True
        if nb_joueurs<8:
          nb_joueurs += 1
        pygame.time.wait(150)
        return nb_joueurs, False


      if (milieu_l - 250 <pos[0]< milieu_l - 200) and (400<pos[1]<450):
        click_souris = True
        if nb_joueurs>2:
          nb_joueurs -= 1
        pygame.time.wait(150)
        return nb_joueurs, False


      if (L-470<pos[0]<L-20) and (H-80<pos[1]<H-20):
        click_souris = True
        pygame.time.wait(250)
        return nb_joueurs, True




        
