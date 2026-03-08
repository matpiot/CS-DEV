class Raquette:
    """
    Représente une raquette de joueur.
    """

    def __init__(self, canvas, x, y, limite_hauteur):
        """
        Initialise la raquette.

        paramètres :
            canvas : surface graphique
            x, y : position initiale
            limite_hauteur : hauteur maximale autorisée (bord bas)
        """

        self.canvas = canvas
        self.limite_hauteur = limite_hauteur

        self.largeur = 15
        self.hauteur = 100

        self.vitesse = 20

        self.id = canvas.create_rectangle(
            x, y,
            x + self.largeur,
            y + self.hauteur,
            fill="white"
        )


    def monter(self, event=None):
        """
        Déplace la raquette vers le haut en restant dans la fenêtre.
        """

        self.canvas.move(self.id, 0, -self.vitesse)
        self._clamp()


    def descendre(self, event=None):
        """
        Déplace la raquette vers le bas en restant dans la fenêtre.
        """

        self.canvas.move(self.id, 0, self.vitesse)
        self._clamp()


    def position(self):
        """
        Retourne la position actuelle de la raquette.
        """

        return self.canvas.coords(self.id)


    def _clamp(self):
        """
        Empêche la raquette de sortir de la zone de jeu.
        """

        x1, y1, x2, y2 = self.canvas.coords(self.id)

        if y1 < 0:
            y1 = 0
            y2 = self.hauteur

        if y2 > self.limite_hauteur:
            y2 = self.limite_hauteur
            y1 = y2 - self.hauteur

        self.canvas.coords(self.id, x1, y1, x2, y2)