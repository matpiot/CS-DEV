import tkinter as tk
from grille import Grille


class Jeu:
    """
    Gère l'interface graphique et les interactions clavier.
    """

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("2048")

        self.grille = Grille()

        self.score_label = tk.Label(self.root, text="Score : 0", font=("Arial", 16))
        self.score_label.pack()

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.labels = [[None]*4 for _ in range(4)]

        for i in range(4):
            for j in range(4):

                label = tk.Label(
                    self.frame,
                    text="",
                    width=6,
                    height=3,
                    font=("Arial", 20),
                    borderwidth=2,
                    relief="ridge"
                )

                label.grid(row=i, column=j)

                self.labels[i][j] = label


        self.creer_boutons()

        self.root.bind("<Left>", self.gauche)
        self.root.bind("<Right>", self.droite)
        self.root.bind("<Up>", self.haut)
        self.root.bind("<Down>", self.bas)

        self.mettre_a_jour()

        self.game_over_label = None
        self.game_over = False


    def creer_boutons(self):
        """
        Crée les boutons Jouer, Rejouer et Quitter.
        """

        frame_boutons = tk.Frame(self.root)
        frame_boutons.pack(pady=10)

        tk.Button(frame_boutons, text="Jouer", command=self.nouvelle_partie).grid(row=0, column=0)
        tk.Button(frame_boutons, text="Rejouer", command=self.nouvelle_partie).grid(row=0, column=1)
        tk.Button(frame_boutons, text="Quitter", command=self.root.destroy).grid(row=0, column=2)


    def nouvelle_partie(self):
        """
        Réinitialise la grille.
        """

        self.grille = Grille()
        self.game_over = False
        self.clear_game_over()
        self.mettre_a_jour()


    def mettre_a_jour(self):
        """
        Met à jour l'affichage graphique.
        """

        for i in range(4):
            for j in range(4):

                valeur = self.grille.grille[i][j]

                if valeur == 0:
                    texte = ""
                else:
                    texte = str(valeur)

                self.labels[i][j].config(text=texte)

        self.score_label.config(text="Score : " + str(self.grille.score))

        if not self.grille.mouvements_possibles():
            self.game_over = True
            self.afficher_game_over()


    def gauche(self, event):
        if self.game_over:
            return
        if self.grille.mouvement_gauche():
            self.mettre_a_jour()

    def droite(self, event):
        if self.game_over:
            return
        if self.grille.mouvement_droite():
            self.mettre_a_jour()

    def haut(self, event):
        if self.game_over:
            return
        if self.grille.mouvement_haut():
            self.mettre_a_jour()

    def bas(self, event):
        if self.game_over:
            return
        if self.grille.mouvement_bas():
            self.mettre_a_jour()


    def lancer(self):
        self.root.mainloop()


    def afficher_game_over(self):
        if self.game_over_label:
            return

        self.game_over_label = tk.Label(self.root, text="Game Over", font=("Arial", 20), fg="red")
        self.game_over_label.pack(pady=5)


    def clear_game_over(self):
        if self.game_over_label:
            self.game_over_label.destroy()
            self.game_over_label = None