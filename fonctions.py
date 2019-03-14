# -*-coding: utf-8 -*

"""Ce module contient certaines fonctions utiles au module roboc"""

import os
import math
import pickle
import random
from labyrinthe import *
from carte import *



"""Recherche d'une partie enregistrée
Renvoie True si une partie avait été enregistréé, False sinon"""

def recherche_partie():
    try:
        with open("partie_en_cours","r") as fichier:
            carte=fichier.read()
        return True
    except FileNotFoundError:
        return False
        
        
        

def charger_cartes():

    """charge toutes les cartes existantes contenues dans le dossier cartes.
    Renvoie une liste contenant des objets de classe Carte, prêts à être transformés en Labyrinthes et utilisés pour une partie"""

    liste_cartes=[]  #Liste que l'on remplira d'objets de classe Carte, à partir des chaînes récupérées dans le dossier "cartes"
    
    for nom_fichier in os.listdir("cartes"):
        if nom_fichier.endswith(".txt"):       #On recherche chaque fichier .txt (qui est donc une carte)
            with open("cartes/{}".format(nom_fichier),"r") as fichier:
                carte = fichier.read()   #La variable carte contient maintenant la chaine de caractère "brute" constituant l'image initiale du labyrinthe
            nom_fichier = nom_fichier.split(".")[0] #On enlève l'extension .txt
            carte = Carte(nom_fichier,carte)                #On crée l'objet de classe Carte à partir de la chaîne "carte" correspondante, et du nom adéquat
            liste_cartes.append(carte)
    return liste_cartes  
        


def enregistrer_partie(labyrinthe):

    """Enregistrement de la partie en cours"""
    
    chaine_a_enregistrer=repr(labyrinthe)
    with open("partie_en_cours","w") as fichier:
        fichier.write(chaine_a_enregistrer)
        
        


def choix_carte(liste_cartes):

    """Demande au joueur la carte sur laquelle il souhaite jouer
    et retourne le numéro de la carte choisie"""
    
    carte_choisie = ""   # Doit contenir un numéro de carte valable à l'issue de la boucle while
    while carte_choisie == "":
        print("\nCartes disponibles :")   #On présente au joueur les cartes disponibles
        for i,elt in enumerate(liste_cartes):
            print("{} : {}".format(i+1,elt))
            
        carte_choisie=input("\nNuméro de la carte choisie : ")    #On lui fait choisir l'une d'elles
        try:
            carte_choisie = int(carte_choisie)
            if carte_choisie not in range(1,len(liste_cartes)+1):   #Si le numéro entré est non conforme
                print("\nVeuillez entrer un numéro de carte valide")
                carte_choisie = ""
            else:
                return carte_choisie
        except ValueError:  #Si le joueur n'a pas entré un entier
            print("\nEntrée non valide")
            carte_choisie = ""
        
                


    
