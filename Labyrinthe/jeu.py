import math
from joueur import Joueur
from labyrinthe import Labyrinthe

class Jeu:

    def __init__(self, canvas, largeur, hauteur):

        self.canvas = canvas
        self.largeur = largeur
        self.hauteur = hauteur

        self.taille_case = 30

        self.labyrinthe = Labyrinthe(largeur, hauteur, self.taille_case)

        self.joueur = Joueur(canvas, 0, 0, self.taille_case)

        self.score = 0
        self.game_over = False
        self.victoire = False

        self.dessiner()

    def dessiner(self):

        lignes = len(self.labyrinthe.grille)
        colonnes = len(self.labyrinthe.grille[0]) if lignes else 0

        for i, ligne in enumerate(self.labyrinthe.grille):
            for j, case in enumerate(ligne):

                x = j * self.taille_case
                y = i * self.taille_case

                if case == 1:

                    self.canvas.create_rectangle(
                        x, y,
                        x + self.taille_case,
                        y + self.taille_case,
                        fill="black"
                    )

                if case == 2:

                    self.canvas.create_rectangle(
                        x, y,
                        x + self.taille_case,
                        y + self.taille_case,
                        fill="green"
                    )

        # Repères visuels pour l'entrée et l'arrivée
        self.canvas.create_text(
            self.taille_case / 2,
            self.taille_case / 2,
            text="Entrée",
            fill="blue",
            font=("Arial", 10, "bold")
        )

        if lignes and colonnes:
            self.canvas.create_text(
                (colonnes - 0.5) * self.taille_case,
                (lignes - 0.5) * self.taille_case,
                text="Arrivée",
                fill="red",
                font=("Arial", 10, "bold")
            )

        self.canvas.tag_raise(self.joueur.id)

    def calculer_score(self):

        sortie_x = self.largeur - self.taille_case
        sortie_y = self.hauteur - self.taille_case

        distance = math.sqrt(
            (self.joueur.x - sortie_x) ** 2 +
            (self.joueur.y - sortie_y) ** 2
        )

        self.score = int(1000 - distance)

    def collision(self, x, y):

        i = y // self.taille_case
        j = x // self.taille_case

        if i < 0 or j < 0:
            return True

        try:
            return self.labyrinthe.grille[i][j] == 1
        except:
            return True

    def deplacer(self, dx, dy):

        if self.game_over:
            return

        new_x = self.joueur.x + dx
        new_y = self.joueur.y + dy

        if self.collision(new_x, new_y):
            self.game_over = True
            self.victoire = False
            return

        self.joueur.deplacer(dx, dy)

        self.calculer_score()

        i = new_y // self.taille_case
        j = new_x // self.taille_case

        if self.labyrinthe.grille[i][j] == 2:
            self.game_over = True
            self.victoire = True