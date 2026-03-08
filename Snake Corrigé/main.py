import tkinter as tk
import random as rd
from pomme import Pomme


class Snake:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Snake")

        self.largeur = 900
        self.hauteur = 500
        self.cell = 20

        self.canvas = tk.Canvas(self.root, width=self.largeur, height=self.hauteur, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=3)

        self.score = 0
        self.label_score = tk.Label(self.root, text="Score : 0")
        self.label_score.grid(row=0, column=0)

        self.bouton_quitter = tk.Button(self.root, text="Quitter", command=self.root.destroy)
        self.bouton_quitter.grid(row=2, column=0)

        self.bouton_rejouer = tk.Button(self.root, text="Rejouer", command=self.reset)
        self.bouton_rejouer.grid(row=2, column=1)

        self.bouton_jouer = tk.Button(self.root, text="Jouer", command=self.jouer)
        self.bouton_jouer.grid(row=2, column=2)

        # Clavier
        self.root.bind("<Up>", self.haut)
        self.root.bind("<Down>", self.bas)
        self.root.bind("<Left>", self.gauche)
        self.root.bind("<Right>", self.droite)

        self.jeu_en_cours = False
        self.direction = (self.cell, 0)
        self.segments = []  # liste d'IDs des segments du serpent
        self.pending_growth = 0

        self.reset()
        self.root.mainloop()

    def reset(self):
        """
        Réinitialise le plateau, le serpent et la pomme.
        """

        self.jeu_en_cours = False
        self.score = 0
        self.label_score.config(text="Score : 0")
        self.direction = (self.cell, 0)
        self.pending_growth = 0

        self.canvas.delete("all")

        # serpent de longueur 3 centré
        start_x = 100
        start_y = 100
        self.segments = []
        for i in range(3):
            seg = self.canvas.create_rectangle(
                start_x - i * self.cell,
                start_y,
                start_x - i * self.cell + self.cell,
                start_y + self.cell,
                fill="green"
            )
            self.segments.append(seg)

        self.pomme = self.creer_pomme()

    def creer_pomme(self):
        """
        Crée une pomme alignée sur la grille.
        """

        max_x = (self.largeur - self.cell) // self.cell
        max_y = (self.hauteur - self.cell) // self.cell
        x = rd.randint(1, max_x - 1) * self.cell
        y = rd.randint(1, max_y - 1) * self.cell
        return Pomme(self.canvas, x, y, self.cell // 2, "red")

    def jouer(self):
        if not self.jeu_en_cours:
            self.jeu_en_cours = True
            self.boucle_jeu()

    def boucle_jeu(self):
        if not self.jeu_en_cours:
            return

        if not self.deplacer_snake():
            self.fin_du_jeu("Perdu")
            return

        if self.collision_pomme():
            self.score += 1
            self.pending_growth += 1
            self.label_score.config(text=f"Score : {self.score}")
            self.pomme.detruire()
            self.pomme = self.creer_pomme()

        self.root.after(80, self.boucle_jeu)

    def deplacer_snake(self):
        """
        Avance le serpent; retourne False en cas de collision mur/soi-même.
        """

        dx, dy = self.direction
        head_coords = self.canvas.coords(self.segments[0])
        x1, y1, x2, y2 = head_coords
        new_head_x1 = x1 + dx
        new_head_y1 = y1 + dy
        new_head_x2 = x2 + dx
        new_head_y2 = y2 + dy

        # murs
        if new_head_x1 < 0 or new_head_y1 < 0 or new_head_x2 > self.largeur or new_head_y2 > self.hauteur:
            return False

        # self collision: compare with existing segments positions
        for seg_id in self.segments:
            sx1, sy1, sx2, sy2 = self.canvas.coords(seg_id)
            if sx1 == new_head_x1 and sy1 == new_head_y1:
                return False

        # créer nouvelle tête
        new_head = self.canvas.create_rectangle(
            new_head_x1,
            new_head_y1,
            new_head_x2,
            new_head_y2,
            fill="green"
        )
        self.segments.insert(0, new_head)

        if self.pending_growth > 0:
            self.pending_growth -= 1
        else:
            tail = self.segments.pop()
            self.canvas.delete(tail)

        return True

    def collision_pomme(self):
        hx1, hy1, hx2, hy2 = self.canvas.coords(self.segments[0])
        px1, py1, px2, py2 = self.pomme.coords()
        return not (hx2 <= px1 or hx1 >= px2 or hy2 <= py1 or hy1 >= py2)

    def fin_du_jeu(self, message):
        self.canvas.create_text(
            self.largeur // 2,
            self.hauteur // 2,
            text=message,
            font=("Helvetica", 30),
            fill="black"
        )
        self.jeu_en_cours = False

    # Déplacements
    def haut(self, event):
        self.direction = (0, -self.cell)

    def bas(self, event):
        self.direction = (0, self.cell)

    def gauche(self, event):
        self.direction = (-self.cell, 0)

    def droite(self, event):
        self.direction = (self.cell, 0)


if __name__ == "__main__":
    Snake()