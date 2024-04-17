import click
import pygame
import random
import carte


def tour(joueur, pioche, defausse, ecran):
  #réalise le tour d'un joueur
  tour_finie = click.click_pioche_defausse(joueur, pioche, defausse, ecran)

  while not tour_finie:
    #tant que son tour n'est finie, son jeu reste affiché
    joueur.affiche_jeu(ecran)
    pioche.affiche(ecran)
    defausse.affiche(ecran)
    pygame.display.flip()
    tour_finie = click.click_pioche_defausse(joueur, pioche, defausse, ecran)


def lancement_manche(pioche, defausse, tab_joueurs):
  ma_carte=carte.Carte(42)
  pioche.melange()
  for joueur in tab_joueurs:
    for i in range(3):
      for _ in range(4):
        joueur.jeu_actuel[i].append(pioche.cartes[0])
        pioche.cartes.pop(0)

    abs = random.randint(0, 2)
    ord = random.randint(0, 3)
    joueur.jeu_actuel[abs][ord].etat = "ouverte"
    while (joueur.jeu_actuel[abs][ord].etat != "cachee"):
      abs = random.randint(0, 2)
      ord = random.randint(0, 3)
    joueur.jeu_actuel[abs][ord].etat = "ouverte"
  defausse.ajout_carte(ma_carte)
  defausse.ajout_carte(pioche.cartes[0])
  pioche.cartes.pop(0)
  pioche.cartes[0].etat = "ouverte"


def fin_manche(J):
  #J est un joueur, on testera s'il a retourné toutes ses cartes ou non
  i = 0
  manche_finie = True
  while (manche_finie and i < 3):
    j = 0
    while (j < 4 and manche_finie):
      if J.jeu_actuel[i][j].etat == "ouverte":
        manche_finie = False
      j += 1
    i += 1

  return manche_finie


def manche(tab_joueurs, pioche, defausse, ecran):
  lancement_manche(pioche, defausse, tab_joueurs)
  i_joueur = 0
  joueur = tab_joueurs[i_joueur]
  manche_fin = False

  while not manche_fin:
    tour(joueur, pioche, defausse, ecran)
    defausse.affiche(ecran)
    joueur.affiche_jeu(ecran) 
    pygame.display.flip()
    i_joueur = (i_joueur + 1) % len(tab_joueurs)
    manche_fin = fin_manche(joueur)
    joueur = tab_joueurs[i_joueur]
    pygame.time.wait(2000)
