"""
Une pièce correspond à un tétrimino du jeu Tetris.
"""

import random

SHAPES = [
    [[1,1,1,1]],

    [[1,1],
     [1,1]],

    [[0,1,0],
     [1,1,1]],

    [[1,0,0],
     [1,1,1]],

    [[0,0,1],
     [1,1,1]],

    [[0,1,1],
     [1,1,0]],

    [[1,1,0],
     [0,1,1]]
]


class Piece:
    """
    Représente une pièce active contrôlée par le joueur.
    """

    def __init__(self):
        """
        Initialise une pièce aléatoire au sommet de la grille.
        """
        self.shape = random.choice(SHAPES)
        self.x = 3
        self.y = 0

    def rotate(self):
        """
        Effectue une rotation de la pièce (90 degrés).
        La rotation est obtenue en transposant la matrice.
        """
        self.shape = [list(row) for row in zip(*self.shape[::-1])]