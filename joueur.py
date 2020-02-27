# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module joueur
   ~~~~~~~~~~~~~
   
   Ce module gère un joueur. 
"""

def Joueur(nom):
    joueur={"nomjoueur" : nom , "listetresor" : []}

    return joueur
    """
      creer un nouveau joueur portant le nom passé en paramètre. Ce joueur possède une liste de trésors à trouver vide
      paramètre: nom une chaine de caractères
      retourne le joueur ainsi créé
    """
#Michel=Joueur("Michel")
#print(Michel)


def ajouterTresor(joueur,tresor):
    joueur["listetresor"].append(tresor)

    #if tresor not in joueur[1]:
      #joueur[1]=joueur[1]+[tresor]

    """
    ajoute un trésor à trouver à un joueur (ce trésor sera ajouter en fin de liste) Si le trésor est déjà dans la liste des trésors à trouver la fonction ne fait rien
    paramètres:
    joueur le joueur à modifier
    tresor un entier strictement positif
    la fonction ne retourne rien mais modifie le joueur
    """
#ajouterTresor(Michel,"4")
#ajouterTresor(Michel,"5")
#ajouterTresor(Michel,"6")
#print(Michel["listetresor"])

def prochainTresor(joueur):
    try:
      return joueur["listetresor"][0]
    except:
      return None

    """
    retourne le prochain trésor à trouver d'un joueur, retourne None si aucun trésor n'est à trouver
    paramètre:
      joueur le joueur
    résultat un entier représentant le trésor ou None
    """
#print(prochainTresor(Michel))

def tresorTrouve(joueur):
    del joueur["listetresor"][0]
    """ 
    enlève le premier trésor à trouver car le joueur l'a trouvé
    paramètre:
        joueur le joueur
    la fonction ne retourne rien mais modifie le joueur
    """
#tresorTrouve(Michel)
#print(Michel)

def getNbTresorsRestants(joueur):
    return len(joueur["listetresor"])
    """
    retourne le nombre de trésors qu'il reste à trouver
    paramètre: joueur le joueur
    résultat: le nombre de trésors attribués au joueur
    """
#print(getNbTresorsRestants(Michel))

def getNom(joueur):
    return joueur["nomjoueur"]
    """
    retourne le nom du joueur
    paramètre: joueur le joueur
    résultat: le nom du joueur 
    """
#print(getNom(Michel))