class Carre:
    def __init__(self, canvas, x, y, vx, vy, largeur, hauteur, couleur):
        self.canvas = canvas
        self.vx = vx
        self.vy = vy
        self.id = canvas.create_rectangle(
            x,
            y,
            x + largeur,
            y + hauteur,
            fill=couleur
        )

    def deplacer(self):
        self.canvas.move(self.id, self.vx, self.vy)

    def coords(self):
        return self.canvas.coords(self.id)

    def set_vitesse(self, vx, vy):
        self.vx = vx
        self.vy = vy