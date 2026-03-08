import tkinter as tk
from grille import Grille
from joueur import Joueur


class Jeu:
    """
    Classe principale qui gère la partie.
    """

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Morpion")

        self.grille = Grille()

        self.joueur1 = Joueur("Joueur 1", "X")
        self.joueur2 = Joueur("Joueur 2", "O")
        self.score1 = 0
        self.score2 = 0

        self.joueur_actuel = self.joueur1

        self.boutons = []

        self.creer_interface()


    def creer_interface(self):
        """
        Crée les boutons de la grille graphique.
        """

        top = tk.Frame(self.root)
        top.grid(row=0, column=0, columnspan=3, pady=5)

        self.score_label = tk.Label(top, text="Joueur 1 : 0 | Joueur 2 : 0", font=("Arial", 12))
        self.score_label.pack()

        for i in range(3):

            ligne = []

            for j in range(3):

                bouton = tk.Button(
                    self.root,
                    text="",
                    width=10,
                    height=4,
                    font=("Arial", 24),
                    command=lambda l=i, c=j: self.jouer(l, c)
                )

                bouton.grid(row=i+1, column=j)

                ligne.append(bouton)

            self.boutons.append(ligne)

        bottom = tk.Frame(self.root)
        bottom.grid(row=4, column=0, columnspan=3, pady=5)

        tk.Button(bottom, text="Rejouer", command=self.reset_partie).pack(side="left", padx=5)
        tk.Button(bottom, text="Quitter", command=self.root.destroy).pack(side="left", padx=5)


    def jouer(self, ligne, colonne):
        """
        Gère un coup joué par un joueur.
        """

        symbole = self.joueur_actuel.symbole

        if self.grille.placer(ligne, colonne, symbole):

            self.boutons[ligne][colonne].config(text=symbole)

            if self.grille.victoire(symbole):

                self.handle_victoire()
                return

            if self.grille.pleine():

                self.afficher_message("Match nul")
                return

            self.changer_joueur()


    def changer_joueur(self):
        """
        Change de joueur.
        """

        if self.joueur_actuel == self.joueur1:
            self.joueur_actuel = self.joueur2
        else:
            self.joueur_actuel = self.joueur1


    def desactiver_grille(self):
        """
        Désactive tous les boutons.
        """

        for ligne in self.boutons:
            for bouton in ligne:
                bouton.config(state="disabled")


    def activer_grille(self):
        for ligne in self.boutons:
            for bouton in ligne:
                bouton.config(state="normal", text="")


    def handle_victoire(self):
        if self.joueur_actuel == self.joueur1:
            self.score1 += 1
        else:
            self.score2 += 1

        self.update_scores()
        self.afficher_message(f"{self.joueur_actuel.nom} gagne !")
        self.desactiver_grille()


    def update_scores(self):
        self.score_label.config(text=f"Joueur 1 : {self.score1} | Joueur 2 : {self.score2}")


    def reset_partie(self):
        self.grille = Grille()
        self.activer_grille()
        self.joueur_actuel = self.joueur1


    def afficher_message(self, texte):
        popup = tk.Toplevel(self.root)
        popup.title("Information")
        tk.Label(popup, text=texte, font=("Arial", 14)).pack(padx=10, pady=10)
        tk.Button(popup, text="OK", command=popup.destroy).pack(pady=5)


    def lancer(self):
        """
        Lance la fenêtre du jeu.
        """

        self.root.mainloop()