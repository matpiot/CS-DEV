import random
from case import Case


class Grille:
    """
    Représente la grille du démineur.
    """

    def __init__(self, taille=8, nb_mines=10):
        self.taille = taille
        self.nb_mines = nb_mines

        self.grille = [
            [Case() for _ in range(taille)]
            for _ in range(taille)
        ]

        self.placer_mines()
        self.calculer_voisins()

    def placer_mines(self):
        mines_placees = 0

        while mines_placees < self.nb_mines:
            x = random.randint(0, self.taille - 1)
            y = random.randint(0, self.taille - 1)

            if not self.grille[x][y].mine:
                self.grille[x][y].mine = True
                mines_placees += 1

    def calculer_voisins(self):
        for x in range(self.taille):
            for y in range(self.taille):
                if self.grille[x][y].mine:
                    continue

                compteur = 0
                for nx, ny in self.voisins(x, y):
                    if self.grille[nx][ny].mine:
                        compteur += 1

                self.grille[x][y].mines_voisines = compteur

    def voisins(self, x, y):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx = x + dx
                ny = y + dy
                if 0 <= nx < self.taille and 0 <= ny < self.taille:
                    yield nx, ny

    def reveler_case(self, x, y):
        if not (0 <= x < self.taille and 0 <= y < self.taille):
            return None

        case = self.grille[x][y]
        if case.revelee:
            return case

        case.reveler()

        if case.mines_voisines == 0 and not case.mine:
            self._flood_fill(x, y)

        return case

    def _flood_fill(self, x, y):
        stack = [(x, y)]

        while stack:
            cx, cy = stack.pop()
            for nx, ny in self.voisins(cx, cy):
                voisin = self.grille[nx][ny]
                if voisin.revelee or voisin.mine:
                    continue
                voisin.reveler()
                if voisin.mines_voisines == 0:
                    stack.append((nx, ny))

    def toutes_les_cases_revelees(self):
        for ligne in self.grille:
            for case in ligne:
                if not case.mine and not case.revelee:
                    return False
        return True

    def afficher(self):
        for ligne in self.grille:
            print(" ".join(case.afficher() for case in ligne))