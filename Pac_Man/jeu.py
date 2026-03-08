import tkinter as tk
import random

from joueur import Joueur
from fantome import Fantome
from grille import Grille


class Jeu:
    """
    Classe principale du jeu Pac-Man.
    """

    def __init__(self):

        self.largeur = 800
        self.hauteur = 500

        self.root = tk.Tk()
        self.root.title("Pac-Man")

        self.canvas = tk.Canvas(
            self.root,
            width=self.largeur,
            height=self.hauteur,
            bg="black"
        )

        # UI score + boutons
        self.score = 0
        self.running = False
        self.game_over = False

        self.score_label = tk.Label(self.root, text="Score : 0", font=("Arial", 14))
        self.score_label.pack(fill="x")

        self.canvas.pack()

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill="x", pady=4)

        tk.Button(btn_frame, text="Jouer", command=self.start_game).pack(side="left", expand=True, fill="x", padx=2)
        tk.Button(btn_frame, text="Rejouer", command=self.reset_game).pack(side="left", expand=True, fill="x", padx=2)
        tk.Button(btn_frame, text="Quitter", command=self.root.destroy).pack(side="left", expand=True, fill="x", padx=2)

        self.joueur = Joueur(self.canvas, 100, 100, 30, self.largeur, self.hauteur)

        self.fantome = Fantome(self.canvas, 600, 300, 30, self.largeur, self.hauteur)

        self.grille = Grille(self.canvas, self.largeur, self.hauteur)
        self.grille.creer_points()
        self.grille.dessiner_bords()

        # contrôles clavier

        self.root.bind("<Left>", self.joueur.aller_gauche)
        self.root.bind("<Right>", self.joueur.aller_droite)
        self.root.bind("<Up>", self.joueur.aller_haut)
        self.root.bind("<Down>", self.joueur.aller_bas)


    def collision_fantome(self):
        """
        Vérifie si Pac-Man touche un fantôme.
        """

        px1, py1, px2, py2 = self.joueur.position()
        fx1, fy1, fx2, fy2 = self.fantome.position()

        if px1 <= fx2 and px2 >= fx1 and py1 <= fy2 and py2 >= fy1:

            self.running = False
            self.game_over = True
            self.afficher_game_over()


    def boucle(self):
        """
        Boucle principale du jeu.
        """

        if self.running and not self.game_over:

            self.joueur.deplacer()
            self.fantome.deplacer(self.joueur)

            eaten = self.grille.verifier_collision(self.joueur)

            if eaten:
                self.score += eaten
                self.update_score()

            self.collision_fantome()

        self.root.after(50, self.boucle)


    def lancer(self):

        self.boucle()
        self.root.mainloop()


    def start_game(self):
        """
        Lance ou reprend la partie.
        """

        if not self.game_over:
            self.running = True


    def reset_game(self):
        """
        Réinitialise la partie et relance.
        """

        self.running = False
        self.game_over = False
        self.score = 0
        self.update_score()

        self.canvas.delete("all")

        # recrée les entités
        self.joueur = Joueur(self.canvas, 100, 100, 30, self.largeur, self.hauteur)
        self.fantome = Fantome(self.canvas, 600, 300, 30, self.largeur, self.hauteur)
        self.grille = Grille(self.canvas, self.largeur, self.hauteur)
        self.grille.creer_points()
        self.grille.dessiner_bords()

        self.running = True


    def update_score(self):
        self.score_label.config(text=f"Score : {self.score}")


    def afficher_game_over(self):
        self.canvas.create_text(
            self.largeur // 2,
            self.hauteur // 2,
            text="GAME OVER",
            fill="red",
            font=("Arial", 32, "bold")
        )