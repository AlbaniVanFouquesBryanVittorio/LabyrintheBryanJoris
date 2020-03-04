# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module matrice
   ~~~~~~~~~~~~~~~
   
   Ce module gère une matrice. 
"""

#-----------------------------------------
# contructeur et accesseurs
#-----------------------------------------

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
    """
    crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant 
    valeurParDefaut dans chacune des cases
    paramètres: 
      nbLignes un entier strictement positif qui indique le nombre de lignes
      nbColonnes un entier strictement positif qui indique le nombre de colonnes
      valeurParDefaut la valeur par défaut
    résultat la matrice ayant les bonnes propriétés
    """
    mat = [[valeurParDefaut for x in range(nbColonnes)] for y in range(nbLignes)]
    return mat

matrice=(Matrice(3,3,valeurParDefaut=0))
#print(matrice)

def getNbLignes(matrice):
    """
    retourne le nombre de lignes de la matrice
    paramètre: matrice la matrice considérée
    """
    return len(matrice)

#print(getNbLignes(matrice))

def getNbColonnes(matrice):
    """
    retourne le nombre de colonnes de la matrice
    paramètre: matrice la matrice considérée
    """
    try:
      return len(matrice[0])
    except:
      return 0

#print(getNbColonnes(matrice))

def getVal(matrice,ligne,colonne):
    """
    retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """
    try:
      return matrice[ligne][colonne]
    except:
      return "Erreur, valeur demandé inexistante"

#print(getVal(matrice,0,0))

def setVal(matrice,ligne,colonne,valeur):
    """
    met la valeur dans la case se trouve en (ligne,colonne) de la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
                valeur la valeur à stocker dans la matrice
    cette fonction ne retourne rien mais modifie la matrice
    """
    try:
      matrice[ligne][colonne]=valeur
    except:
      pass
    
#setVal(matrice,0,1,2)
#print(matrice)

#------------------------------------------        
# decalages
#------------------------------------------


def decalageLigneAGauche(matrice, numLig, nouvelleValeur=0):
    """
    permet de décaler une ligne vers la gauche en insérant une nouvelle
    valeur pour remplacer la premiere case à droite de cette ligne
    le fonction retourne la valeur qui a été éjectée
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat la valeur qui a été ejectée lors du décalage
    """
    valeurEjecte=matrice[numLig][0]
    matrice[numLig].pop(0)
    matrice[numLig].append(nouvelleValeur)
    return valeurEjecte
    
#print(decalageLigneAGauche(matrice, 0, nouvelleValeur=3))
#print(matrice)

def decalageLigneADroite(matrice, numLig, nouvelleValeur=0):
    """
    decale la ligne numLig d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    valeurEjecte=matrice[numLig][-1]
    matrice[numLig].pop()
    matrice[numLig].insert(0,nouvelleValeur)
    return valeurEjecte
    
#print(decalageLigneADroite(matrice, 0, nouvelleValeur=3))
#print(matrice)

def decalageColonneEnHaut(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    valeurEjecte=matrice[0][numCol]

    for i in range(1,len(matrice)):
      matrice[i-1][numCol]=matrice[i][numCol]

    matrice[-1][numCol]=nouvelleValeur
    return valeurEjecte

    """
    valeurEjecte=matrice[0][numCol]
    matrice[0].pop(numCol)
    matrice[-1].insert(numCol,nouvelleValeur)
    return valeurEjecte
    """

#print(decalageColonneEnHaut(matrice, 1, nouvelleValeur=3))
#print(matrice)

def decalageColonneEnBas(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """

    valeurEjecte=matrice[-1][numCol]

    for i in range(len(matrice)-1,-1,-1):
      matrice[i][numCol]=matrice[i-1][numCol]

    matrice[0][numCol]=nouvelleValeur
    return valeurEjecte
    

#print(decalageColonneEnBas(matrice, 1, nouvelleValeur=3))
#print(matrice)
