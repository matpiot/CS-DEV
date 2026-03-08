class Case:
    """
    Représente une case du démineur.
    """

    def __init__(self, mine=False):
        self.mine = mine
        self.revelee = False
        self.mines_voisines = 0

    def reveler(self):
        """Révèle la case."""
        self.revelee = True

    def afficher(self):
        """Retourne la représentation de la case."""
        if not self.revelee:
            return "■"

        if self.mine:
            return "*"

        return str(self.mines_voisines)