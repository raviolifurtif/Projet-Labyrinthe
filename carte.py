# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte et la fonction
permettant de créer un objet de classeLabyrinthe
(car l'attribut labyrinthe de la classe Carte est un objet de classe Labyrinthe)."""

import os
import labyrinthe
from fonctions import *





def creer_labyrinthe(chaine):

    """Prend une chaine en paramètre (qui encode la carte "brute" avec robot)
    et renvoie un objet de type labyrinthe"""
    
    robot = [0,0]                      #On mettra dans cette liste les coordonnées du robot : [ligne,position au sein de la ligne]
    lignes=chaine.split("\n")       #On sépare la chaîne de caractères composant la carte en une liste contenant chacune des lignes du labyrinthe
    for i,elt in enumerate(lignes):
        if "X" in elt :             #On cherche la position du robot au sein des lignes
            robot[0] = i
            robot[1] = elt.find("X")
    
    #La variable robot contient à présent les coordonnées initiales du robot
    
    #On va maintenant remplacer dans la grille le X par un espace vide : notre variable grille ne contiendra que le labyrinthe vierge
    lignes[robot[0]] = lignes[robot[0]][:robot[1]]+" "+lignes[robot[0]][robot[1]+1:]  
    laby = labyrinthe.Labyrinthe(robot,lignes)
    return laby


class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = creer_labyrinthe(chaine)  #Objet de classe Labyrinthe, créé par la fonction ci-dessus

    def __repr__(self):
    
        """Permet d'afficher le nom des cartes pour que le joueur en choisisse une"""
    
        return "{}".format(self.nom)
