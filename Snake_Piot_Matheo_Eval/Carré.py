import tkinter as tk
import random as rd

class Carré:
    def __init__(self, canvas, x, y, vx, vy, largeur, hauteur, couleur):
        
        """
        Entrée :
            canvas (tk.Canvas) : canevas où dessiner les carrés
            x, y (int|float)    : position du coin supérieur gauche
            largeur, hauteur    : dimensions du rectangle
            couleur (str)       : couleur de remplissage
        Sortie :
            None
        description de la fonction :
            Crée un rectangle sur le canevas pour représenter un carré
            et stocke son identifiant dans self.id.
        """
        self.canvas = canvas
        self.id = canvas.create_rectangle(x, y, x+largeur, y+hauteur, fill = couleur)
        self.vx = vx
        self.vy = vy

    def deplacer(self):
        """
        Entrée :
            (aucune)
        Sortie :
            None
        description de la fonction :
            Déplace le carré selon ses composantes de vitesse (vx, vy)
            puis vérifie la collision avec les bords du canevas.
        """
        
        self.canvas.move(self.id, self.vx, self.vy)
        self.canvas.bind_all("<A>", self.deplacer_haut)                #on associe les déplacements aux boutons comme demandé
        self.canvas.bind_all("<Q>", self.deplacer_bas)
        self.canvas.bind_all("<O>", self.deplacer_gauche)                
        self.canvas.bind_all("<P>", self.deplacer_droite)
        self.verifier_collisions_bords()
       
    def detruire(self):                 #fonction supprimant le canvas du carré 
        """
        Entrée :
            (aucune) -- utilise self.canvas et self.id
        Sortie :
            None
        description de la fonction :
            Supprime l'objet graphique correspondant au carré du canevas.
        """
        self.canvas.delete(self.id)
    
    def coords(self):
        """
        Entrée :
            (aucune) -- utilise self.canvas et self.id
        Sortie :
            list[float] : [x1, y1, x2, y2] coordonnées du carré
        description de la fonction :
            Retourne les coordonnées actuelles du carré sur le canevas.
        """
        return self.canvas.coords(self.id)  # retourne les coordonnées des coins du carré
    
    def vitesse(self):
        """
        Entrée :
            (aucune) -- utilise self.canvas et self.id
        Sortie :
            list[float] : [vx, vy] vitesse des carrés :
            Retourne la vitesse des carrés sur le cannevas 
        """
        return self.canvas.vitesse(self.id)