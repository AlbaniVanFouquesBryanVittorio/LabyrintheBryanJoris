# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module joueur
   ~~~~~~~~~~~~~
   
   Ce module gère un joueur. 
"""

def Joueur(nom):
    listetresors=[]
    joueur=[nom,listetresors]

    return joueur
    """
      creer un nouveau joueur portant le nom passé en paramètre. Ce joueur possède une liste de trésors à trouver vide
      paramètre: nom une chaine de caractères
      retourne le joueur ainsi créé
    """
Michel=Joueur("Michel")


def ajouterTresor(joueur,tresor):
    if tresor not in joueur[1]:
      joueur[1]=joueur[1]+[tresor]
    return joueur

    """
    ajoute un trésor à trouver à un joueur (ce trésor sera ajouter en fin de liste) Si le trésor est déjà dans la liste des trésors à trouver la fonction ne fait rien
    paramètres:
    joueur le joueur à modifier
    tresor un entier strictement positif
    la fonction ne retourne rien mais modifie le joueur
    """
#print(ajouterTresor(Michel,"4"))
#print(ajouterTresor(Michel,"5")) 
#print(ajouterTresor(Michel,"6"))

def prochainTresor(joueur):
    try:
      return joueur[1][0]
    except:
      return None

    """
    retourne le prochain trésor à trouver d'un joueur, retourne None si aucun trésor n'est à trouver
    paramètre:
      joueur le joueur
    résultat un entier représentant le trésor ou None
    """
    pass
#print(prochainTresor(Michel))

def tresorTrouve(joueur):
    del joueur[1][0]
    return joueur
    """ 
    enlève le premier trésor à trouver car le joueur l'a trouvé
    paramètre:
        joueur le joueur
    la fonction ne retourne rien mais modifie le joueur
    """
    pass
#print(tresorTrouve(Michel))

def getNbTresorsRestants(joueur):
    x=0
    for i in joueur[1]:
      x=x+1
    return x
    """
    retourne le nombre de trésors qu'il reste à trouver
    paramètre: joueur le joueur
    résultat: le nombre de trésors attribués au joueur
    """
    pass
#print(getNbTresorsRestants(Michel))

def getNom(joueur):
    return joueur[0]
    """
    retourne le nom du joueur
    paramètre: joueur le joueur
    résultat: le nom du joueur 
    """
    pass
#print(getNom(Michel))