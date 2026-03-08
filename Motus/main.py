import random
import tkinter as tk
from tkinter import messagebox

from motsecret import MotSecret
from tentative import Tentative


class JeuMotusGUI:
    """Interface graphique simple pour jouer à Motus."""

    def __init__(self, mots_possibles, nb_tentatives=6):
        mot = random.choice(mots_possibles)
        self.mot_secret = MotSecret(mot)
        self.nb_tentatives = nb_tentatives
        self.tentatives_effectuees = 0

        self.root = tk.Tk()
        self.root.title("Motus")

        self.status_var = tk.StringVar(value=f"Il te reste {self.nb_tentatives} tentatives.")

        self._build_ui()

    def _build_ui(self):
        tk.Label(self.root, text="MOTUS", font=("Segoe UI", 18, "bold")).pack(pady=(10, 4))
        tk.Label(
            self.root,
            text=f"Trouve le mot de {len(self.mot_secret.mot)} lettres",
        ).pack()
        tk.Label(self.root, textvariable=self.status_var).pack(pady=(0, 8))

        self.attempts_frame = tk.Frame(self.root)
        self.attempts_frame.pack(padx=10, pady=10, fill="x")

        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=(0, 10))

        self.entry = tk.Entry(
            input_frame,
            width=max(10, len(self.mot_secret.mot) + 2),
            font=("Consolas", 14),
        )
        self.entry.pack(side="left", padx=(0, 6))
        self.entry.focus_set()

        submit = tk.Button(input_frame, text="Valider", command=self._on_submit)
        submit.pack(side="left")

        self.entry.bind("<Return>", self._on_submit)

    def _render_attempt(self, tentative: Tentative):
        colors = {
            "VERT": "#4caf50",
            "JAUNE": "#f9a825",
            "GRIS": "#9e9e9e",
        }

        row = tk.Frame(self.attempts_frame)
        row.pack(anchor="w", pady=2)

        for lettre, statut in zip(tentative.mot_propose, tentative.resultat):
            cell = tk.Label(
                row,
                text=lettre.upper(),
                width=2,
                height=1,
                bg=colors.get(statut, "#9e9e9e"),
                fg="white",
                font=("Consolas", 14, "bold"),
            )
            cell.pack(side="left", padx=2, ipadx=6, ipady=4)

    def _on_submit(self, event=None):  # noqa: ARG002 - event is unused
        proposition = self.entry.get().strip().lower()

        if not proposition:
            self.status_var.set("Entre un mot.")
            return

        if len(proposition) != len(self.mot_secret.mot):
            self.status_var.set(
                f"Le mot doit faire {len(self.mot_secret.mot)} lettres."
            )
            return

        if not proposition.isalpha():
            self.status_var.set("Utilise uniquement des lettres.")
            return

        self.entry.delete(0, tk.END)

        tentative = Tentative(proposition)
        tentative.evaluer(self.mot_secret)
        self._render_attempt(tentative)

        self.tentatives_effectuees += 1

        if self.mot_secret.est_trouve(proposition):
            self.status_var.set("Bravo ! Mot trouvé.")
            messagebox.showinfo("Gagné", "Bravo ! Tu as trouvé le mot.")
            self._disable_inputs()
            return

        restantes = self.nb_tentatives - self.tentatives_effectuees

        if restantes <= 0:
            self.status_var.set(
                f"Perdu ! Le mot était {self.mot_secret.mot.upper()}."
            )
            messagebox.showinfo(
                "Perdu",
                f"Le mot était {self.mot_secret.mot.upper()}.",
            )
            self._disable_inputs()
            return

        self.status_var.set(f"Il te reste {restantes} tentative(s).")

    def _disable_inputs(self):
        self.entry.config(state="disabled")

    def lancer(self):
        self.root.mainloop()


if __name__ == "__main__":
    liste_mots = [
        "pomme",
        "train",
        "robot",
        "table",
        "terre",
        "lampe",
        "livre",
        "chaud",
        "froid",
        "melon",
        "banjo",
        "nuage",
        "souris",
        "cactus",
        "piano",
        "plage",
        "avion",
        "cheval",
        "sapin",
    ]

    JeuMotusGUI(liste_mots).lancer()