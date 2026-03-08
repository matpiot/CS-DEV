import tkinter as tk

class Vaisseau:
    def __init__(self, canvas, x, y, largeur=40, hauteur=20, couleur="blue"):
        self.canvas = canvas
        self.largeur = largeur
        self.hauteur = hauteur
        self.x = x
        self.y = y
        self.couleur = couleur
        self.id = canvas.create_rectangle(x - largeur//2, y - hauteur//2,
                                          x + largeur//2, y + hauteur//2, fill=couleur)

    def deplacer(self, dx):
        self.x += dx
        self.canvas.move(self.id, dx, 0)