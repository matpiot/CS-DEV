from case import Case


class Grille:
    """
    Représente la grille du puissance 4.
    """

    def __init__(self, lignes=6, colonnes=7):
        self.lignes = lignes
        self.colonnes = colonnes

        self.grille = [
            [Case() for _ in range(colonnes)]
            for _ in range(lignes)
        ]

    def afficher(self):
        for ligne in self.grille:
            print(" ".join(case.afficher() for case in ligne))
        print()

    def colonne_valide(self, colonne):
        return 0 <= colonne < self.colonnes and self.grille[0][colonne].est_vide()

    def placer_jeton(self, colonne, symbole):

        for i in range(self.lignes - 1, -1, -1):

            case = self.grille[i][colonne]

            if case.est_vide():
                case.placer(symbole)
                return i, colonne

        return None

    def est_pleine(self):
        return all(not case.est_vide() for case in self.grille[0])

    def verifier_victoire(self, symbole):

        for i in range(self.lignes):
            for j in range(self.colonnes - 3):

                if all(self.grille[i][j+k].symbole == symbole for k in range(4)):
                    return True

        for i in range(self.lignes - 3):
            for j in range(self.colonnes):

                if all(self.grille[i+k][j].symbole == symbole for k in range(4)):
                    return True

        for i in range(self.lignes - 3):
            for j in range(self.colonnes - 3):

                if all(self.grille[i+k][j+k].symbole == symbole for k in range(4)):
                    return True

        for i in range(3, self.lignes):
            for j in range(self.colonnes - 3):

                if all(self.grille[i-k][j+k].symbole == symbole for k in range(4)):
                    return True

        return False