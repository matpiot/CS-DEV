import tkinter as tk
import random as rd
from pomme import Pomme
from carre import Carre


class Snake:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Snake")

        self.largeur = 900
        self.hauteur = 500

        self.canvas = tk.Canvas(self.root, width=self.largeur, height=self.hauteur, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=3)

        self.score = 0
        self.label_score = tk.Label(self.root, text="Score : 0")
        self.label_score.grid(row=0, column=0)

        self.bouton_quitter = tk.Button(self.root, text="Quitter", command=self.root.destroy)
        self.bouton_quitter.grid(row=2, column=0)

        self.bouton_jouer = tk.Button(self.root, text="Jouer", command=self.jouer)
        self.bouton_jouer.grid(row=2, column=2)

        # Initialisation du serpent (tête uniquement, version stricte)
        self.snake = Carre(
            self.canvas,
            x=100,
            y=100,
            vx=10,
            vy=0,
            largeur=20,
            hauteur=20,
            couleur="green"
        )

        # Initialisation pomme
        self.pomme = self.creer_pomme()

        # Clavier
        self.root.bind("<Up>", self.haut)
        self.root.bind("<Down>", self.bas)
        self.root.bind("<Left>", self.gauche)
        self.root.bind("<Right>", self.droite)

        self.jeu_en_cours = False
        self.root.mainloop()

    def creer_pomme(self):
        x = rd.randint(20, self.largeur - 20)
        y = rd.randint(20, self.hauteur - 20)
        return Pomme(self.canvas, x, y, 10, "red")

    def jouer(self):
        if not self.jeu_en_cours:
            self.jeu_en_cours = True
            self.boucle_jeu()

    def boucle_jeu(self):
        self.snake.deplacer()

        if self.collision_bords():
            self.fin_du_jeu("Perdu")
            return

        if self.collision_pomme():
            self.score += 1
            self.label_score.config(text=f"Score : {self.score}")
            self.pomme.detruire()
            self.pomme = self.creer_pomme()

        self.root.after(80, self.boucle_jeu)

    def collision_bords(self):
        x1, y1, x2, y2 = self.snake.coords()
        return x1 < 0 or y1 < 0 or x2 > self.largeur or y2 > self.hauteur

    def collision_pomme(self):
        sx1, sy1, sx2, sy2 = self.snake.coords()
        px1, py1, px2, py2 = self.pomme.coords()
        return not (sx2 < px1 or sx1 > px2 or sy2 < py1 or sy1 > py2)

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
        self.snake.set_vitesse(0, -10)

    def bas(self, event):
        self.snake.set_vitesse(0, 10)

    def gauche(self, event):
        self.snake.set_vitesse(-10, 0)

    def droite(self, event):
        self.snake.set_vitesse(10, 0)


if __name__ == "__main__":
    Snake()