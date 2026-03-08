class Joueur:
    """
    Représente Pac-Man (le joueur).
    """

    def __init__(self, canvas, x, y, taille, limite_largeur, limite_hauteur):
        """
        Initialise Pac-Man.
        """

        self.canvas = canvas
        self.taille = taille
        self.limite_largeur = limite_largeur
        self.limite_hauteur = limite_hauteur

        self.x = x
        self.y = y

        self.dx = 0
        self.dy = 0

        self.id = canvas.create_oval(
            x, y,
            x + taille,
            y + taille,
            fill="yellow"
        )


    def deplacer(self):
        """
        Déplace Pac-Man selon sa direction puis le garde dans les bornes.
        """

        self.canvas.move(self.id, self.dx, self.dy)
        self._clamp()


    def aller_gauche(self, event=None):
        self.dx = -5
        self.dy = 0


    def aller_droite(self, event=None):
        self.dx = 5
        self.dy = 0


    def aller_haut(self, event=None):
        self.dx = 0
        self.dy = -5


    def aller_bas(self, event=None):
        self.dx = 0
        self.dy = 5


    def position(self):
        """
        Retourne la position de Pac-Man.
        """

        return self.canvas.coords(self.id)


    def _clamp(self):
        """
        Empêche Pac-Man de sortir de l'aire de jeu.
        """

        x1, y1, x2, y2 = self.canvas.coords(self.id)

        if x1 < 0:
            x1, x2 = 0, self.taille

        if y1 < 0:
            y1, y2 = 0, self.taille

        if x2 > self.limite_largeur:
            x2 = self.limite_largeur
            x1 = x2 - self.taille

        if y2 > self.limite_hauteur:
            y2 = self.limite_hauteur
            y1 = y2 - self.taille

        self.canvas.coords(self.id, x1, y1, x2, y2)