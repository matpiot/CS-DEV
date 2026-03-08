import tkinter as tk
from tkinter import messagebox

from grille import Grille


class Puissance4GUI:
    """Interface graphique simple pour Puissance 4."""

    def __init__(self, lignes=6, colonnes=7):
        self.grille = Grille(lignes=lignes, colonnes=colonnes)
        self.lignes = lignes
        self.colonnes = colonnes
        self.cell_size = 70
        self.marge = 10
        self.game_over = False

        self.joueurs = [
            {"nom": "Rouge", "symbole": "X", "couleur": "#e53935"},
            {"nom": "Jaune", "symbole": "O", "couleur": "#fdd835"},
        ]
        self.joueur_index = 0

        self.root = tk.Tk()
        self.root.title("Puissance 4")

        header = tk.Frame(self.root)
        header.pack(pady=(8, 4))

        self.status_var = tk.StringVar()
        tk.Label(header, textvariable=self.status_var, font=("Segoe UI", 12, "bold")).pack()

        self.canvas = tk.Canvas(
            self.root,
            width=self.colonnes * self.cell_size + 2 * self.marge,
            height=self.lignes * self.cell_size + 2 * self.marge,
            bg="#0d47a1",
            highlightthickness=0,
        )
        self.canvas.pack(padx=10, pady=10)

        self.canvas.bind("<Button-1>", self._on_click)

        self._draw_board()
        self._update_status()

    def _current_player(self):
        return self.joueurs[self.joueur_index]

    def _toggle_player(self):
        self.joueur_index = 1 - self.joueur_index
        self._update_status()

    def _update_status(self, message=None):
        if message:
            self.status_var.set(message)
        else:
            joueur = self._current_player()
            self.status_var.set(f"Au tour de {joueur['nom']} ({joueur['symbole']})")

    def _draw_board(self):
        self.canvas.delete("all")

        for i in range(self.lignes):
            for j in range(self.colonnes):
                x0 = self.marge + j * self.cell_size
                y0 = self.marge + i * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, fill="#0d47a1", outline="#0a3574")

                case = self.grille.grille[i][j]
                couleur = "white"
                if case.symbole == "X":
                    couleur = self.joueurs[0]["couleur"]
                elif case.symbole == "O":
                    couleur = self.joueurs[1]["couleur"]

                cx = x0 + self.cell_size / 2
                cy = y0 + self.cell_size / 2
                r = self.cell_size * 0.38
                self.canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill=couleur, outline="#08306b")

    def _on_click(self, event):
        if self.game_over:
            return

        colonne = (event.x - self.marge) // self.cell_size
        colonne = int(colonne)

        if not self.grille.colonne_valide(colonne):
            self._update_status("Colonne pleine ou invalide.")
            return

        joueur = self._current_player()
        position = self.grille.placer_jeton(colonne, joueur["symbole"])
        if position is None:
            self._update_status("Colonne pleine.")
            return

        self._draw_board()

        if self.grille.verifier_victoire(joueur["symbole"]):
            self.game_over = True
            self._update_status(f"{joueur['nom']} gagne !")
            messagebox.showinfo("Victoire", f"{joueur['nom']} gagne !")
            return

        if self.grille.est_pleine():
            self.game_over = True
            self._update_status("Match nul.")
            messagebox.showinfo("Match nul", "Plus de coups possibles.")
            return

        self._toggle_player()

    def lancer(self):
        self.root.mainloop()


if __name__ == "__main__":
    Puissance4GUI().lancer()