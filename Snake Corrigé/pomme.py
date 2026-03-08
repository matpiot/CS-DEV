class Pomme:
    def __init__(self, canvas, x, y, rayon, couleur):
        self.canvas = canvas
        self.rayon = rayon
        self.id = canvas.create_oval(
            x - rayon,
            y - rayon,
            x + rayon,
            y + rayon,
            fill=couleur
        )

    def coords(self):
        return self.canvas.coords(self.id)

    def detruire(self):
        self.canvas.delete(self.id)