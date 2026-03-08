"""
Classe Board : représente la grille du jeu.
Elle gère les collisions et la suppression des lignes.
"""

from settings import ROWS, COLUMNS

class Board:

    def __init__(self):
        """
        Crée une grille vide.
        La grille est une matrice de 0 (case vide).
        """
        self.grid = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]


    def collision(self, piece, dx=0, dy=0):
        """
        Vérifie si une pièce entre en collision
        avec un mur ou une autre pièce.
        """

        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):

                if cell:

                    new_x = piece.x + x + dx
                    new_y = piece.y + y + dy

                    if new_x < 0 or new_x >= COLUMNS:
                        return True

                    if new_y >= ROWS:
                        return True

                    if new_y >= 0 and self.grid[new_y][new_x]:
                        return True

        return False


    def merge(self, piece):
        """
        Ajoute définitivement une pièce dans la grille.
        """

        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):

                if cell:
                    self.grid[piece.y + y][piece.x + x] = 1


    def clear_lines(self):
        """
        Supprime les lignes complètes.
        Les blocs situés au-dessus descendent.
        """

        new_grid = [row for row in self.grid if not all(row)]

        while len(new_grid) < ROWS:
            new_grid.insert(0, [0 for _ in range(COLUMNS)])

        self.grid = new_grid