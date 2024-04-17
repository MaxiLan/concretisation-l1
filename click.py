import pygame
import carte
import defausse
import pioche


#choix entre pioche et défausse (1er et 2e click)
def click_pioche_defausse(joueur, p, d, ecran):
  click_carte = False
  #click_defausse=False
  pygame.event.get()
  s = pygame.mouse.get_pressed()
  if s[0]:
    pos = pygame.mouse.get_pos()

    #CLICK DÉFAUSSE !!!
    if (580 < pos[0] < 700) and (560 < pos[1] < 720):

      carte_select = d.retire_carte()
      ch = "images/" + str(carte_select.num) + ".png"
      img = pygame.image.load(ch)
      img = pygame.transform.scale(img, (110, 160))
      ecran.blit(img, (580, 375))
      d.affiche(ecran)
      pygame.display.flip()

      while (not click_carte):
        pygame.event.get()
        s = pygame.mouse.get_pressed()

        if s[0]:
          pos = pygame.mouse.get_pos()
          for i in range(3):
            for j in range(4):
              if (25 + j * 130 < pos[0] <
                  135 + j * 130) and (30 + i * 175 < pos[1] < 190 + i * 175):
                click_carte = True
                aux = joueur.jeu_actuel[i][j]
                joueur.jeu_actuel[i][j] = carte_select
                joueur.jeu_actuel[i][j].etat = "ouverte"
                d.ajout_carte(aux)
                carte.cacher_carte(ecran, "defausse")
                pygame.display.flip()
                return True

    #CLICK PIOCHE !!!!
    elif (715 < pos[0] < 825 and 560 < pos[1] < 720):
      click_defausse = False
      carte_select = p.cartes[0]
      carte_select.etat = "ouverte"
      p.cartes.pop(0)
      p.affiche(ecran)
      ch = "images/" + str(carte_select.num) + ".png"
      img = pygame.image.load(ch)
      img = pygame.transform.scale(img, (110, 160))
      ecran.blit(img, (715, 375))
      pygame.display.flip()

      while not (click_carte or click_defausse):
        pygame.event.get()
        s = pygame.mouse.get_pressed()
        if s[0]:
          pos = pygame.mouse.get_pos()
          for i in range(3):
            for j in range(4):
              if (25 + j * 130 < pos[0] <
                  135 + j * 130) and (30 + i * 175 < pos[1] < 190 + i * 175):
                click_carte = True
                aux = joueur.jeu_actuel[i][j]
                joueur.jeu_actuel[i][j] = carte_select
                joueur.jeu_actuel[i][j].etat = "ouverte"
                d.ajout_carte(aux)
                carte.cacher_carte(ecran, "pioche")
                return True

          if (580 < pos[0] < 700) and (560 < pos[1] < 720):
            d.ajout_carte(carte_select)
            d.affiche(ecran)
            carte.cacher_carte(ecran, "pioche")
            pygame.display.flip()
            click_defausse = True
            return retourne_cartes(joueur)

  else:
    return False


#si 2e click = defausse
def retourne_cartes(joueur):
  carte_bien_valide = False
  while not (carte_bien_valide):
    pygame.event.get()
    s = pygame.mouse.get_pressed()
    if s[0]:
      pos = pygame.mouse.get_pos()
      for i in range(3):
        for j in range(4):
          if (25 + j * 130 < pos[0] < 135 + j * 130) and (30 + i * 175 < pos[1]
                                                          < 190 + i * 175):
            if joueur.jeu_actuel[i][j].etat != "ouverte":
              joueur.jeu_actuel[i][j].etat = "ouverte"
              carte_bien_valide = True

  return carte_bien_valide
