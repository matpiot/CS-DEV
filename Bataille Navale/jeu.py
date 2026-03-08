from grille import Grille


class JeuBatailleNavale:
    """Contrôle la logique du jeu."""

    def __init__(self):

        self.grille = Grille()

        for taille in [5, 4, 3, 3, 2]:
            self.grille.placer_bateau_aleatoire(taille)

    def tirer(self, position):

        return self.grille.tirer(position)

    def est_termine(self):

        return self.grille.victoire()