# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

import os
from carte import *
from fonctions import *



class Labyrinthe:

    """Classe représentant un labyrinthe.
    
    le paramètre grille passé au constructeur est une liste contenant les chaînes de caractères
    formant le labyrinthe vierge.
    
    le paramètre robot est une liste contenant la position du robot : [ligne,colonne]
    exemple : robot=[3,1] si le robot est sur la quatrième ligne en deuxième position"""

    def __init__(self, robot, grille):
        self.robot = robot                  #l'attribut robot est une liste contenant les coordonnées du robot : [3,1] si le robot est sur la quatrième ligne en deuxième position
        self.grille = {}                    #l'attribut grille est un dictionnaire. 
        for i,elt in enumerate(grille):     #On remplit ce dictionnaire avec les lignes de la grille, avec comme clé la position de la ligne. exemple : self.grille[0] contient la chaine représentant la ligne en haut du labyrinthe
            self.grille[i] = elt
        
        
    """méthode renvoyant une longue chaîne avec des retours à la ligne,
    composant le labyrinthe dans son état actualisé avec le robot correctement placé"""
        
    def __repr__(self):
        lignes_avec_robot=[]    #cette liste va contenir les lignes du labyrinthe sans robot. Il suffira d'ajouter le robot au bon endroit.
        labyrinthe_actuel=""    #cette variable (qui sera celle renvoyée) va se remplir en concaténant les lignes de "lignes_avec_robot"
        for elt in self.grille.values():
            lignes_avec_robot.append(elt)   #On a "copié" notre labyrinthe sans robot dans une liste tampon
            
        #On place à présent le X du robot au bon endroit dans la bonne ligne grâce aux coordonnées contenues dans la variable robot :
        
        lignes_avec_robot[self.robot[0]]=lignes_avec_robot[self.robot[0]][:self.robot[1]]+"X"+lignes_avec_robot[self.robot[0]][self.robot[1]+1:] 
        labyrinthe_actuel="\n".join(lignes_avec_robot)
        return labyrinthe_actuel
        
    """Methodes permettant de transformer le labyrinthe après que
    le joueur a entré une commande (exemple : n3)
    On prend en paramètre le nombre de cases à parcourir
    dans la direction souhaitée par le joueur.
    
    La variable iteration_deplacement permet de réitérer l'opération
    autant de fois que demandé (jusqu'à tomber sur un mur ou sur la sortie)."""
    
    def mouvement_nord(self,iteration_deplacement):
        while iteration_deplacement > 0:
            if self.grille[self.robot[0]-1][self.robot[1]] == "0": #on regarde s'il y a un obstacle au nord du robot
                print("\n")
                print("Vous avez rencontré un obstacle !")
                iteration_deplacement = 0   #On arrête le déplacement, il y a un mur
            elif self.grille[self.robot[0]-1][self.robot[1]] in " .": #on regarde si l'emplacement au nord du robot est libre
                self.robot[0] -= 1  #On déplace le robot d'une case vers le Nord
                iteration_deplacement -= 1
            elif self.grille[self.robot[0]-1][self.robot[1]] == "V" : #On regarde si la case au nord est la sortie
                self.robot[0] -= 1  #On déplace le robot d'une case vers le Nord
                iteration_deplacement = 0   #On arrête le déplacement, on a gagné
                print("\n")
                print(self)
                print("\n")
                print("Félicitations, vous avez gagné !\n")
            else:
                print("Erreur de déplacement !")

                
    def mouvement_sud(self,iteration_deplacement):
        while iteration_deplacement > 0:
            if self.grille[self.robot[0]+1][self.robot[1]] == "0": #on regarde s'il y a un obstacle au Sud du robot
                print("\n")
                print("Vous avez rencontré un obstacle !")
                iteration_deplacement = 0   #On arrête le déplacement, il y a un mur
            elif self.grille[self.robot[0]+1][self.robot[1]] in " .": #on regarde si l'emplacement au Sud du robot est libre
                self.robot[0] += 1  #On déplace le robot d'une case vers le Sud
                iteration_deplacement -= 1
            elif self.grille[self.robot[0]+1][self.robot[1]] == "V" : #Si la case au Sud est la sortie
                self.robot[0] += 1  #On déplace le robot d'une case vers le Sud
                iteration_deplacement = 0   #On arrête le déplacement, on a gagné
                print("\n")
                print(self)
                print("\n")
                print("Félicitations, vous avez gagné !\n")
            else:
                print("Erreur de déplacement !")

                
    def mouvement_est(self,iteration_deplacement):
        while iteration_deplacement > 0:
            if self.grille[self.robot[0]][self.robot[1]+1] == "0": #on regarde s'il y a un obstacle à l'Est du robot
                print("\n")
                print("Vous avez rencontré un obstacle !")
                iteration_deplacement = 0   #On arrête le déplacement, il y a un mur
            elif self.grille[self.robot[0]][self.robot[1]+1] in " .": #on regarde si l'emplacement à l'Est du robot est libre
                self.robot[1] += 1  #On déplace le robot d'une case vers l'Est
                iteration_deplacement -= 1
            elif self.grille[self.robot[0]][self.robot[1]+1] == "V" : #Si la case à l'Est est la sortie
                self.robot[1] += 1  #On déplace le robot d'une case vers l'Est
                iteration_deplacement = 0   #On arrête le déplacement, on a gagné
                print("\n")
                print(self)
                print("\n")
                print("Félicitations, vous avez gagné !\n")
            else:
                print("Erreur de déplacement !")
                iteration_deplacement = 0
               
    def mouvement_ouest(self,iteration_deplacement):
        while iteration_deplacement > 0:
            if self.grille[self.robot[0]][self.robot[1]-1] == "0": #on regarde s'il y a un obstacle à l'Ouest du robot
                print("\n")
                print("Vous avez rencontré un obstacle !")
                iteration_deplacement = 0   #On arrête le déplacement, il y a un mur
            elif self.grille[self.robot[0]][self.robot[1]-1] in " .": #on regarde si l'emplacement à l'Ouest du robot est libre
                self.robot[1] -= 1  #On déplace le robot d'une case vers l'Ouest
                iteration_deplacement -= 1
            elif self.grille[self.robot[0]][self.robot[1]-1] == "V" : #Si la case à l'Ouest est la sortie
                self.robot[1] -= 1  #On déplace le robot d'une case vers l'Ouest
                iteration_deplacement = 0   #On arrête le déplacement, on a gagné
                print("\n")
                print(self)
                print("\n")
                print("Félicitations, vous avez gagné !\n")
            else:
                print("Erreur lors du déplacement !")    #Si quelque chose se passe mal, ce message s'affichera
                

