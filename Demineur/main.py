import tkinter as tk
from tkinter import messagebox

from grille import Grille


class DemineurGUI:
    """Interface graphique simple pour le démineur."""

    def __init__(self, taille=8, nb_mines=10):
        self.grille = Grille(taille=taille, nb_mines=nb_mines)
        self.taille = taille
        self.nb_mines = nb_mines
        self.game_over = False

        self.root = tk.Tk()
        self.root.title("Démineur")

        header = tk.Frame(self.root)
        header.pack(pady=(8, 4))
        tk.Label(header, text=f"Grille {taille} x {taille}").pack(side="left", padx=6)
        tk.Label(header, text=f"Mines : {nb_mines}").pack(side="left", padx=6)

        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(padx=10, pady=10)

        self.buttons = {}
        self._build_grid()

    def _build_grid(self):
        for x in range(self.taille):
            for y in range(self.taille):
                btn = tk.Button(
                    self.grid_frame,
                    width=3,
                    height=1,
                    text="",
                    command=lambda a=x, b=y: self._on_click(a, b),
                    font=("Consolas", 12, "bold"),
                    relief="raised",
                )
                btn.grid(row=x, column=y, padx=1, pady=1, sticky="nsew")
                self.buttons[(x, y)] = btn

        for i in range(self.taille):
            self.grid_frame.grid_rowconfigure(i, weight=1)
            self.grid_frame.grid_columnconfigure(i, weight=1)

    def _on_click(self, x, y):
        if self.game_over:
            return

        case = self.grille.reveler_case(x, y)
        if case is None:
            return

        self._sync_buttons()

        if case.mine:
            self.game_over = True
            self._reveal_all_mines()
            messagebox.showinfo("Perdu", "BOOM ! Tu as déclenché une mine.")
            return

        if self.grille.toutes_les_cases_revelees():
            self.game_over = True
            self._disable_all()
            messagebox.showinfo("Gagné", "Bravo ! Toutes les cases sûres sont révélées.")

    def _sync_buttons(self):
        colors = {
            1: "#1565c0",
            2: "#2e7d32",
            3: "#c62828",
            4: "#283593",
            5: "#4e342e",
            6: "#00838f",
            7: "#424242",
            8: "#1b5e20",
        }

        for x in range(self.taille):
            for y in range(self.taille):
                case = self.grille.grille[x][y]
                btn = self.buttons[(x, y)]

                if not case.revelee:
                    btn.config(text="", bg="SystemButtonFace", relief="raised")
                    continue

                if case.mine:
                    btn.config(text="*", bg="#d32f2f", fg="white", relief="sunken")
                    continue

                if case.mines_voisines == 0:
                    btn.config(text="", bg="#e0e0e0", relief="sunken")
                else:
                    color = colors.get(case.mines_voisines, "black")
                    btn.config(
                        text=str(case.mines_voisines),
                        fg=color,
                        bg="#e0e0e0",
                        relief="sunken",
                    )

    def _reveal_all_mines(self):
        for x in range(self.taille):
            for y in range(self.taille):
                case = self.grille.grille[x][y]
                if case.mine:
                    case.reveler()
        self._sync_buttons()
        self._disable_all()

    def _disable_all(self):
        for btn in self.buttons.values():
            btn.config(state="disabled")

    def lancer(self):
        self.root.mainloop()


if __name__ == "__main__":
    DemineurGUI(taille=8, nb_mines=10).lancer()