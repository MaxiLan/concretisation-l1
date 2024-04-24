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
  img = pygame.transform.scale(img, (100 , 100))

  ecran.blit(img, (milieu_l - 250, 400))

  #signe plus
  img = pygame.image.load("images/plus.png")
  img = pygame.transform.scale(img, (100 , 100))

  ecran.blit(img, (milieu_l + 150, 400))

  #ok
  objet_font1 =  pygame.font.Font(None, 40)

  ecran.blit(img, (600, 300)) 

  #nb joueurs
  objet_font = pygame.font.Font(None, 70)
  ecran.blit(objet_font.render(str(nb_joueurs), True, "white"), (300, 300))

  pygame.display.flip()


def click(ecran, nb_joueurs):
  click_souris = False
  
  while not click_souris:
    pygame.event.get()
    s = pygame.mouse.get_pressed()

    if s[0]:
      pos = pygame.mouse.get_pos()

      if (400<pos[0]<500) and (400<pos[1]<500):
        click_souris = True
        if nb_joueurs<8:
          nb_joueurs += 1
        pygame.time.wait(150)
        return nb_joueurs, False


      if (100<pos[0]<200) and (400<pos[1]<500):
        click_souris = True
        if nb_joueurs>2:
          nb_joueurs -= 1
        pygame.time.wait(150)
        return nb_joueurs, False


      if (600<pos[0]<700) and (300<pos[1]<400):
        click_souris = True
        pygame.time.wait(150)
        return nb_joueurs, True




        
