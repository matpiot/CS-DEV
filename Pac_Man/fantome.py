import random


class Fantome:
    """
    Représente un fantôme.
    """

    def __init__(self, canvas, x, y, taille, limite_largeur, limite_hauteur):
        """
        Initialise le fantôme.
        """

        self.canvas = canvas
        self.taille = taille
        self.limite_largeur = limite_largeur
        self.limite_hauteur = limite_hauteur

        self.vitesse = 3
        self.vx = self.vitesse
        self.vy = self.vitesse

        self.id = canvas.create_rectangle(
            x, y,
            x + taille,
            y + taille,
            fill="red"
        )


    def deplacer(self, cible):
        """
        Déplacement semi-dirigé vers la cible avec rebond sur les bords.
        """

        cx1, cy1, cx2, cy2 = cible.position()
        tx, ty = self.position_centre()

        # Ajuste la direction vers la cible avec un peu d'aléa
        direction_x = 1 if cx1 > tx else -1
        direction_y = 1 if cy1 > ty else -1

        if random.random() < 0.2:
            direction_x *= -1
        if random.random() < 0.2:
            direction_y *= -1

        self.vx = self.vitesse * direction_x
        self.vy = self.vitesse * direction_y

        self.canvas.move(self.id, self.vx, self.vy)
        self._rebond_si_necessaire()


    def position(self):
        """
        Retourne la position du fantôme.
        """

        return self.canvas.coords(self.id)


    def position_centre(self):
        x1, y1, x2, y2 = self.position()
        return ((x1 + x2) / 2, (y1 + y2) / 2)


    def _rebond_si_necessaire(self):
        """
        Fait rebondir le fantôme sur les bords de l'aire de jeu.
        """

        x1, y1, x2, y2 = self.position()
        rebond = False

        if x1 < 0 or x2 > self.limite_largeur:
            self.vx = -self.vx
            rebond = True

        if y1 < 0 or y2 > self.limite_hauteur:
            self.vy = -self.vy
            rebond = True

        if rebond:
            # annule le déplacement hors limite et applique le rebond
            self.canvas.move(self.id, self.vx * 2, self.vy * 2)