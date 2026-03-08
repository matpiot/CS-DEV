"""
Interface graphique Tkinter pour le Mastermind : gère la saisie des tentatives,
l'affichage des retours et le cycle de partie.
"""

import tkinter as tk
from tkinter import messagebox
from jeu import Jeu

class Interface:
    def __init__(self):
        """
        Entrée : aucune.
        Sortie : None.
        Effet : instancie la fenêtre Tkinter, prépare les menus déroulants de couleurs,
        les boutons d'action et le conteneur des résultats, et crée un objet `Jeu`.
        """
        self.jeu = Jeu()
        self.root = tk.Tk()
        self.root.title("Mastermind")
        self.couleurs = self.jeu.code_secret.couleurs

        # Frame pour entrer les tentatives
        self.frame_input = tk.Frame(self.root)
        self.frame_input.pack(pady=10)

        self.entries = []
        for i in range(self.jeu.code_secret.longueur):
            var = tk.StringVar()
            entry = tk.OptionMenu(self.frame_input, var, *self.couleurs)
            entry.var = var
            entry.pack(side=tk.LEFT, padx=5)
            self.entries.append(entry)

        self.btn_valider = tk.Button(self.root, text="Valider", command=self.valider)
        self.btn_valider.pack(pady=10)

        # Frame pour afficher le résultat
        self.frame_result = tk.Frame(self.root)
        self.frame_result.pack(pady=10)

        self.labels_result = []

    def valider(self):
        """
        Entrée : aucune (utilise les valeurs sélectionnées dans les menus déroulants).
        Sortie : None.
        Effet : lit la tentative, l'envoie au jeu, affiche le retour bien/mal placés,
        et gère les états de victoire ou défaite via des pop-ups.
        """
        choix = [e.var.get() for e in self.entries]
        if "" in choix:
            messagebox.showwarning("Erreur", "Veuillez sélectionner toutes les couleurs")
            return

        bien_places, mal_places = self.jeu.jouer_tentative(choix)
        label = tk.Label(self.frame_result, text=f"Tentative {self.jeu.tour_actuel}: {choix} | Bien placés: {bien_places}, Mal placés: {mal_places}")
        label.pack()
        self.labels_result.append(label)

        if self.jeu.gagne:
            messagebox.showinfo("Gagné !", f"Félicitations ! Vous avez trouvé le code: {self.jeu.code_secret.code}")
            self.root.destroy()
        elif self.jeu.tour_actuel >= self.jeu.max_tours:
            messagebox.showinfo("Perdu", f"Vous avez perdu. Le code était: {self.jeu.code_secret.code}")
            self.root.destroy()

    def lancer(self):
        """
        Entrée : aucune.
        Sortie : None.
        Effet : lance la boucle principale Tkinter.
        """
        self.root.mainloop()

if __name__ == "__main__":
    app = Interface()
    app.lancer()