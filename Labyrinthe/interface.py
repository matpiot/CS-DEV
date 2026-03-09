import tkinter as tk
from jeu import Jeu

class Interface:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Labyrinthe")

        self.largeur = 600
        self.hauteur = 600

        self.canvas = tk.Canvas(
            self.root,
            width=self.largeur,
            height=self.hauteur,
            bg="white"
        )

        self.canvas.pack()

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.btn_jouer = tk.Button(self.frame, text="Jouer", command=self.jouer)
        self.btn_jouer.pack(side=tk.LEFT, padx=10)

        self.btn_rejouer = tk.Button(self.frame, text="Rejouer", command=self.rejouer)
        self.btn_rejouer.pack(side=tk.LEFT, padx=10)

        self.btn_quitter = tk.Button(self.frame, text="Quitter", command=self.root.destroy)
        self.btn_quitter.pack(side=tk.LEFT, padx=10)

        self.label_score = tk.Label(self.root, text="Score : 0")
        self.label_score.pack()

        self.root.bind("<Left>", lambda e: self.deplacer(-30,0))
        self.root.bind("<Right>", lambda e: self.deplacer(30,0))
        self.root.bind("<Up>", lambda e: self.deplacer(0,-30))
        self.root.bind("<Down>", lambda e: self.deplacer(0,30))

        self.jeu = None

    def jouer(self):

        self.canvas.delete("all")
        self.jeu = Jeu(self.canvas, self.largeur, self.hauteur)

    def rejouer(self):

        self.jouer()

    def deplacer(self, dx, dy):

        if self.jeu is None:
            return

        self.jeu.deplacer(dx, dy)

        self.label_score.config(text=f"Score : {self.jeu.score}")

        if self.jeu.game_over:
            message = "Bravo ! Arrivée atteinte" if self.jeu.victoire else "GAME OVER"
            color = "green" if self.jeu.victoire else "red"
            self.canvas.create_text(
                300,
                300,
                text=message,
                font=("Arial",40),
                fill=color
            )

    def lancer(self):
        self.root.mainloop()


if __name__ == "__main__":

    app = Interface()
    app.lancer()