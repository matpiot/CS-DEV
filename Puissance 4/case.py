class Case:
    """
    Représente une case de la grille.
    """

    def __init__(self):
        self.symbole = "."

    def est_vide(self):
        return self.symbole == "."

    def placer(self, symbole):
        self.symbole = symbole

    def afficher(self):
        return self.symbole