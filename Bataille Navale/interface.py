import tkinter as tk


TAILLE_CASE = 40
TAILLE_GRILLE = 10


class InterfaceJeu:
    """Interface graphique Tkinter."""

    def __init__(self, jeu):

        self.jeu = jeu

        self.root = tk.Tk()
        self.root.title("Bataille Navale")

        self.canvas = tk.Canvas(
            self.root,
            width=TAILLE_CASE * TAILLE_GRILLE,
            height=TAILLE_CASE * TAILLE_GRILLE
        )

        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.cliquer)

        self.dessiner_grille()

    def dessiner_grille(self):

        for i in range(TAILLE_GRILLE):
            for j in range(TAILLE_GRILLE):

                x1 = i * TAILLE_CASE
                y1 = j * TAILLE_CASE
                x2 = x1 + TAILLE_CASE
                y2 = y1 + TAILLE_CASE

                self.canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue")

    def cliquer(self, event):

        x = event.x // TAILLE_CASE
        y = event.y // TAILLE_CASE

        resultat = self.jeu.tirer((x, y))

        couleur = "white"

        if resultat == "touche":
            couleur = "red"

        x1 = x * TAILLE_CASE
        y1 = y * TAILLE_CASE
        x2 = x1 + TAILLE_CASE
        y2 = y1 + TAILLE_CASE

        self.canvas.create_rectangle(x1, y1, x2, y2, fill=couleur)

        if self.jeu.est_termine():

            self.canvas.create_text(
                200,
                200,
                text="Victoire !",
                font=("Arial", 30),
                fill="green"
            )

    def lancer(self):

        self.root.mainloop()