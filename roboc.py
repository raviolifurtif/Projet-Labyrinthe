# -*-coding: utf-8 -*

"""Ce module contient le code principal
permettant de faire tourner le jeu roboc"""


import os
import math
import pickle
from fonctions import *
from carte import *
from labyrinthe import *



#chargement des cartes : liste_cartes contient une liste d'objets de classe Carte
liste_cartes = charger_cartes()

carte_jouee = ""    #Variable qui va contenir la carte choisie par le joueur

#recherche carte en cours
if recherche_partie() == True :  #True si le fichier "partie_en_cours" existe
    continuer_partie = ""
    while continuer_partie == "":
        continuer_partie = input("Continuer la partie en cours ? (o/n)")
        if continuer_partie.lower() == "o" or continuer_partie.lower() == "oui":  #Le joueur souhaite continuer la partie
            with open("partie_en_cours","r") as fichier:
                partie_en_cours = fichier.read()
                carte_jouee = Carte("partie_continuée",partie_en_cours) #On récupère la partie sauvegardée pour la continuer
        else :      #Si le joueur souhaite commencer une nouvelle partie, on lui fait choisir la carte :
            numero = choix_carte(liste_cartes)
            carte_jouee = liste_cartes[numero-1]
else:       #Si aucune partie n'est en cours, on fait directement choisir une nouvelle carte au joueur :
    numero = choix_carte(liste_cartes)
    carte_jouee = liste_cartes[numero-1]
    

    
continuer = True    

# On commence à présent une partie

while continuer == True:

    deplacement = ""            #contiendra le déplacement entré par le joueur
    iteration_deplacement = ""  #contiendra l'itération demandée par le joueur dans la direction souhaitée
    
    """On s'assure dans cette boucle while que l'entrée du joueur est valable
    (déplacement légal, ou quitter la partie)"""
    
    while deplacement == "": 
        print("\n")
        print(carte_jouee.labyrinthe) # On affiche au joueur l'état actuel du labyrinthe
        deplacement=input("\nDéplacement souhaité ? (Q pour quitter) ")
        if deplacement == "":
            pass    #si le joueur n'a rien saisi, on recommence
        elif deplacement.lower()[0] in "eons" and len(deplacement)>1:   #si la première lettre est un point cardinal et qu'il y a plus d'un caractère
            try :
                iteration_deplacement=int(deplacement[1:])  #On vérifie que ce qui suit la direction demandée est un entier. On le place dans "iteration_deplacement"
                deplacement=deplacement[0]  # Si oui, on ne garde dans "deplacement" que la première lettre, qui donne la direction
            except ValueError:  #Si ce qui suit le point cardinal n'est pas un entier
                print("Déplacement invalide")
                deplacement=""
        elif deplacement.lower()[0] in "eons" and len(deplacement) == 1:    #Si le point cardinal est entré sans itération spécifique
            iteration_deplacement=1
        elif deplacement.lower() == "q" or deplacement.lower() == "quitter" :   #Si le joueur souhaite quitter la partie
            pass
        else:
            print("Déplacement invalide")
            deplacement = ""

    """On va maintenant opérer le(s) déplacement(s) entré par le joueur"""
            
    if deplacement.lower()[0] == "n":
        carte_jouee.labyrinthe.mouvement_nord(iteration_deplacement)
    elif deplacement.lower()[0] == "s":
        carte_jouee.labyrinthe.mouvement_sud(iteration_deplacement)
    elif deplacement.lower()[0] == "e":
        carte_jouee.labyrinthe.mouvement_est(iteration_deplacement)
    elif deplacement.lower()[0] == "o":
        carte_jouee.labyrinthe.mouvement_ouest(iteration_deplacement)
    else :  #Cela signifie que le joueur a souhaité quitter : fin de la boucle de jeu
        continuer = False
    
    if "V" not in repr(carte_jouee.labyrinthe): #L'absence du "V" (qui représente la sortie) atteste que la partie est gagnée.
        continuer = False                       #Fin de la boucle de jeu
        os.remove("partie_en_cours")            #Suppression du fichier de sauvegarde car partie achevée
    else:
        enregistrer_partie(carte_jouee.labyrinthe)  #Partie non terminée : on enregistre automatiquement
    
    

os.system("pause")