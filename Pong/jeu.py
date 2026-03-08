import tkinter as tk
import random
from balle import Balle
from raquette import Raquette


class Jeu:
    """
    Classe principale qui gère le jeu Pong.
    """

    def __init__(self):
        """
        Initialise la fenêtre et les objets du jeu.
        """

        self.largeur = 800
        self.hauteur = 500

        self.root = tk.Tk()
        self.root.title("Pong")

        self.score_gauche = 0
        self.score_droite = 0
        self.running = False

        self.canvas = tk.Canvas(
            self.root,
            width=self.largeur,
            height=self.hauteur,
            bg="black"
        )

        # interface (scores + boutons)
        self.score_label = tk.Label(self.root, text="0 - 0", font=("Arial", 16), fg="white", bg="black")
        self.score_label.pack(fill="x")

        self.canvas.pack()

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill="x", pady=4)

        tk.Button(btn_frame, text="Jouer", command=self.start_game).pack(side="left", expand=True, fill="x", padx=2)
        tk.Button(btn_frame, text="Rejouer", command=self.reset_match).pack(side="left", expand=True, fill="x", padx=2)
        tk.Button(btn_frame, text="Quitter", command=self.root.destroy).pack(side="left", expand=True, fill="x", padx=2)

        # création des objets

        self.balle = Balle(self.canvas, 390, 240)

        self.raquette_gauche = Raquette(self.canvas, 30, 200, self.hauteur)
        self.raquette_droite = Raquette(self.canvas, 755, 200, self.hauteur)

        # contrôles clavier

        self.root.bind("w", self.raquette_gauche.monter)
        self.root.bind("s", self.raquette_gauche.descendre)

        self.root.bind("<Up>", self.raquette_droite.monter)
        self.root.bind("<Down>", self.raquette_droite.descendre)


    def collision_raquette(self):
        """
        Vérifie si la balle touche une raquette.
        """

        bx1, by1, bx2, by2 = self.balle.position()

        for raquette in [self.raquette_gauche, self.raquette_droite]:

            rx1, ry1, rx2, ry2 = raquette.position()

            if bx2 >= rx1 and bx1 <= rx2 and by2 >= ry1 and by1 <= ry2:
                self.balle.rebond_horizontal()
                return


    def collision_murs(self):
        """
        Vérifie si la balle touche les murs haut/bas.
        """

        bx1, by1, bx2, by2 = self.balle.position()

        if by1 <= 0 or by2 >= self.hauteur:
            self.balle.rebond_vertical()


    def boucle_jeu(self):
        """
        Boucle principale du jeu.
        """

        if self.running:
            self.balle.deplacer()
            self.collision_murs()
            self.collision_raquette()
            self.verifier_point()

        self.root.after(16, self.boucle_jeu)


    def lancer(self):
        """
        Lance le jeu.
        """

        self.boucle_jeu()
        self.root.mainloop()


    def start_game(self):
        """
        Démarre ou reprend la partie.
        """

        if not self.running:
            if self.balle is None:
                self.balle = Balle(self.canvas, 390, 240)
            self.running = True


    def reset_match(self):
        """
        Réinitialise scores et balle.
        """

        self.score_gauche = 0
        self.score_droite = 0
        self.update_score_label()
        self.reset_balle(direction=random.choice([-1, 1]))
        self.running = True


    def reset_balle(self, direction=1):
        """
        Replace la balle au centre et relance vers un joueur.
        """

        x = (self.largeur - self.balle.taille) / 2
        y = (self.hauteur - self.balle.taille) / 2
        self.canvas.coords(self.balle.id, x, y, x + self.balle.taille, y + self.balle.taille)

        self.balle.vx = abs(self.balle.vx) * direction
        self.balle.vy = random.choice([-4, 4])


    def update_score_label(self):
        """
        Met à jour l'affichage du score.
        """

        self.score_label.config(text=f"{self.score_gauche} - {self.score_droite}")


    def verifier_point(self):
        """
        Vérifie si un point est marqué et réinitialise la balle.
        """

        bx1, by1, bx2, by2 = self.balle.position()

        if bx1 <= 0:
            self.score_droite += 1
            self.update_score_label()
            self.reset_balle(direction=-1)

        elif bx2 >= self.largeur:
            self.score_gauche += 1
            self.update_score_label()
            self.reset_balle(direction=1)