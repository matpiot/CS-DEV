class Projectile:
    def __init__(self, canvas, x, y, longueur=5, hauteur=15, couleur="red"):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x - longueur//2, y - hauteur,
                                          x + longueur//2, y, fill=couleur)
        self.x = x
        self.y = y
        self.longueur = longueur
        self.hauteur = hauteur
        self.active = True

    def deplacer(self, dy):
        self.y += dy
        self.canvas.move(self.id, 0, dy)
        if self.y < 0:
            self.active = False
            self.canvas.delete(self.id)