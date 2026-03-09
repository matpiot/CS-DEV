class Joueur:

    def __init__(self, canvas, x, y, taille):
        self.canvas = canvas
        self.taille = taille
        self.x = x
        self.y = y

        self.id = canvas.create_rectangle(
            x, y, x + taille, y + taille,
            fill="blue"
        )

    def deplacer(self, dx, dy):
        self.x += dx
        self.y += dy
        self.canvas.move(self.id, dx, dy)