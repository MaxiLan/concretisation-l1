import pygame

def affiche_accueil(ecran):
  nb_joueurs = 2
  nb_min = 2
  nb_max = 8

  nb_choisi = False

  while not nb_choisi:  
    ecran.fill("grey24")
    affiche_nb_joueurs(ecran, nb_joueurs)
    affiche_titre(ecran)
    affiche_moins(ecran)
    affiche_plus(ecran)
    affiche_ok(ecran)
  
    nb_joueurs, nb_choisi = click(ecran, nb_joueurs)

  return nb_joueurs


def affiche_titre(ecran):
  img = pygame.image.load("images/-2.png")
  img = pygame.transform.scale(img, (200 , 200))

  ecran.blit(img, (100, 100))
  pygame.display.flip()


def affiche_moins(ecran):
  img = pygame.image.load("images/moins.png")
  img = pygame.transform.scale(img, (100 , 100))

  ecran.blit(img, (100, 400))
  pygame.display.flip()


def affiche_plus(ecran):
  img = pygame.image.load("images/plus.png")
  img = pygame.transform.scale(img, (100 , 100))

  ecran.blit(img, (400, 400))
  pygame.display.flip()


def affiche_ok(ecran):
  img = pygame.image.load("images/-1.png")
  img = pygame.transform.scale(img, (100 , 100))

  ecran.blit(img, (600, 300))
  pygame.display.flip()


def affiche_nb_joueurs(ecran, nb_joueurs):
  objet_font = pygame.font.Font(None, 28)
  ecran.blit(objet_font.render(str(nb_joueurs), True, "white"), (300, 300))
  pygame.display.flip()


def click(ecran, nb_joueurs):
  click_souris = False
  
  while not click_souris:
    s = pygame.mouse.get_pressed()
    pygame.event.get()

    if s[0]:
      pos = pygame.mouse.get_pos()

      if (400<pos[0]<500) and (400<pos[1]<500):
        click_souris = True
        nb_joueurs += 1
        return nb_joueurs, False


      if (100<pos[0]<200) and (400<pos[1]<500):
        click_souris = True
        nb_joueurs -= 1
        return nb_joueurs, False


      if (600<pos[0]<700) and (300<pos[1]<400):
        click_souris = True
        return nb_joueurs, True




        
