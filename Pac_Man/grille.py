class Grille:
    """
    Gère les murs et les points à manger.
    """

    def __init__(self, canvas, largeur, hauteur):
        self.canvas = canvas
        self.largeur = largeur
        self.hauteur = hauteur
        self.points = []
        self.bords = []


    def creer_points(self):
        """
        Place les points dans le labyrinthe.
        """

        # Efface d'anciens points si on recrée une partie
        for point in self.points:
            self.canvas.delete(point)
        self.points = []

        for x in range(50, self.largeur - 50, 40):
            for y in range(50, self.hauteur - 50, 40):

                point = self.canvas.create_oval(
                    x, y,
                    x + 8,
                    y + 8,
                    fill="white"
                )

                self.points.append(point)


    def verifier_collision(self, joueur):
        """
        Vérifie si Pac-Man mange un point.
        Retourne le nombre de points mangés.
        """

        jx1, jy1, jx2, jy2 = joueur.position()
        eaten = 0

        for point in self.points[:]:

            px1, py1, px2, py2 = self.canvas.coords(point)

            if jx1 <= px2 and jx2 >= px1 and jy1 <= py2 and jy2 >= py1:

                self.canvas.delete(point)
                self.points.remove(point)
                eaten += 1

        return eaten


    def dessiner_bords(self):
        """
        Dessine les bords extérieurs du terrain.
        """

        for bord in self.bords:
            self.canvas.delete(bord)

        self.bords = [
            self.canvas.create_rectangle(0, 0, self.largeur, 5, fill="blue"),  # haut
            self.canvas.create_rectangle(0, self.hauteur - 5, self.largeur, self.hauteur, fill="blue"),  # bas
            self.canvas.create_rectangle(0, 0, 5, self.hauteur, fill="blue"),  # gauche
            self.canvas.create_rectangle(self.largeur - 5, 0, self.largeur, self.hauteur, fill="blue"),  # droite
        ]