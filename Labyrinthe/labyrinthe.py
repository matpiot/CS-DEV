import random

class Labyrinthe:

    def __init__(self, largeur, hauteur, taille_case):
        self.largeur = largeur
        self.hauteur = hauteur
        self.taille_case = taille_case

        self.grille = []
        self.generer()

    def generer(self):

        lignes = self.hauteur // self.taille_case
        colonnes = self.largeur // self.taille_case

        self.grille = []

        for i in range(lignes):
            ligne = []
            for j in range(colonnes):

                if random.random() < 0.25:
                    ligne.append(1)  # mur
                else:
                    ligne.append(0)  # passage

            self.grille.append(ligne)

        # départ et sortie libres
        self.grille[0][0] = 0
        self.grille[lignes-1][colonnes-1] = 2  # sortie