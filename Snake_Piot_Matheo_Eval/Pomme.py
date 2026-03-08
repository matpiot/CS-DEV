import tkinter as tk
import random as rd

class Pomme:
    def __init__(self, canvas, x, y, rayon, couleur):  #on définit les caractéristiques de la pomme
        """
        Entrée :
            canvas (tk.Canvas) : canevas où dessiner la pomme
            x, y (int|float)    : position du centre de la pomme
            rayon (int|float)   : rayon de la pomme
            couleur (str)       : couleur de la pomme
        Sortie :
            None
        description de la fonction :
            Crée la pomme sur le canvas avec des coordonnées aléatoires
        """
        self.canvas = canvas                                                                #on écrit ces égalités pour que la classe puisse être exploitée par le code principal
        self.id = canvas.create_oval(x-rayon, y-rayon, x+rayon, y+rayon, fill=couleur)
        self.rayon = rayon

    def coords(self):                               #on récupère les coordonnées de la pomme
        """
        Entrée :
            (aucune)
        Sortie :
            list[float] : [x1, y1, x2, y2] coordonnées de l'oval (Pomme)
        description de la fonction :
            Retourne les coordonnées actuelles de la pomme sur le canevas.
        """
        return self.canvas.coords(self.id)