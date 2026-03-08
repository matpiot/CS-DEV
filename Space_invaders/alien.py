class Alien:
    def __init__(self, canvas, x, y, taille=30, couleur="green"):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.taille = taille
        self.couleur = couleur
        self.id = canvas.create_rectangle(x, y, x + taille, y + taille, fill=couleur)

    def deplacer(self, dx, dy=0):
        self.x += dx
        self.y += dy
        self.canvas.move(self.id, dx, dy)