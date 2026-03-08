class Balle:
    """
    Représente la balle du jeu Pong.
    Gère sa position, son déplacement et ses rebonds.
    """

    def __init__(self, canvas, x, y):
        """
        Initialise la balle.

        paramètres :
            canvas : surface graphique tkinter
            x, y : position initiale
        """

        self.canvas = canvas
        self.taille = 20

        self.vx = 4
        self.vy = 4

        self.id = canvas.create_oval(
            x, y,
            x + self.taille,
            y + self.taille,
            fill="white"
        )


    def deplacer(self):
        """
        Déplace la balle selon sa vitesse.
        """

        self.canvas.move(self.id, self.vx, self.vy)


    def rebond_horizontal(self):
        """
        Inverse la direction horizontale.
        """

        self.vx = -self.vx


    def rebond_vertical(self):
        """
        Inverse la direction verticale.
        """

        self.vy = -self.vy


    def position(self):
        """
        Retourne les coordonnées de la balle.
        """

        return self.canvas.coords(self.id)