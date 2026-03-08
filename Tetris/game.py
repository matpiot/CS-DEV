"""
Classe principale du jeu.
Elle gère :
- la fenêtre graphique
- les entrées clavier
- la boucle du jeu
"""

import tkinter as tk

from settings import *
from board import Board
from piece import Piece


class Game:

    def __init__(self):
        """
        Initialise la fenêtre et les objets du jeu.
        """

        self.root = tk.Tk()
        self.root.title("Tetris")

        self.canvas = tk.Canvas(
            self.root,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            bg="black"
        )

        self.canvas.pack()

        self.board = Board()
        self.piece = Piece()
        self.game_over = False

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Up>", self.rotate_piece)


    def move_left(self, event):
        """
        Déplace la pièce vers la gauche.
        """

        if self.game_over:
            return

        if not self.board.collision(self.piece, dx=-1):
            self.piece.x -= 1


    def move_right(self, event):
        """
        Déplace la pièce vers la droite.
        """

        if self.game_over:
            return

        if not self.board.collision(self.piece, dx=1):
            self.piece.x += 1


    def move_down(self, event=None):
        """
        Fait descendre la pièce.
        """

        if self.game_over:
            return

        if not self.board.collision(self.piece, dy=1):
            self.piece.y += 1
        else:
            self.lock_piece()


    def rotate_piece(self, event=None):
        """
        Tente de faire pivoter la pièce, annule si collision.
        """

        if self.game_over:
            return

        prev_shape = [row[:] for row in self.piece.shape]
        self.piece.rotate()

        if self.board.collision(self.piece):
            self.piece.shape = prev_shape


    def lock_piece(self):
        """
        Fixe la pièce, nettoie les lignes et génère la suivante.
        """

        self.board.merge(self.piece)
        self.board.clear_lines()
        self.piece = Piece()

        if self.board.collision(self.piece):
            self.game_over = True

    def draw_cell(self, x, y):
        """
        Dessine une case du jeu.
        """

        x1 = x * CELL_SIZE
        y1 = y * CELL_SIZE

        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE

        self.canvas.create_rectangle(
            x1, y1, x2, y2,
            fill="cyan",
            outline="gray"
        )


    def draw(self):
        """
        Redessine entièrement la grille.
        """

        self.canvas.delete("all")

        for y, row in enumerate(self.board.grid):
            for x, cell in enumerate(row):

                if cell:
                    self.draw_cell(x, y)


        for y, row in enumerate(self.piece.shape):
            for x, cell in enumerate(row):

                if cell:
                    self.draw_cell(self.piece.x + x, self.piece.y + y)


    def game_loop(self):
        """
        Boucle principale du jeu.
        """

        if self.game_over:
            self.draw()
            self.draw_game_over()
            return

        self.move_down()
        self.draw()

        self.root.after(DROP_DELAY, self.game_loop)


    def run(self):
        """
        Lance le jeu.
        """

        self.game_loop()
        self.root.mainloop()


    def draw_game_over(self):
        """
        Affiche un message de fin de partie.
        """

        self.canvas.create_text(
            WINDOW_WIDTH // 2,
            WINDOW_HEIGHT // 2,
            text="Game Over",
            fill="white",
            font=("Arial", 24, "bold")
        )