class Grille:
    """
    Représente la grille du morpion.
    Elle stocke les coups joués et vérifie les conditions de victoire.
    """

    def __init__(self):
        """
        Initialise une grille vide 3x3.
        """
        self.grille = [["" for _ in range(3)] for _ in range(3)]


    def placer(self, ligne, colonne, symbole):
        """
        Place un symbole dans la grille si la case est vide.
        """

        if self.grille[ligne][colonne] == "":
            self.grille[ligne][colonne] = symbole
            return True

        return False


    def victoire(self, symbole):
        """
        Vérifie si un joueur a gagné.
        """

        g = self.grille

        # lignes
        for ligne in g:
            if ligne.count(symbole) == 3:
                return True

        # colonnes
        for col in range(3):
            if g[0][col] == g[1][col] == g[2][col] == symbole:
                return True

        # diagonales
        if g[0][0] == g[1][1] == g[2][2] == symbole:
            return True

        if g[0][2] == g[1][1] == g[2][0] == symbole:
            return True

        return False


    def pleine(self):
        """
        Vérifie si la grille est pleine (match nul).
        """

        for ligne in self.grille:
            if "" in ligne:
                return False

        return True