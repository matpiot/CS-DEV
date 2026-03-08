import random
from bateau import Bateau


class Grille:
    """Représente la grille du jeu."""

    def __init__(self, taille=10):
        self.taille = taille
        self.bateaux = []
        self.tirs = set()

    def placer_bateau_aleatoire(self, longueur):

        while True:

            horizontal = random.choice([True, False])

            x = random.randint(0, self.taille - 1)
            y = random.randint(0, self.taille - 1)

            positions = []

            for i in range(longueur):

                nx = x + i if horizontal else x
                ny = y if horizontal else y + i

                if nx >= self.taille or ny >= self.taille:
                    break

                positions.append((nx, ny))

            if len(positions) != longueur:
                continue

            if any(pos in p for bateau in self.bateaux for p in bateau.positions for pos in positions):
                continue

            self.bateaux.append(Bateau(positions))
            return

    def tirer(self, position):

        self.tirs.add(position)

        for bateau in self.bateaux:

            if bateau.recevoir_tir(position):
                return "touche"

        return "rate"

    def victoire(self):

        return all(bateau.est_coule() for bateau in self.bateaux)